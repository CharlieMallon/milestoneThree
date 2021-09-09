// ---------- burger menu

// event listener for burger menu
const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu);

// Show/hide the menu on mobile

function burgerMenu() {
    // shows/hide the menu
    let element = document.getElementById('burger-menu');
    element.classList.toggle('burger');
    element.classList.toggle('hidden');
    // adds animation to burger button
    burgerButton.classList.toggle("is-active")
}

// ---------- open/close details of task
// get the bit that can be click
let colls = document.getElementsByClassName("task-header-internal");

for (let i = 0; i < colls.length; i++) {
    // for each task add an event listener
    colls[i].addEventListener('click', function() {
        let content = this.closest(".task-card");
        content.classList.toggle('open');

        let children = content.lastElementChild.children;
        let height = 0;
        // if opening task calculate contents height
        if (content.classList.contains('open')){
            for (let j = 0; j < children.length; j++) {
                let childHeight = children[j].offsetHeight;
                height = height + childHeight;
            }
        }
        content.lastElementChild.style.height = `${height}px`;
    }); 
};

// ---------- open delete task modal

let task = document.getElementsByClassName("open-modal");

for (let i = 0; i < task.length; i++) {
    task[i].addEventListener('click', function() {
        let content = this.nextElementSibling;
        content.classList.remove('hidden');
    });
};

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
        let element = e.target.closest(".modal-background");
        element.classList.add('hidden');
    }
}

// ---------- switch between category types

let cat = document.getElementsByClassName("add-cat")[0];

// if cat element exists add event listener
if (cat)
    // event listener
    cat.addEventListener('click', addCat)

// loops through thr elements with the class of 'cat' and toggles the hidden class
function addCat() {
    let catloop = document.getElementsByClassName("cat");

    for (let i = 0; i < catloop.length; i++) {
        catloop[i].classList.toggle('hidden');
    }
}

// ---------- Account tabs

// get the bit that can be click
let section = document.getElementsByClassName("section-header");

for (let i = 0; i < section.length; i++) {
    // for each task add an event listener
    section[i].addEventListener('click', function() {
        let content = this.closest(".section");
        content.classList.toggle('open');

        let children = content.lastElementChild.lastElementChild.children;
        let height = 0;
        // if opening task calculate contents height
        if (content.classList.contains('open')){
            for (let j = 0; j < children.length; j++) {
                let childHeight = children[j].offsetHeight;
                height = height + childHeight;
            }
        }
        content.lastElementChild.style.height = `${height}px`;
    }); 
};