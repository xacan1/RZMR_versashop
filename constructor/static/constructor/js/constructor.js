"use strict";


window.addEventListener('load', elements_listener());


function getCookie(name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function elements_listener() {
    get_types();
    get_groups_and_fittings1();
    get_groups_and_fittings2();
    get_diameters();
    get_lengths();

    let select_type = document.querySelector('#Types');

    if (select_type) {
        select_type.addEventListener('click', get_types);
    }

    let select_fittings1 = document.querySelector('#GroupsEndFittings1');

    if (select_fittings1) {
        select_fittings1.addEventListener('click', get_groups_and_fittings1);
    }

    let select_fittings2 = document.querySelector('#GroupsEndFittings2');

    if (select_fittings2) {
        select_fittings2.addEventListener('click', get_groups_and_fittings2);
    }

    let select_fittingsA1 = document.querySelector('#GroupsEndFittingsA1');

    if (select_fittingsA1) {
        select_fittingsA1.addEventListener('click', get_groups_and_fittingsA);
    }

    let select_fittingsA2 = document.querySelector('#GroupsEndFittingsA2');

    if (select_fittingsA2) {
        select_fittingsA2.addEventListener('click', get_groups_and_fittingsA);
    }

    let select_diameters = document.querySelector('#Diameters');

    if (select_diameters) {
        select_diameters.addEventListener('click', get_diameters);
    }

    let select_pressures = document.querySelector('#Pressures');

    if (select_pressures) {
        select_pressures.addEventListener('click', get_pressures);
    }

    let select_lengths = document.querySelector('#LengthsHoses');

    if (select_lengths) {
        select_lengths.addEventListener('click', get_lengths);
    }

    let select_innerscreen = document.querySelector('#InnerScreen');

    if (select_innerscreen) {
        select_innerscreen.addEventListener('click', get_innerscreen);
    }

    let select_braids = document.querySelector('#Braids');

    if (select_braids) {
        select_braids.addEventListener('click', get_braids);
    }

    let select_materials1 = document.querySelector('#Materials1');

    if (select_materials1) {
        select_materials1.addEventListener('click', get_materials);
    }

    let select_materials2 = document.querySelector('#Materials2');

    if (select_materials2) {
        select_materials2.addEventListener('click', get_materials);
    }

    let select_materialsA1 = document.querySelector('#MaterialsA1');

    if (select_materialsA1) {
        select_materialsA1.addEventListener('click', get_materials);
    }

    let select_materialsA2 = document.querySelector('#MaterialsA2');

    if (select_materialsA2) {
        select_materialsA2.addEventListener('click', get_materials);
    }

    let select_types_fittings1 = document.querySelector('#TypeFitting1');

    if (select_types_fittings1) {
        select_types_fittings1.addEventListener('click', get_types_fittings1);
    }

    let select_types_fittings2 = document.querySelector('#TypeFitting2');

    if (select_types_fittings2) {
        select_types_fittings2.addEventListener('click', get_types_fittings2);
    }
}

async function get_types() {
    let select_type = document.querySelector('#Types');

    if (select_type.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListProductType',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP types: ' + response.status);
        return;
    }

    let types = await response.json();

    if (Object.keys(types).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let type of types.list) {
        let option = document.createElement('option');
        option.value = type.Code;
        option.textContent = type.Value;
        select_type.appendChild(option);
    }
}


async function get_groups_and_fittings1() {
    let select_groups_fittings = document.querySelector('#GroupsEndFittings1');

    if (select_groups_fittings.childNodes.length > 1) {
        let select_type_fitting1 = document.querySelector('#TypeFitting1');
        select_type_fitting1.innerHTML = '';
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP fitting1: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_groups_fittings.appendChild(option);
    }
}

async function get_groups_and_fittings2() {
    let select_fittings = document.querySelector('#GroupsEndFittings2');

    if (select_fittings.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP fitting2: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_fittings.appendChild(option);
    }
}

async function get_groups_and_fittingsA() {
    let id = this.getAttribute('id');
    let select_fittings = document.querySelector(`#${id}`);

    if (select_fittings.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP fitting1: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_fittings.appendChild(option);
    }
}

async function get_diameters() {
    let select_diameters = document.querySelector('#Diameters');

    // очистка всех зависимых полей при смене диаметра
    if (select_diameters.childNodes.length > 1) {
        document.querySelector('#TypeFitting1').innerHTML = '';
        document.querySelector('#TypeFitting2').innerHTML = '';
        document.querySelector('#Pressures').innerHTML = '';
        document.querySelector('#InnerScreen').innerHTML = '';
        document.querySelector('#Braids').innerHTML = '';
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListDiameters',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP diameters: ' + response.status);
        return;
    }

    let diameters = await response.json();

    if (Object.keys(diameters).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let diameter of diameters.list) {
        let option = document.createElement('option');
        option.value = diameter.Code;
        option.textContent = diameter.Value;
        select_diameters.appendChild(option);
    }
}

