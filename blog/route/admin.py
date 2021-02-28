import wtforms as wtf
from flask import session, redirect, url_for, request, render_template, current_app, flash, Blueprint

from flask_admin import AdminIndexView
from flask_admin.helpers import is_form_submitted
from flask_admin.contrib.mongoengine import ModelView

auth_bp = Blueprint(name="auth",
                    import_name=__name__,
                    template_folder="../template")


@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        if username != current_app.config[
                "USERNAME"] or password != current_app.config["PASSWORD"]:
            error = "Incorrect user name or password!"
        if error is None:
            session.clear()
            session["user_id"] = username
            return redirect(url_for("admin.index"))
        flash(error)
    return render_template("login.html")


@auth_bp.before_request
def set_session():
    session.permanent = False


def check_auth():
    return session.get("user_id") is not None


def challenge():
    return redirect(url_for('auth.login', next=request.url))


class CustomIndexlView(AdminIndexView):
    """
    Add login authentication to Admin index.
    """
    def is_accessible(self):
        return check_auth()

    def inaccessible_callback(self, name, **kwargs):
        return challenge()


class CustomModelView(ModelView):
    form_overrides = dict(content=wtf.FileField)

    def is_accessible(self):
        return check_auth()

    def inaccessible_callback(self, name, **kwargs):
        return challenge()

    def get_create_form(self):
        form = self.get_form()
        return form

    @staticmethod
    def get_form_data():
        if not is_form_submitted():
            return None
        formdata = request.form
        if request.files:
            formdata = formdata.copy()
            formdata.update({
                k: v.read().decode("utf-8")
                for k, v in request.files.items()
            })
        return formdata

    def create_form(self, obj=None):
        """Change default behevior to allow file type of content"""
        return self.get_create_form()(CustomModelView.get_form_data(), obj=obj)
