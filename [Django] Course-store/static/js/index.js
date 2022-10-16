fetch("/menu-items").then((response) => {
    return response.json()
}).then((data) => {
    var navbar = document.getElementById("menuNav");
    var menu = "";
    for (let el of data) {
        menu += "<li class='nav-item'>" + "<a href='" + el.url + "' class='nav-link active'>" + el.name + "</a></li>"
    }
    navbar.innerHTML = menu;
});
