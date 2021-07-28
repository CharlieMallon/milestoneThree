// event listener for burger menu

const burgerButton = document.getElementById('burger-btn');

burgerButton.addEventListener('click', burgerMenu)

// Show/hide the menu on mobile

function burgerMenu() {
    var element = document.getElementById('burger-menu');
    element.classList.toggle('burger');
}

// event listeners for show/hide modal

const button = document.getElementById('add-task');
const span = document.getElementsByClassName('close')[0];
const modal = document.getElementById('add-modal')

button.addEventListener('click',(e)=> addModalOpen(e))
span.addEventListener('click', (e)=> addModalClose(e))
modal.addEventListener('click',(e)=> addModalClose(e))

// open the modal

function addModalOpen(e) {
    console.log('e.target :>> ', e.target.dataset.closer);
    if (e.target.dataset.closer === 'open'){
        console.log('happy :>> ', 'happy open');
        var element = document.getElementById('add-modal');
        element.classList.remove('hidden');
    }
}

// close the modal

function addModalClose(e) {
    console.log('e.target :>> ', e.target.dataset.closer);
    if (e.target.dataset.closer === 'close'){
        console.log('happy :>> ', 'happy close');
        var element = document.getElementById('add-modal');
        element.classList.add('hidden');
    }
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