async function get_pressures() {
    let select_pressures = document.querySelector('#Pressures');

    // очистка всех зависимых полей при смене давления
    if (select_pressures.childNodes.length > 1) {
        document.querySelector('#TypeFitting1').innerHTML = '';
        document.querySelector('#TypeFitting2').innerHTML = '';
        document.querySelector('#Braids').innerHTML = '';
        return;
    }

    let diameter = document.querySelector('#Diameters');

    if (diameter) {
        diameter = diameter.value;
    }

    let request1C = '';

    if (diameter) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListPressureHoseStartSelection&diameter=${diameter}`;
    }
    else {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': request1C,
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let pressures = await response.json();

    if (Object.keys(pressures).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let pressure of pressures.list) {
        let option = document.createElement('option');
        option.value = pressure.Code;
        option.textContent = pressure.Value;
        select_pressures.appendChild(option);
    }

    // get_braid();
}

async function get_innerscreen() {
    let select_innerscreens = document.querySelector('#InnerScreen');

    if (select_innerscreens.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters');

    if (diameter) {
        diameter = diameter.value;
    }

    let request1C = '';

    if (diameter) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListInnerScreenStartSelection&diameter=${diameter}`;
    }
    else {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': encodeURI(request1C),
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let innerscreens = await response.json();

    if (Object.keys(innerscreens).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let innerscreen of innerscreens.list) {
        let option = document.createElement('option');
        option.value = innerscreen.Code;
        option.textContent = innerscreen.Value;
        select_innerscreens.appendChild(option);
    }
}

async function get_braid() {
    let select_braid = document.querySelector('#Braids');

    if (select_braid.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters');

    if (diameter) {
        diameter = diameter.value;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure) {
        pressure = pressure.value;
    }

    let request1C = '';

    if (pressure && diameter) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getBraid&pressure=${pressure}&diameter=${diameter}`;
    }
    else {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': encodeURI(request1C),
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let braid = await response.json();

    if (Object.keys(braid).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    let option = document.createElement('option');
    option.value = braid.Code;
    option.textContent = braid.Value;
    select_braid.appendChild(option);
}

async function get_braids() {
    let select_braid = document.querySelector('#Braids');

    if (select_braid.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters');

    if (diameter) {
        diameter = diameter.value;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure) {
        pressure = pressure.value;
    }

    let request1C = '';

    if (pressure && diameter) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListBraidStartSelection&pressure=${pressure}&diameter=${diameter}`;
    }
    else {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': encodeURI(request1C),
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let braids = await response.json();

    if (Object.keys(braids).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let braid of braids.list) {
        let option = document.createElement('option');
        option.value = braid.Code;
        option.textContent = braid.Value;
        select_braid.appendChild(option);
    }
}

async function get_lengths() {
    let select_lengths = document.querySelector('#LengthsHoses');

    if (select_lengths.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListLengthsHoses',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP lengths: ' + response.status);
        return;
    }

    let lengths = await response.json();

    if (Object.keys(lengths).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let length of lengths.list) {
        let option = document.createElement('option');
        option.value = length.Code;
        option.textContent = length.Value;
        select_lengths.appendChild(option);
    }
}


async function get_materials() {
    let id = this.getAttribute('id');
    let select_lengths = document.querySelector(`#${id}`);

    if (select_lengths.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListMaterials',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP materials: ' + response.status);
        return;
    }

    let lengths = await response.json();

    if (Object.keys(lengths).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let length of lengths.list) {
        let option = document.createElement('option');
        option.value = length.Code;
        option.textContent = length.Value;
        select_lengths.appendChild(option);
    }
}

async function get_types_fittings1() {
    let select_type_fitting1 = document.querySelector('#TypeFitting1');

    if (select_type_fitting1.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittings1');

    if (group_code) {
        group_code = group_code.value;
    }

    let diameter = document.querySelector('#Diameters');

    if (diameter) {
        diameter = diameter.value;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure) {
        pressure = pressure.value;
    }

    let request1C = '';

    if (group_code && diameter) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code}&diameter=${diameter}`;
    }
    else {
        return;
    }

    if (pressure) {
        request1C += `&pressure=${pressure}`;
    }

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': encodeURI(request1C),
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP materials: ' + response.status);
        return;
    }

    let lengths = await response.json();

    if (Object.keys(lengths).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let length of lengths.list) {
        let option = document.createElement('option');
        option.value = length.Code;
        option.textContent = length.Value;
        select_type_fitting1.appendChild(option);
    }
}

async function get_types_fittings2() {
    let id = this.getAttribute('id');
    let select_lengths = document.querySelector(`#${id}`);

    if (select_lengths.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittings2');
    return;

    let optoins = {
        methos: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_get_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP materials: ' + response.status);
        return;
    }

    let lengths = await response.json();

    if (Object.keys(lengths).length === 0) {
        console.log('Пустой ответ');
        return;
    }

    for (let length of lengths.list) {
        let option = document.createElement('option');
        option.value = length.Code;
        option.textContent = length.Value;
        select_lengths.appendChild(option);
    }
}