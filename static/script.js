// event listener for burger menu

const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu)

// Show/hide the menu on mobile

function burgerMenu() {
    var element = document.getElementById("burger-menu");
    element.classList.toggle("burger");
}
