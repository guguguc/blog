function mark_current() {
    let pagenation = document.getElementsByClassName("pagination");
    if (pagenation.length === 0) return;
    pagenation = pagenation[0];
    let current = location.href;
    let page = pagenation.getElementsByTagName("a");
    for (let idx = 0; idx < page.length; ++idx) {
        if (page[idx].href === current) {
            page[idx].classList.add("current");
            console.log(page[idx].href);
            break;
        }
    }
}

mark_current();
