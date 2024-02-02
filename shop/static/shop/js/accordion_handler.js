"use strict";

window.addEventListener('load', accordion_handler());

function accordion_handler() {
    let selectedCheckBoxes = document.querySelectorAll('input[type="checkbox"]:checked');

    for (let checkBoxes of selectedCheckBoxes) {
        let id_group_accordion = checkBoxes.parentElement.parentElement.getAttribute('aria-labelledby');
        let groupCheckBoxes = document.querySelectorAll(`[aria-labelledby="${id_group_accordion}"]`);

        for (let elem of groupCheckBoxes) {
            elem.classList.add('show');
        }
    }
}