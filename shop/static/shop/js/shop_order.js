"use strict";

window.addEventListener('load', elements_listener());

async function elements_listener() {
    let button_save = document.getElementById('Save');

    if (button_save) {
        button_save.addEventListener('click', save_document);
    }

    let button_print = document.getElementById('Print');
}

async function save_document() {
    let request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getCustomerDocuments&document_code=${document_code}`;

}