// ---------- Shave JS code -----------
/**
shave - Shave is a javascript plugin that truncates multi-line text within a html element based on set max height
@version v2.5.7
@link https://github.com/dollarshaveclub/shave#readme
@author Jeff Wainwright <yowainwright@gmail.com> (jeffry.in)
@license MIT
**/
(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined'
		? (module.exports = factory())
		: typeof define === 'function' && define.amd
		? define(factory)
		: ((global = global || self), (global.shave = factory()));
})(this, function () {
	'use strict';

	function shave(target, maxHeight) {
		var opts = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : {};
		if (typeof maxHeight === 'undefined' || isNaN(maxHeight))
			throw Error('maxHeight is required');
		var els = typeof target === 'string' ? document.querySelectorAll(target) : target;
		if (!els) return;
		var character = opts.character || '…';
		var classname = opts.classname || 'js-shave';
		var spaces = typeof opts.spaces === 'boolean' ? opts.spaces : true;
		var charHtml = '<span class="js-shave-char">'.concat(character, '</span>');
		if (!('length' in els)) els = [els];

		for (var i = 0; i < els.length; i += 1) {
			var el = els[i];
			var styles = el.style;
			var span = el.querySelector('.'.concat(classname));
			var textProp = el.textContent === undefined ? 'innerText' : 'textContent'; // If element text has already been shaved

			if (span) {
				// Remove the ellipsis to recapture the original text
				el.removeChild(el.querySelector('.js-shave-char'));
				el[textProp] = el[textProp]; // eslint-disable-line
				// nuke span, recombine text
			}

			var fullText = el[textProp];
			var words = spaces ? fullText.split(' ') : fullText; // If 0 or 1 words, we're done

			if (words.length < 2) continue; // Temporarily remove any CSS height for text height calculation

			var heightStyle = styles.height;
			styles.height = 'auto';
			var maxHeightStyle = styles.maxHeight;
			styles.maxHeight = 'none'; // If already short enough, we're done

			if (el.offsetHeight <= maxHeight) {
				styles.height = heightStyle;
				styles.maxHeight = maxHeightStyle;
				continue;
			} // Binary search for number of words which can fit in allotted height

			var max = words.length - 1;
			var min = 0;
			var pivot = void 0;

			while (min < max) {
				pivot = (min + max + 1) >> 1; // eslint-disable-line no-bitwise

				el[textProp] = spaces ? words.slice(0, pivot).join(' ') : words.slice(0, pivot);
				el.insertAdjacentHTML('beforeend', charHtml);
				if (el.offsetHeight > maxHeight) max = pivot - 1;
				else min = pivot;
			}

			el[textProp] = spaces ? words.slice(0, max).join(' ') : words.slice(0, max);
			el.insertAdjacentHTML('beforeend', charHtml);
			var diff = spaces ? ' '.concat(words.slice(max).join(' ')) : words.slice(max);
			var shavedText = document.createTextNode(diff);
			var elWithShavedText = document.createElement('span');
			elWithShavedText.classList.add(classname);
            // next line commented out and moved to the style sheet (lines 344 - 346)
			// elWithShavedText.style.display = 'none';
			elWithShavedText.appendChild(shavedText);
			el.insertAdjacentElement('beforeend', elWithShavedText);
			styles.height = heightStyle;
			styles.maxHeight = maxHeightStyle;
		}
	}

	return shave;
});

// -------------  end of Shave JS code ----------

// ---------- Shave titles

let toShave = document.getElementsByClassName('shave-me');

for (let i=0; i < toShave.length; i++) {
    shave(toShave[i], 60);
}

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

        let shaved = content.children

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

