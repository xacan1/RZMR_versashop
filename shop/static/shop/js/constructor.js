"use strict";


window.addEventListener('load', elements_listener());


async function elements_listener() {
    get_types();
    get_groups_and_fittings1();
    get_groups_and_fittings2();
    get_diameters();
    get_pressures();
    get_lengths();

    let select_type = document.querySelector('#type');

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
}

async function get_types() {
    let select_type = document.querySelector('#type');

    if (select_type.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListProductType', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP types: ' + response.status);
        return;
    }

    let types = await response.json();

    for (let type of types.list) {
        let option = document.createElement('option');
        option.value = type.Code;
        option.textContent = type.Value;
        select_type.appendChild(option);
    }
}


async function get_groups_and_fittings1() {
    let select_fittings = document.querySelector('#GroupsEndFittings1');

    if (select_fittings.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP fitting1: ' + response.status);
        return;
    }

    let fittings = await response.json();

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_fittings.appendChild(option);
    }
}

async function get_groups_and_fittings2() {
    let select_fittings = document.querySelector('#GroupsEndFittings2');

    if (select_fittings.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP fitting2: ' + response.status);
        return;
    }

    let fittings = await response.json();

    for (let fitting of fittings.list) {
        let option = document.createElement('option');
        option.value = fitting.Code;
        option.textContent = fitting.Value;
        select_fittings.appendChild(option);
    }
}

async function get_diameters() {
    let select_diameters = document.querySelector('#Diameters');

    if (select_diameters.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListDiameters', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP diameters: ' + response.status);
        return;
    }

    let diameters = await response.json();

    for (let diameter of diameters.list) {
        let option = document.createElement('option');
        option.value = diameter.Code;
        option.textContent = diameter.Value;
        select_diameters.appendChild(option);
    }
}

async function get_pressures() {
    let select_pressures = document.querySelector('#Pressures');

    if (select_pressures.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListPressures', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let pressures = await response.json();

    for (let pressure of pressures.list) {
        let option = document.createElement('option');
        option.value = pressure.Code;
        option.textContent = pressure.Value;
        select_pressures.appendChild(option);
    }
}

async function get_lengths() {
    let select_lengths = document.querySelector('#LengthsHoses');

    if (select_lengths.childNodes.length > 1) {
        return;
    }

    let optoins = {
        methos: 'GET',
        headers: { 'Content-Type': 'text/plain' },
    }

    let response = await fetch('http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListLengthsHoses', optoins);

    if (!response.ok && response.status != 401) {
        console.log('Ошибка HTTP pressures: ' + response.status);
        return;
    }

    let lengths = await response.json();

    for (let length of lengths.list) {
        let option = document.createElement('option');
        option.value = length.Code;
        option.textContent = length.Value;
        select_lengths.appendChild(option);
    }
}