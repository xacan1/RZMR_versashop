"use strict";


window.addEventListener('load', elements_listener());


function get_cookie(name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function elements_listener() {
    let select_type = document.querySelector('#Types');

    if (select_type) {
        select_type.addEventListener('click', get_types);
    }

    let select_fittings1 = document.querySelector('#GroupsEndFittings1');

    if (select_fittings1) {
        select_fittings1.addEventListener('click', get_groups_and_fittings);
        select_fittings1.addEventListener('change', () => {
            document.querySelector('#TypeFitting1').innerHTML = '';
            clear_image('#img1');
        });
    }

    let select_fittings2 = document.querySelector('#GroupsEndFittings2');

    if (select_fittings2) {
        select_fittings2.addEventListener('click', get_groups_and_fittings);
        select_fittings2.addEventListener('change', () => {
            document.querySelector('#TypeFitting2').innerHTML = '';
            clear_image('#img2');
        });
    }

    let select_fittingsA1 = document.querySelector('#GroupsEndFittingsA1');

    if (select_fittingsA1) {
        select_fittingsA1.addEventListener('click', get_groups_and_fittings);
        select_fittingsA1.addEventListener('change', () => {
            document.querySelector('#TypeFittingA1').innerHTML = '';
            clear_image('#imgA1');
        });
    }

    let select_fittingsA2 = document.querySelector('#GroupsEndFittingsA2');

    if (select_fittingsA2) {
        select_fittingsA2.addEventListener('click', get_groups_and_fittings);
        select_fittingsA2.addEventListener('change', () => {
            document.querySelector('#TypeFittingA2').innerHTML = '';
            clear_image('#imgA2');
        });
    }

    let select_diameters = document.querySelector('#Diameters');

    if (select_diameters) {
        select_diameters.addEventListener('click', get_diameters);
        select_diameters.addEventListener('change', () => {
            document.querySelector('#TypeFitting1').innerHTML = '';
            clear_image('#img1');
            document.querySelector('#TypeFitting2').innerHTML = '';
            clear_image('#img2');
            document.querySelector('#Pressures').innerHTML = '';
            document.querySelector('#InnerScreen').innerHTML = '';
            document.querySelector('#Braids').innerHTML = '';
            document.querySelector('#Corrugation').innerHTML = '';
            get_corrugation();
        });
    }

    let select_pressures = document.querySelector('#Pressures');

    if (select_pressures) {
        select_pressures.addEventListener('click', get_pressures);
        select_pressures.addEventListener('change', () => {
            document.querySelector('#TypeFitting1').innerHTML = '';
            clear_image('#img1');
            document.querySelector('#TypeFitting2').innerHTML = '';
            clear_image('#img2');
            document.querySelector('#TypeFittingA1').innerHTML = '';
            document.querySelector('#TypeFittingA2').innerHTML = '';
            document.querySelector('#Braids').innerHTML = '';
            document.querySelector('#Corrugation').innerHTML = '';
            get_corrugation();
        });
    }

    let select_corrugation = document.querySelector('#Corrugation');

    if (select_corrugation) {
        select_corrugation.addEventListener('change', get_image_part_of_product);
    }

    let select_lengths = document.querySelector('#LengthsHoses');

    if (select_lengths) {
        select_lengths.addEventListener('click', get_lengths);
    }

    let select_innerscreen = document.querySelector('#InnerScreen');

    if (select_innerscreen) {
        select_innerscreen.addEventListener('click', get_innerscreen);
    }

    let select_outershells = document.querySelector('#OuterShells');

    if (select_outershells) {
        select_outershells.addEventListener('click', get_outershells);
    }

    let select_braids = document.querySelector('#Braids');

    if (select_braids) {
        select_braids.addEventListener('click', get_braids);
    }

    let select_materials1 = document.querySelector('#Materials1');

    if (select_materials1) {
        select_materials1.addEventListener('click', get_materials);
        select_materials1.addEventListener('change', () => {
            document.querySelector('#TypeFitting1').innerHTML = '';
            clear_image('#img1');
        });
    }

    let select_materials2 = document.querySelector('#Materials2');

    if (select_materials2) {
        select_materials2.addEventListener('click', get_materials);
        select_materials2.addEventListener('change', () => {
            document.querySelector('#TypeFitting2').innerHTML = '';
            clear_image('#img2');
        });
    }

    let select_materialsA1 = document.querySelector('#MaterialsA1');

    if (select_materialsA1) {
        select_materialsA1.addEventListener('click', get_materials);
        select_materialsA1.addEventListener('change', () => {
            document.querySelector('#TypeFittingA1').innerHTML = '';
            clear_image('#imgA1');
        });
    }

    let select_materialsA2 = document.querySelector('#MaterialsA2');

    if (select_materialsA2) {
        select_materialsA2.addEventListener('click', get_materials);
        select_materialsA2.addEventListener('change', () => {
            document.querySelector('#TypeFittingA2').innerHTML = '';
            clear_image('#imgA2');
        });
    }

    let select_types_fittings1 = document.querySelector('#TypeFitting1');

    if (select_types_fittings1) {
        select_types_fittings1.addEventListener('click', get_types_fittings1);
        select_types_fittings1.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittings2 = document.querySelector('#TypeFitting2');

    if (select_types_fittings2) {
        select_types_fittings2.addEventListener('click', get_types_fittings2);
        select_types_fittings2.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittingsA1 = document.querySelector('#TypeFittingA1');

    if (select_types_fittingsA1) {
        select_types_fittingsA1.addEventListener('click', get_types_fittingsA1);
        select_types_fittingsA1.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittingsA2 = document.querySelector('#TypeFittingA2');

    if (select_types_fittingsA2) {
        select_types_fittingsA2.addEventListener('click', get_types_fittingsA2);
        select_types_fittingsA2.addEventListener('change', get_image_part_of_product);
    }

    let button_copy_K1 = document.querySelector('#CopyA1');

    if (button_copy_K1) {
        button_copy_K1.addEventListener('click', copy_from_K1);
    }

    let button_clear_form = document.querySelector('#ClearForm');

    if (button_clear_form) {
        button_clear_form.addEventListener('click', clear_form);
    }

    let button_order = document.querySelector('#Order');

    if (button_order) {
        button_order.addEventListener('click', create_product);
    }
}

async function get_types() {
    const id = this.getAttribute('id');
    let select_type = document.querySelector(`#${id}`);

    if (select_type.childNodes.length > 0) {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListProductType',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP types: ${response.status}`);
        return;
    }

    let types = await response.json();

    if (Object.keys(types).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let type of types.list) {
        let option = document.createElement('option');
        option.value = type.Code;
        option.textContent = type.Value;
        select_type.appendChild(option);
    }
}

async function get_groups_and_fittings() {
    const id = this.getAttribute('id');
    let select_groups_fittings = document.querySelector(`#${id}`);

    if (select_groups_fittings.childNodes.length > 1) {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP groups_and_fittings ${id}: ` + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_groups_fittings.appendChild(option);
    }
}

async function get_diameters() {
    let select_diameters = document.querySelector('#Diameters');

    if (select_diameters.childNodes.length > 1) {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListDiameters',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

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
        return;
    }

    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListPressureHoseStartSelection&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': request1C,
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP pressures: ${response.status}`);
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
}

async function get_corrugation() {
    let select_corrugation = document.querySelector('#Corrugation');

    if (select_corrugation.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters').value;
    let pressure = document.querySelector('#Pressures').value;
    let request1C = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getCorrugation';

    if (diameter && pressure) {
        request1C += `&diameter=${diameter}&pressure=${pressure}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP pressures: ${response.status}`);
        return;
    }

    let corrugation = await response.json();

    if (Object.keys(corrugation).length === 0) {
        console.log('Пустой ответ в #Corrugation');
        return;
    }

    if (corrugation.Code === '0') {
        return;
    }

    let option = document.createElement('option');
    option.value = corrugation.Code;
    option.textContent = corrugation.Value;
    select_corrugation.appendChild(option);
    select_corrugation.dispatchEvent(new Event('change'));
}

async function get_innerscreen() {
    let select_innerscreens = document.querySelector('#InnerScreen');

    if (select_innerscreens.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListInnerScreenStartSelection&diameter=${diameter.value}`;
    }
    else {
        return;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

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

async function get_outershells() {
    const id = this.getAttribute('id');
    let select_outershells = document.querySelector(`#${id}`);

    if (select_outershells.childNodes.length > 1) {
        return;
    }

    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListOuterShellStartSelection&diameter=${diameter.value}`;
    }
    else {
        return;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let outershells = await response.json();

    if (Object.keys(outershells).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let outershell of outershells.list) {
        let option = document.createElement('option');
        option.value = outershell.Code;
        option.textContent = outershell.Value;
        select_outershells.appendChild(option);
    }
}

async function get_braid() {
    const id = this.getAttribute('id');
    let select_braid = document.querySelector(`#${id}`);

    if (select_braid.childNodes.length > 0) {
        return;
    }

    let diameter = document.querySelector('#Diameters');
    let pressure = document.querySelector('#Pressures');
    let request1C = '';

    if (diameter && diameter.value && pressure && pressure.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListBraidStartSelection&pressure=${pressure.value}&diameter=${diameter.value}`;
    }
    else {
        return;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let braid = await response.json();

    if (Object.keys(braid).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    let option = document.createElement('option');
    option.value = braid.Code;
    option.textContent = braid.Value;
    select_braid.appendChild(option);
}

async function get_braids() {
    const id = this.getAttribute('id');
    let select_braids = document.querySelector(`#${id}`);

    if (select_braids.childNodes.length > 0) {
        return;
    }

    let diameter = document.querySelector('#Diameters');
    let pressure = document.querySelector('#Pressures');
    let request1C = '';

    if (diameter && diameter.value && pressure && pressure.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListBraidStartSelection&pressure=${pressure.value}&diameter=${diameter.value}`;
    }
    else {
        return;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let braids = await response.json();

    if (Object.keys(braids).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let braid of braids.list) {
        let option = document.createElement('option');
        option.value = braid.Code;
        option.textContent = braid.Value;
        select_braids.appendChild(option);
    }
}

async function get_lengths() {
    let select_lengths = document.querySelector('#LengthsHoses');

    if (select_lengths.childNodes.length > 0) {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListLengthsHoses',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

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
    const id = this.getAttribute('id');
    let select_materials = document.querySelector(`#${id}`);

    if (select_materials.childNodes.length > 1) {
        return;
    }

    let optoins = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListMaterials',
        },
    };

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP materials: ' + response.status);
        return;
    }

    let materials = await response.json();

    if (Object.keys(materials).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let material of materials.list) {
        let option = document.createElement('option');
        option.value = material.Code;
        option.textContent = material.Value;
        select_materials.appendChild(option);
    }
}

async function get_types_fittings1() {
    const id = this.getAttribute('id');
    let select_type_fitting1 = document.querySelector(`#${id}`);

    if (select_type_fitting1.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittings1');
    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#Materials1');

    if (material_code && material_code.value) {
        request1C += `&material_code=${material_code.value}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP select_type_fitting1: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fitting1.appendChild(option);
    }
}

async function get_types_fittingsA1() {
    const id = this.getAttribute('id');
    let select_type_fittingA1 = document.querySelector(`#${id}`);

    if (select_type_fittingA1.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittingsA1');
    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#MaterialsA1');

    if (material_code && material_code.value) {
        request1C += `&material_code=${material_code.value}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP select_type_fittingA1: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fittingA1.appendChild(option);
    }
}

async function get_types_fittingsA2() {
    const id = this.getAttribute('id');
    let select_type_fittingA1 = document.querySelector(`#${id}`);

    if (select_type_fittingA1.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittingsA2');
    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#MaterialsA2');

    if (material_code && material_code.value) {
        request1C += `&material_code=${material_code.value}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP select_type_fittingA2: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fittingA1.appendChild(option);
    }
}

async function get_types_fittings2() {
    const id = this.getAttribute('id');
    let select_type_fitting2 = document.querySelector(`#${id}`);

    if (select_type_fitting2.childNodes.length > 1) {
        return;
    }

    let group_code = document.querySelector('#GroupsEndFittings2');
    let diameter = document.querySelector('#Diameters');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#Pressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#Materials2');

    if (material_code && material_code.value) {
        request1C += `&material_code=${material_code.value}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP select_type_fitting2: ' + response.status);
        return;
    }

    let fittings = await response.json();

    if (Object.keys(fittings).length === 0) {
        console.log(`Пустой ответ для ${id}`);
        return;
    }

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fitting2.appendChild(option);
    }
}

async function get_image_part_of_product() {
    const id = this.getAttribute('id');
    let position_image_code = 0;
    let get_image = 1;
    let diameter = document.querySelector('#Diameters').value;
    let typefitting_code = undefined;
    let group_product_code = undefined;
    let id_img = '';

    if (id === 'Corrugation') {
        position_image_code = 2;
        id_img = '#img0';
        typefitting_code = document.querySelector(`#${id}`).value;
    }
    else if (id === 'TypeFitting1') {
        position_image_code = 0;
        id_img = '#img1';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#GroupsEndFittings1').value;
    }
    else if (id === 'TypeFitting2') {
        position_image_code = 1;
        id_img = '#img2';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#GroupsEndFittings2').value;
    }
    else if (id === 'TypeFittingA1') {
        position_image_code = 1;
        id_img = '#imgA1';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#GroupsEndFittingsA1').value;
    }
    else if (id === 'TypeFittingA2') {
        position_image_code = 0;
        id_img = '#imgA2';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#GroupsEndFittingsA2').value;
    }
    else {
        return;
    }

    let img = document.querySelector(id_img);

    let request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getImagePartOfProduct&position_image_code=${position_image_code}`;

    if (diameter) {
        request1C += `&diameter=${diameter}`;
    }
    else {
        return;
    }

    if (group_product_code) {
        request1C += `&group_product_code=${group_product_code}`;
    }

    if (typefitting_code) {
        request1C += `&typefitting_code=${typefitting_code}`;
    }

    if (get_image) {
        request1C += `&get_image=${get_image}`;
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

    let response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log(`Ошибка HTTP get_image_part_of_product: ${response.status}`);
        return;
    }

    if (response.headers.get('Content-Disposition') === null) {
        let response_json = await response.json();

        if (id !== 'Corrugation') {
            img.setAttribute('src', '');
        }

        if (Object.keys(response_json).length === 0) {
            console.log(`Пустой ответ для ${position_image_code}`);
            return;
        }
    }
    else {
        let response_bytes = await response.blob();
        let img_url = URL.createObjectURL(response_bytes);
        img.setAttribute('src', img_url);
        URL.revokeObjectURL(img_url);
    }
}

function clear_image(id_img) {
    let img = document.querySelector(id_img);
    img.setAttribute('src', '');
}

function copy_from_K1() {
    document.querySelector('#GroupsEndFittingsA2').innerHTML = document.querySelector('#GroupsEndFittingsA1').innerHTML;
    document.querySelector('#GroupsEndFittingsA2').value = document.querySelector('#GroupsEndFittingsA1').value;
    document.querySelector('#MaterialsA2').innerHTML = document.querySelector('#MaterialsA1').innerHTML;
    document.querySelector('#MaterialsA2').value = document.querySelector('#MaterialsA1').value;
    document.querySelector('#TypeFittingA2').innerHTML = document.querySelector('#TypeFittingA1').innerHTML;
    document.querySelector('#TypeFittingA2').value = document.querySelector('#TypeFittingA1').value;
}

function clear_form() {
    document.querySelector('#Materials1').innerHTML = '';
    document.querySelector('#Materials2').innerHTML = '';
    document.querySelector('#TypeFitting1').innerHTML = '';
    clear_image('#img1');
    document.querySelector('#TypeFitting2').innerHTML = '';
    clear_image('#img2');
    document.querySelector('#MaterialsA1').innerHTML = '';
    document.querySelector('#MaterialsA2').innerHTML = '';
    document.querySelector('#TypeFittingA1').innerHTML = '';
    document.querySelector('#TypeFittingA2').innerHTML = '';
    document.querySelector('#InnerScreen').innerHTML = '';
    document.querySelector('#OuterShells').innerHTML = '';
    document.querySelector('#Braids').innerHTML = '';
}

async function create_product() {
    let data = {};
    let product_type_code = document.querySelector('#Types').value;
    let pressure = document.querySelector('#Pressures').value;
    let diameter = document.querySelector('#Diameters').value;
    let length = document.querySelector('#LengthsHoses').value;
    let corrugation_code = document.querySelector('#Corrugation').value;
    let braid_code = document.querySelector('#Braids').value;

    if (product_type_code && pressure && diameter && length && corrugation_code && braid_code) {
        data.product_type_code = product_type_code;
        data.pressure = pressure;
        data.diameter = diameter;
        data.length = length;
        data.corrugation_code = corrugation_code;
        data.braid_code = braid_code;
    }
    else {
        alert('Не заполнены обязательные поля: Тип изделия, Диаметр, Давление, Длина, Оплетка');
        return;
    }

    let innerscreen_code = document.querySelector('#InnerScreen').value;
    let outershells_code = document.querySelector('#OuterShells').value;
    let typefitting1_code = document.querySelector('#TypeFitting1').value;
    let typefitting2_code = document.querySelector('#TypeFitting2').value;
    let typefittingadd1_code = document.querySelector('#TypeFittingA1').value;
    let typefittingadd2_code = document.querySelector('#TypeFittingA2').value;

    data.innerscreen_code = innerscreen_code ? innerscreen_code : '0';
    data.outershells_code = outershells_code ? outershells_code : '0';
    data.typefitting1_code = typefitting1_code ? typefitting1_code : '0';
    data.typefitting2_code = typefitting2_code ? typefitting2_code : '0';
    data.typefittingadd1_code = typefittingadd1_code ? typefittingadd1_code : '0';
    data.typefittingadd2_code = typefittingadd2_code ? typefittingadd2_code : '0';

    let request1C = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=createProduct';

    let optoins = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': get_cookie('csrftoken'),
            'Request1C': request1C,
        },
        body: JSON.stringify(data),
    };

    const response = await fetch('/constructor_api/v1/proxy_request/', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP createProduct: ' + response.status);
        return;
    }

    let response_json = await response.json();
    // console.log(response_json);

}