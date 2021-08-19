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

// open delete task modal

var task = document.getElementsByClassName("delete");

for (let i = 0; i < task.length; i++) {
    task[i].addEventListener('click', function() {
    var content = this.nextElementSibling;
    content.classList.remove('hidden')
});
}

// close delete task modal

const span = document.getElementsByClassName('close');

for (let i = 0; i < span.length; i++) {
    span[i].addEventListener('click', (e) => addModalClose(e))
}

const modal = document.getElementsByClassName('modal-background');

for (let i = 0; i < modal.length; i++) {
    modal[i].addEventListener('click', (e) => addModalClose(e))
}

const no = document.getElementsByClassName('no-btn');

for (let i = 0; i < no.length; i++) {
    no[i].addEventListener('click', (e) => addModalClose(e))
}

function addModalClose(e) {
    console.log('e.target :>> ', e.target.dataset.closer);
    if (e.target.dataset.closer === 'close'){
        // console.log('happy :>> ', 'happy close');
        var element = e.target.closest(".modal-background");
        // console.log('element :>> ', element);
        element.classList.add('hidden');
    }
}