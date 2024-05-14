"use strict";

window.addEventListener('load', elements_listener());


function get_cookie(name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function elements_listener() {
    let corrugation = document.querySelector('#constructorCorrugation');
    set_empty_corrugation(corrugation);

    let select_type = document.querySelector('#constructorTypes');

    if (select_type) {
        select_type.addEventListener('click', get_types);
    }

    let select_fittings1 = document.querySelector('#constructorGroupsEndFittings1');

    if (select_fittings1) {
        select_fittings1.addEventListener('click', get_groups_and_fittings);
        select_fittings1.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFitting1');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImg1');
            let type_fittingA = document.querySelector('#constructorTypeFittingA1');
            set_empty_typefitting(type_fittingA);
            clear_image('#constructorImgA1');
        });
    }

    let select_fittings2 = document.querySelector('#constructorGroupsEndFittings2');

    if (select_fittings2) {
        select_fittings2.addEventListener('click', get_groups_and_fittings);
        select_fittings2.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFitting2');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImg2');
            let type_fittingA = document.querySelector('#constructorTypeFittingA2');
            set_empty_typefitting(type_fittingA);
            clear_image('#constructorImgA2');
        });
    }

    let select_fittingsA1 = document.querySelector('#constructorGroupsEndFittingsA1');

    if (select_fittingsA1) {
        select_fittingsA1.addEventListener('click', get_groups_and_fittings);
        select_fittingsA1.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFittingA1');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImgA1');
        });
    }

    let select_fittingsA2 = document.querySelector('#constructorGroupsEndFittingsA2');

    if (select_fittingsA2) {
        select_fittingsA2.addEventListener('click', get_groups_and_fittings);
        select_fittingsA2.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFittingA2');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImgA2');
        });
    }

    let select_diameters = document.querySelector('#constructorDiameters');

    if (select_diameters) {
        select_diameters.addEventListener('click', get_diameters);
        select_diameters.addEventListener('change', () => {
            set_empty_typefitting(document.querySelector('#constructorTypeFitting1'));
            clear_image('#constructorImg1');
            set_empty_typefitting(document.querySelector('#constructorTypeFitting2'));
            clear_image('#constructorImg2');
            set_empty_pressures(document.querySelector('#constructorPressures'));
            set_empty_innerscreen(document.querySelector('#constructorInnerScreen'));
            set_empty_braids(document.querySelector('#constructorBraid'));
            set_empty_corrugation(document.querySelector('#constructorCorrugation'));
            get_corrugation();
            get_braid();
        });
    }

    let select_pressures = document.querySelector('#constructorPressures');

    if (select_pressures) {
        select_pressures.addEventListener('click', get_pressures);
        select_pressures.addEventListener('change', () => {
            set_empty_typefitting(document.querySelector('#constructorTypeFitting1'));
            clear_image('#constructorImg1');
            set_empty_typefitting(document.querySelector('#constructorTypeFitting2'));
            clear_image('#constructorImg2');
            set_empty_typefitting(document.querySelector('#constructorTypeFittingA1'));
            set_empty_typefitting(document.querySelector('#constructorTypeFittingA2'));
            set_empty_braids(document.querySelector('#constructorBraid'));
            set_empty_corrugation(document.querySelector('#constructorCorrugation'));
            get_corrugation();
            get_braid();
        });
    }

    let select_corrugation = document.querySelector('#constructorCorrugation');

    if (select_corrugation) {
        select_corrugation.addEventListener('change', get_image_part_of_product);
    }

    let select_lengths = document.querySelector('#constructorLengthsHoses');

    if (select_lengths) {
        select_lengths.addEventListener('click', get_lengths);
    }

    let select_innerscreen = document.querySelector('#constructorInnerScreen');

    if (select_innerscreen) {
        select_innerscreen.addEventListener('click', get_innerscreen);
    }

    let select_outershells = document.querySelector('#constructorOuterShells');

    if (select_outershells) {
        select_outershells.addEventListener('click', get_outershells);
    }

    let select_braids = document.querySelector('#constructorBraid');

    if (select_braids) {
        select_braids.addEventListener('click', get_braid);
    }

    let select_materials1 = document.querySelector('#constructorMaterials1');

    if (select_materials1) {
        select_materials1.addEventListener('click', get_materials);
        select_materials1.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFitting1');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImg1');
        });
    }

    let select_materials2 = document.querySelector('#constructorMaterials2');

    if (select_materials2) {
        select_materials2.addEventListener('click', get_materials);
        select_materials2.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFitting2');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImg2');
        });
    }

    let select_materialsA1 = document.querySelector('#constructorMaterialsA1');

    if (select_materialsA1) {
        select_materialsA1.addEventListener('click', get_materials);
        select_materialsA1.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFittingA1');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImgA1');
        });
    }

    let select_materialsA2 = document.querySelector('#constructorMaterialsA2');

    if (select_materialsA2) {
        select_materialsA2.addEventListener('click', get_materials);
        select_materialsA2.addEventListener('change', () => {
            let type_fitting = document.querySelector('#constructorTypeFittingA2');
            set_empty_typefitting(type_fitting);
            clear_image('#constructorImgA2');
        });
    }

    let select_types_fittings1 = document.querySelector('#constructorTypeFitting1');

    if (select_types_fittings1) {
        select_types_fittings1.addEventListener('click', get_types_fittings1);
        select_types_fittings1.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittings2 = document.querySelector('#constructorTypeFitting2');

    if (select_types_fittings2) {
        select_types_fittings2.addEventListener('click', get_types_fittings2);
        select_types_fittings2.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittingsA1 = document.querySelector('#constructorTypeFittingA1');

    if (select_types_fittingsA1) {
        select_types_fittingsA1.addEventListener('click', get_types_fittingsA1);
        select_types_fittingsA1.addEventListener('change', get_image_part_of_product);
    }

    let select_types_fittingsA2 = document.querySelector('#constructorTypeFittingA2');

    if (select_types_fittingsA2) {
        select_types_fittingsA2.addEventListener('click', get_types_fittingsA2);
        select_types_fittingsA2.addEventListener('change', get_image_part_of_product);
    }

    let button_copy1 = document.querySelector('#constructorCopy1');

    if (button_copy1) {
        button_copy1.addEventListener('click', copy_from1);
    }

    let button_copyA1 = document.querySelector('#constructorCopyA1');

    if (button_copyA1) {
        button_copyA1.addEventListener('click', copy_fromA1);
    }

    let button_clear_form = document.querySelector('#constructorClearForm');

    if (button_clear_form) {
        button_clear_form.addEventListener('click', clear_form);
    }

    let button_order = document.querySelector('#constructorOrder');

    if (button_order) {
        button_order.addEventListener('click', create_product);
    }
}

function set_empty_pressures(pressures) {
    pressures.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Рабочее давление, PN(Бар) -';
    pressures.appendChild(option_empty);
}

function set_empty_braids(braids) {
    braids.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Оплетка -';
    braids.appendChild(option_empty);
}

function set_empty_outershells(outershells) {
    outershells.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Наружная оболочка -';
    outershells.appendChild(option_empty);
}

function set_empty_innerscreen(innerscreen) {
    innerscreen.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Внутренний экран -';
    innerscreen.appendChild(option_empty);
}

function set_empty_corrugation(corrugation) {
    corrugation.innerHTML = '';
    // let option_empty = document.createElement('option');
    // option_empty.value = '';
    // option_empty.textContent = '- Гофра -';
    // corrugation.appendChild(option_empty);
}

function set_empty_typefitting(type_fitting) {
    type_fitting.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Тип концевой арматуры -';
    type_fitting.appendChild(option_empty);
}

function set_empty_fittings(group_fitting) {
    group_fitting.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Группа концевой арматуры -';
    group_fitting.appendChild(option_empty);
}

function set_empty_materials(materials) {
    materials.innerHTML = '';
    let option_empty = document.createElement('option');
    option_empty.value = '';
    option_empty.textContent = '- Материал -';
    materials.appendChild(option_empty);
}

async function get_types() {
    const id = this.getAttribute('id');
    let select_type = document.querySelector(`#${id}`);

    if (select_type.childElementCount > 0) {
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

    if (select_groups_fittings.childElementCount > 1) {
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
    let select_diameters = document.querySelector('#constructorDiameters');

    if (select_diameters.childElementCount > 1) {
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
    let select_pressures = document.querySelector('#constructorPressures');

    // очистка всех зависимых полей при смене давления
    if (select_pressures.childElementCount > 1) {
        return;
    }

    let diameter = document.querySelector('#constructorDiameters');
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
    let select_corrugation = document.querySelector('#constructorCorrugation');

    if (select_corrugation.childElementCount > 0) {
        return;
    }

    let diameter = document.querySelector('#constructorDiameters').value;
    let pressure = document.querySelector('#constructorPressures').value;
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
        console.log('Пустой ответ в #constructorCorrugation');
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
    let select_innerscreens = document.querySelector('#constructorInnerScreen');

    if (select_innerscreens.childElementCount > 1) {
        return;
    }

    let diameter = document.querySelector('#constructorDiameters');
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

    if (select_outershells.childElementCount > 1) {
        return;
    }

    let diameter = document.querySelector('#constructorDiameters');
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
    let select_braids = document.querySelector('#constructorBraid');

    if (select_braids.childElementCount > 1) {
        return;
    }

    let diameter = document.querySelector('#constructorDiameters');
    let pressure = document.querySelector('#constructorPressures');
    let request1C = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getBraid';

    if (diameter && diameter.value && pressure && pressure.value) {
        request1C += `&diameter=${diameter.value}&pressure=${pressure.value}`;
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

    if (braid.Code === '0') {
        return;
    }

    let option = document.createElement('option');
    option.value = braid.Code;
    option.textContent = braid.Value;
    select_braids.appendChild(option);
    select_braids.value = option.value;
    select_braids.dispatchEvent(new Event('change'));
}

async function get_lengths() {
    let select_lengths = document.querySelector('#constructorLengthsHoses');

    if (select_lengths.childElementCount > 1) {
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

    if (select_materials.childElementCount > 1) {
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

    if (select_type_fitting1.childElementCount > 1) {
        return;
    }

    let group_code = document.querySelector('#constructorGroupsEndFittings1');
    let diameter = document.querySelector('#constructorDiameters');
    let pressure = document.querySelector('#constructorPressures');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value && pressure && pressure.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}&pressure=${pressure.value}`;
    }
    else {
        return;
    }

    let material_code = document.querySelector('#constructorMaterials1');

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

    set_empty_typefitting(select_type_fitting1);

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

    if (select_type_fittingA1.childElementCount > 1) {
        return;
    }

    let group_code = document.querySelector('#constructorGroupsEndFittingsA1');
    let diameter = document.querySelector('#constructorDiameters');
    let type_fitting1 = document.querySelector('#constructorTypeFitting1');
    let request1C = '';

    if (!type_fitting1.value) {
        alert('Сначала нужно выбрать левую концевую арматуру');
        return;
    }

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#constructorPressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#constructorMaterialsA1');

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

    set_empty_typefitting(select_type_fittingA1);

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fittingA1.appendChild(option);
    }
}

async function get_types_fittingsA2() {
    const id = this.getAttribute('id');
    let select_type_fittingA2 = document.querySelector(`#${id}`);

    if (select_type_fittingA2.childElementCount > 1) {
        return;
    }

    let group_code = document.querySelector('#constructorGroupsEndFittingsA2');
    let diameter = document.querySelector('#constructorDiameters');
    let type_fitting2 = document.querySelector('#constructorTypeFitting1');
    let request1C = '';

    if (!type_fitting2.value) {
        alert('Сначала нужно выбрать правую концевую арматуру');
        return;
    }

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#constructorPressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#constructorMaterialsA2');

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

    set_empty_typefitting(select_type_fittingA2);

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_type_fittingA2.appendChild(option);
    }
}

async function get_types_fittings2() {
    const id = this.getAttribute('id');
    let select_type_fitting2 = document.querySelector(`#${id}`);

    if (select_type_fitting2.childElementCount > 1) {
        return;
    }

    let group_code = document.querySelector('#constructorGroupsEndFittings2');
    let diameter = document.querySelector('#constructorDiameters');
    let request1C = '';

    if (group_code && group_code.value && diameter && diameter.value) {
        request1C = `http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListTypeFittingStartSelection&group_code=${group_code.value}&diameter=${diameter.value}`;
    }
    else {
        return;
    }

    let pressure = document.querySelector('#constructorPressures');

    if (pressure && pressure.value) {
        request1C += `&pressure=${pressure.value}`;
    }

    let material_code = document.querySelector('#constructorMaterials2');

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

    set_empty_typefitting(select_type_fitting2);

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
    let diameter = document.querySelector('#constructorDiameters').value;
    let typefitting_code = undefined;
    let group_product_code = undefined;
    let id_img = '';

    if (id === 'constructorCorrugation') {
        position_image_code = 2;
        id_img = '#constructorImg0';
        typefitting_code = document.querySelector(`#${id}`).value;
    }
    else if (id === 'constructorTypeFitting1') {
        position_image_code = 0;
        id_img = '#constructorImg1';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#constructorGroupsEndFittings1').value;
    }
    else if (id === 'constructorTypeFitting2') {
        position_image_code = 1;
        id_img = '#constructorImg2';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#constructorGroupsEndFittings2').value;
    }
    else if (id === 'constructorTypeFittingA1') {
        position_image_code = 1;
        id_img = '#constructorImgA1';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#constructorGroupsEndFittingsA1').value;
    }
    else if (id === 'constructorTypeFittingA2') {
        position_image_code = 0;
        id_img = '#constructorImgA2';
        typefitting_code = document.querySelector(`#${id}`).value;
        group_product_code = document.querySelector('#constructorGroupsEndFittingsA2').value;
    }
    else {
        return;
    }

    if (!typefitting_code) {
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

        if (id !== 'constructorCorrugation') {
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
        img.addEventListener('load', (event) => { URL.revokeObjectURL(img_url); }, { once: true, });
    }
}

function clear_image(id_img) {
    let img = document.querySelector(id_img);
    img.setAttribute('src', '');
}

function copy_from1() {
    let select_fittings2 = document.querySelector('#constructorGroupsEndFittings2');
    select_fittings2.innerHTML = document.querySelector('#constructorGroupsEndFittings1').innerHTML;
    select_fittings2.value = document.querySelector('#constructorGroupsEndFittings1').value;

    let select_materials2 = document.querySelector('#constructorMaterials2');
    select_materials2.innerHTML = document.querySelector('#constructorMaterials1').innerHTML;
    select_materials2.value = document.querySelector('#constructorMaterials1').value;

    let type_fitting2 = document.querySelector('#constructorTypeFitting2');
    type_fitting2.innerHTML = document.querySelector('#constructorTypeFitting1').innerHTML;
    type_fitting2.value = document.querySelector('#constructorTypeFitting1').value;
    type_fitting2.dispatchEvent(new Event('change'));
}

function copy_fromA1() {
    let select_fittingsA2 = document.querySelector('#constructorGroupsEndFittingsA2');
    select_fittingsA2.innerHTML = document.querySelector('#constructorGroupsEndFittingsA1').innerHTML;
    select_fittingsA2.value = document.querySelector('#constructorGroupsEndFittingsA1').value;

    let select_materialsA2 = document.querySelector('#constructorMaterialsA2');
    select_materialsA2.innerHTML = document.querySelector('#constructorMaterialsA1').innerHTML;
    select_materialsA2.value = document.querySelector('#constructorMaterialsA1').value;

    let type_fittingA2 = document.querySelector('#constructorTypeFittingA2');
    type_fittingA2.innerHTML = document.querySelector('#constructorTypeFittingA1').innerHTML;
    type_fittingA2.value = document.querySelector('#constructorTypeFittingA1').value;
    type_fittingA2.dispatchEvent(new Event('change'));
}

function clear_form() {
    clear_image('#constructorImg1');
    clear_image('#constructorImg2');
    clear_image('#constructorImgA1');
    clear_image('#constructorImgA2');
    set_empty_innerscreen(document.querySelector('#constructorInnerScreen'));
    set_empty_outershells(document.querySelector('#constructorOuterShells'));
    set_empty_braids(document.querySelector('#constructorBraid'));
    set_empty_typefitting(document.querySelector('#constructorTypeFitting1'));
    set_empty_typefitting(document.querySelector('#constructorTypeFitting2'));
    set_empty_typefitting(document.querySelector('#constructorTypeFittingA1'));
    set_empty_typefitting(document.querySelector('#constructorTypeFittingA2'));
    set_empty_fittings(document.querySelector('#constructorGroupsEndFittings1'));
    set_empty_fittings(document.querySelector('#constructorGroupsEndFittings2'));
    set_empty_fittings(document.querySelector('#constructorGroupsEndFittingsA1'));
    set_empty_fittings(document.querySelector('#constructorGroupsEndFittingsA2'));
    set_empty_materials(document.querySelector('#constructorMaterials1'));
    set_empty_materials(document.querySelector('#constructorMaterials2'));
    set_empty_materials(document.querySelector('#constructorMaterialsA1'));
    set_empty_materials(document.querySelector('#constructorMaterialsA2'));
    set_empty_corrugation(document.querySelector('#constructorCorrugation'));
    set_empty_pressures(document.querySelector('#constructorPressures'));
}

async function create_product() {
    let data = {};
    let product_type_code = document.querySelector('#constructorTypes').value;
    let pressure = document.querySelector('#constructorPressures').value;
    let diameter = document.querySelector('#constructorDiameters').value;
    let length = document.querySelector('#constructorLengthsHoses').value;
    let corrugation_code = document.querySelector('#constructorCorrugation').value;
    let braid_code = document.querySelector('#constructorBraid').value;

    if (product_type_code) {
        data.product_type_code = product_type_code;
    }
    else {
        alert('Не заполнено обязательное поле: Тип изделия');
        return;
    }

    if (pressure) {
        data.pressure = pressure;
    }
    else {
        alert('Не заполнено обязательное поле: Давление');
        return;
    }

    if (diameter) {
        data.diameter = diameter;
    }
    else {
        alert('Не заполнено обязательное поле: Диаметр');
        return;
    }

    if (length) {
        data.length = length;
    }
    else {
        alert('Не заполнено обязательное поле: Длина');
        return;
    }

    if (braid_code) {
        data.braid_code = braid_code;
    }
    else {
        alert('Не заполнено обязательное поле: Оплетка');
        return;
    }

    if (corrugation_code) {
        data.corrugation_code = corrugation_code;
    }
    else {
        alert('Не заполнено обязательное поле: Гофра');
        return;
    }

    let innerscreen_code = document.querySelector('#constructorInnerScreen').value;
    let outershells_code = document.querySelector('#constructorOuterShells').value;
    let typefitting1_code = document.querySelector('#constructorTypeFitting1').value;
    let typefitting2_code = document.querySelector('#constructorTypeFitting2').value;
    let typefittingadd1_code = document.querySelector('#constructorTypeFittingA1').value;
    let typefittingadd2_code = document.querySelector('#constructorTypeFittingA2').value;

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

    // вспомогательная невидимая кнопка, нужна для вызова модального окна добавления товара в корзину,
    // так как я добавляю товар стандартно как везде в магазине через колбэк Bootstrap модального окна,
    // я просто присваиваю для товара PK на кнопке и имитирую щелчек по ней
    let button_order_modal = document.querySelector('#constructorOrderForModal');
    let product_name = document.querySelector('#constructorNameProduct');

    if (response_json.id === '0') {
        product_name.textContent = '';
        button_order_modal.removeAttribute('data-shop-product-pk');
        return;
    }

    product_name.textContent = response_json.Value;
    button_order_modal.setAttribute('data-shop-product-pk', response_json.id);

    if (button_order_modal.getAttribute('data-shop-product-pk')) {
        button_order_modal.dispatchEvent(new Event('click'));
    }
}
