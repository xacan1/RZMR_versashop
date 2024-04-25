"use strict";

window.addEventListener('load', elements_listener());

function elements_listener() {
    let small_images = document.querySelectorAll('.resize-img');

    for (let image of small_images) {
        image.addEventListener('click', change_big_image);
    }
}

function change_big_image() {
    let small_src = this.getAttribute('src');
    let big_img = document.querySelector('#bigImage');
    big_img.setAttribute('src', small_src);
}