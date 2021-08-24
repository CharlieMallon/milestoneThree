// ---------- burger menu

// event listener for burger menu

const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu)

// Show/hide the menu on mobile

function burgerMenu() {
    var element = document.getElementById('burger-menu');
    element.classList.toggle('burger');
    element.classList.toggle('hidden');
}

// ---------- open/close details of task

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

// ---------- open delete task modal

var task = document.getElementsByClassName("open-modal");

for (let i = 0; i < task.length; i++) {
    task[i].addEventListener('click', function() {
    var content = this.nextElementSibling;
    content.classList.remove('hidden')
});
}

// ---------- close a modal

// event listener for x span
const span = document.getElementsByClassName('close');

for (let i = 0; i < span.length; i++) {
    span[i].addEventListener('click', (e) => ModalClose(e))
}

// event listener for clicking off the modal
const modal = document.getElementsByClassName('modal-background');

for (let i = 0; i < modal.length; i++) {
    modal[i].addEventListener('click', (e) => ModalClose(e))
}

// event listener for 'no' or 'cancel' button on modal
const no = document.getElementsByClassName('no-btn');

for (let i = 0; i < no.length; i++) {
    no[i].addEventListener('click', (e) => ModalClose(e))
}

// close the modal by adding hidden on the background only if the data target is 'close'
function ModalClose(e) {
    if (e.target.dataset.closer === 'close'){
        var element = e.target.closest(".modal-background");
        element.classList.add('hidden');
    }
}

// ---------- switch between category types

var cat = document.getElementsByClassName("add-cat")[0];

// if cat element exists add event listener
if (cat)
    // event listener
    cat.addEventListener('click', addCat)

// loops through thr elements with the class of 'cat' and toggles the hidden class
function addCat() {
    var catloop = document.getElementsByClassName("cat");

    for (let i = 0; i < catloop.length; i++) {
        catloop[i].classList.toggle('hidden');
    }
}

// ---------- progress bar

