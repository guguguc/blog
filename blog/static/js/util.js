
const bar = document.querySelector("#search-bar");
let resp = document.querySelector(".test");

bar.addEventListener('input', function(e) {
    resp.value = e.target.value;
})
