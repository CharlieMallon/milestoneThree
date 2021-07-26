// event listener for burger menu

const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu)

// Show/hide the menu on mobile

function burgerMenu() {
    var element = document.getElementById("burger-menu");
    element.classList.toggle("burger");
}

// event listeners for show/hide modal

const button = document.getElementById('add-task');
const span = document.getElementsByClassName("close")[0];
const close = document.getElementsByClassName("modal");

button.addEventListener('click', addModal)
span.addEventListener('click', addModal)
close.addEventListener('click', addModal)


// open/close the modal

function addModal() {
    var element = document.getElementById("add-modal");
    element.classList.toggle("hidden");
}