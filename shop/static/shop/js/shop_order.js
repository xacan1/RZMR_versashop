"use strict";

window.addEventListener('load', elements_listener());


function get_cookie(name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function elements_listener() {
    let button_save = document.getElementById('Save');

    if (button_save) {
        button_save.addEventListener('click', get_pdf_document);
    }
}

async function get_pdf_document() {
    let external_code = document.getElementById('ExternalCode');
    let document_code = null;
    let document_date = null;

    if (external_code) {
        document_code = external_code.getAttribute('data-external-code');
        document_date = external_code.getAttribute('data-date-create');
    }

    if (!document_code) {
        return;
    }

    let request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getCustomerDocuments&document_code=${document_code}&document_type=0`;

    if (document_date) {
        request1C += `&date_document=${document_date}`;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': encodeURI(request1C),
        },
    };

    let response = await fetch('/shop/api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP get_pdf_document: ${response.status}`);
        return;
    }

    if (response.headers.get('Content-Disposition') === null) {
        let response_json = await response.json();

        if (Object.keys(response_json).length === 0) {
            console.log('Пустой ответ при получении PDF документов');
            return;
        }
    }
    else {
        let response_bytes = await response.blob();
        const pdf_url = URL.createObjectURL(response_bytes);
        const a_pdf = document.createElement('a');
        a_pdf.href = pdf_url;
        a_pdf.download = `${document_code}.pdf`;
        a_pdf.target = '_blank';
        a_pdf.click();
        URL.revokeObjectURL(pdf_url);
    }
}