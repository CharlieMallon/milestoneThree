// event listener for burger menu

const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu)

// Show/hide the menu on mobile

function burgerMenu() {
    var element = document.getElementById('burger-menu');
    element.classList.toggle('burger');
}

// event lister for open/close details of task

var colls = document.getElementsByClassName("arrow");

for (let i = 0; i < colls.length; i++) {
    colls[i].addEventListener('click', function() {
        if (this.classList.contains('fa-caret-down')){
            this.classList.remove('fa-caret-down')
            this.classList.add('fa-caret-up')
        } else {
            this.classList.remove('fa-caret-up')
            this.classList.add('fa-caret-down')
        }
            
    var content = this.parentNode.parentNode.nextElementSibling;
    content.classList.toggle('hidden')
});
}
