"use strict";

window.addEventListener('load', mask_listener());

function mask_listener() {
    const element_phone1 = document.getElementById('phoneHeader');
    const maskOptions = {
        mask: '+7(000)000-00-00',
        lazy: false
    }

    if (element_phone1) {
        const mask_phone1 = new IMask(element_phone1, maskOptions);
    }

    const element_phone2 = document.getElementById('phone');

    if (element_phone2) {
        const mask_phone2 = new IMask(element_phone2, maskOptions);
    }

    const element2 = document.getElementById('email');
    let maskOptions2 = {
        mask: function (value) {
            if (/^[a-z0-9_\.-]+$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@[a-z0-9-]+$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}\.$/.test(value))
                return true;
            if (/^[a-z0-9_\.-]+@[a-z0-9-]+\.[a-z]{1,4}\.[a-z]{1,4}$/.test(value))
                return true;
            return false;
        },
        lazy: false
    }

    if (element2) {
        const mask2 = new IMask(element2, maskOptions2);
    }

    const element3 = document.getElementById('card');
    const maskOptions3 = {
        mask: '0000 0000 0000 0000',
        lazy: false
    }

    if (element3) {
        const mask3 = new IMask(element3, maskOptions3);
    }
}
