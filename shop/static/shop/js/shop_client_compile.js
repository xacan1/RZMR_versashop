'use strict';const g=new Intl.NumberFormat("ru-RU",{minimumFractionDigits:2,maximumFractionDigits:2}),k=new Intl.NumberFormat("ru-RU",{minimumFractionDigits:0,maximumFractionDigits:0});window.addEventListener("load",l());window.addEventListener("load",m());window.addEventListener("load",n());
async function n(){var a=document.getElementById("selectSorting");a&&a.addEventListener("change",p);(a=document.getElementById("successAddProductToCartModal"))&&a.addEventListener("show.bs.modal",function(d){q(d)});a=document.getElementsByClassName("form-check-input");for(var b of a)b.addEventListener("click",function(){r();let d=this.getAttribute("id");document.querySelector(`[data-shop-button-id="${d}"]`).removeAttribute("hidden")});b=document.getElementsByClassName("shop-popup-button");for(var c of b)c.addEventListener("click",
r);(c=document.querySelector(".cart-button\x3e.btn"))&&c.addEventListener("click",function(){v(this)});(c=document.querySelector(".favorite-button\x3e.btn"))&&c.addEventListener("click",function(){w(this)});(c=document.querySelector(".delete-favorite-button"))&&c.addEventListener("click",function(){x(this)})}function y(){let a=document.cookie.match(new RegExp("(?:^|; )"+"csrftoken".replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,"\\$1")+"\x3d([^;]*)"));return a?decodeURIComponent(a[1]):void 0}
async function z(){let a={g:0,amount:0,j:[]};var b={method:"GET",headers:{"Content-Type":"application/json;charset\x3dutf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":y()},credentials:"same-origin"};b=await fetch("/api/v1/get_cart_info/",b);return b.ok||401==b.status?401==b.status?a:a=await b.json():(console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP: "+b.status),a)}
function A(){var a=document.getElementById("shop-cart-header").querySelectorAll(".shop-for-del");for(let b of a)b.remove();if(a=document.querySelector(".cart-items\x3e.shopping-item\x3e.bottom"))a.textContent=""}
async function l(){var a=document.querySelector("#shop-cart-header"),b=await z();A();var c=a.querySelector(".shopping-item\x3eul.shopping-list");a.querySelector("#shop-total-quantity-cart").textContent="\u0422\u043e\u0432\u0430\u0440\u043e\u0432: "+k.format(b.g);for(var d of b.j){let h=document.createElement("li");h.className="shop-for-del";h.setAttribute("data-shop-product_cart-pk",d.id);let t;t=d.product.name.includes("\u0420\u0413\u041c ")?"https://rzmr.ru/static/rzmr/img/metallhoses.jpg":d.product.i?
d.product.i:"https://rzmr.ru/static/shop/img/no_image.jpg";let u="/shop/product-details/"+d.product.l;h.innerHTML=`<div>\
            <a href="javascript:void(0)" onclick="delete_cart_product(this);" class="remove" title="\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440">\
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">\
                <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>\
            </svg>\
            </a>\
            <div class="cart-img-head">\
                <a class="cart-img" href="${u}"><img class="img-header-cart" src="${t}" alt="#"></a>\
            </div>\
        </div>\
        <div class="content">\
            <div><a href="${u}">${d.product.name}</a></div>\
            <div class="quantity">${k.format(d.g)}x - <span class="amount">${g.format(d.amount)}</span></div>\
        </div>`;c.append(h)}a.querySelector(".shopping-item\x3e.bottom").innerHTML=`<div class="bottom">\
        <div class="total">\
            <span>\u0418\u0442\u043e\u0433\u043e</span>\
            <span class="total-amount">${g.format(b.amount)}</span>\
        </div>\
        <div class="button" hidden=false>\
            <a href="${location.hostname}/shop/checkout" class="btn animate">\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437</a>\
        </div>\
    </div>`;b.j||a.querySelector(".shopping-item\x3e.bottom\x3e.button").setAttribute("hidden",!0);a.querySelector("#shop-total-items").textContent=k.format(b.g);if(document.querySelector("#shop-cart")){a=document.querySelector("#shop-cart");c=document.getElementById("shop-cart").querySelectorAll(".shop-for-del");for(var f of c)f.remove();f=a.querySelector("#shop-cart\x3e.cart-list-head");0<b.g?(document.querySelector("#empty-cart").textContent="",a=document.createElement("div"),a.className="cart-list-title shop-for-del",
a.innerHTML=`<div class="row py-2">\
            <div class="col-lg-1 col-md-1 col-12">\
            </div>\
            <div class="col-lg-4 col-md-3 col-12">\
                <span>\u0422\u043e\u0432\u0430\u0440</span>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <span>\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e</span>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <span>\u0421\u0443\u043c\u043c\u0430</span>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12" ${0<b.h?"":"hidden"}>\
                <span>\u0421\u043a\u0438\u0434\u043a\u0430</span>\
            </div>\
            <div class="col-lg-1 col-md-2 col-12">\
                <span>\u0423\u0434\u0430\u043b\u0438\u0442\u044c</span>\
            </div>\
        </div>`,f.append(a)):document.querySelector("#empty-cart").textContent="\u041a\u043e\u0440\u0437\u0438\u043d\u0430 \u043f\u0443\u0441\u0442\u0430, \u043d\u043e \u044d\u0442\u043e \u043b\u0435\u0433\u043a\u043e \u0438\u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c ;)";for(var e of b.j)a="/shop/product-details/"+e.product.l,c=document.createElement("div"),d=e.product.name.includes("\u0420\u0413\u041c ")?"https://rzmr.ru/static/rzmr/img/metallhoses.jpg":e.product.i?e.product.i:"https://rzmr.ru/static/shop/img/no_image.jpg",
c.className="cart-single-list shop-for-del",c.innerHTML=`<div class="row align-items-center shop-row-cart-order" data-shop-product_cart-pk="${e.id}" data-shop-product-pk="${e.product.id}" data-shop-price="${e.m}">\
            <div class="col-lg-1 col-md-1 col-12">\
                <div class="p-1">\
                    <a href="${a}"><img class="img-cart-order" src="${d}" alt="#"></a>\
                </div>\
            </div>\
            <div class="col-lg-4 col-md-3 col-12">\
                <p class="product-name fw-bold">\
                    <a href="${a}">\
                    ${e.product.name}</a>\
                </p>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <div class="count-input">\
                    <input class="form-control" type="number" name="quantity" step="1" min="1" value="${k.format(e.g)}" onchange="after_change_quantity(this);">\
                </div>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <p class="shop-amount fs-6">${g.format(e.amount)}</p>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12" ${0<b.h?"":"hidden"}>\
                <p class="shop-discount">${g.format(e.h)}</p>\
            </div>\
            <div class="col-lg-1 col-md-2 col-12">
                <button class="btn" onclick="delete_cart_product(this);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16">
                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
                    </svg>
                </button>
            </div>
        </div>`,f.append(c);e=document.querySelector("#shop-total-amount-cart");f=document.createElement("div");f.className="shop-for-del";f.innerHTML=`<ul>\
        <li>\u0421\u0443\u043c\u043c\u0430 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0432 \u043a\u043e\u0440\u0437\u0438\u043d\u0435<span>${g.format(b.amount)}</span></li>\
        <li>\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430<span>\u0411\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e</span></li>\
        <li ${0<b.h?"":"hidden"}>\u0421\u043a\u0438\u0434\u043a\u0430<span>${g.format(b.h)}</span></li>\
        <li class="last">\u041a \u043e\u043f\u043b\u0430\u0442\u0435<span>${g.format(b.amount)}</span></li>\
    </ul>`;e.append(f);if(0==b.g){b=document.querySelectorAll(".shop-for-hidden");for(let h of b)h.setAttribute("hidden","")}}}
async function q(a){a=await v(a.relatedTarget);let b=document.getElementById("shopCheckSuccess"),c=document.getElementById("shop-check-part-1"),d=document.getElementById("shop-check-part-2"),f=document.getElementById("shopCheckDecliane"),e=document.querySelector(".modal-body\x3eh6");"error"in a?(e.textContent="\u0422\u043e\u0432\u0430\u0440 \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u0441\u044f \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435",b.className="",c.className="",d.className="",f.className=
"shop-check-decline"):(e.textContent="\u0422\u043e\u0432\u0430\u0440 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d \u0432 \u043a\u043e\u0440\u0437\u0438\u043d\u0443",b.className="shop-check-success",c.className="shop-check-sign-success",d.className="shop-check-sign-success",f.className="")}
async function v(a){a={o:a.getAttribute("data-shop-product-pk"),g:1};a={method:"POST",headers:{"Content-Type":"application/json;charset\x3dutf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":y()},credentials:"same-origin",body:JSON.stringify(a)};a=await fetch("/api/v1/update_product_to_cart/",a);if(a.ok)return a=await a.json(),A(),await l(),a;console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP add_product_to_cart: "+a.status)}
async function B(){let a={count:0,products:[]};var b={method:"GET",headers:{"Content-Type":"application/json;charset\x3dutf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":y()},credentials:"same-origin"};b=await fetch("/api/v1/get_favorite_products_info/",b);return b.ok||401==b.status?a=await b.json():(console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP get_wishlist_info: "+b.status),a)}
async function m(){let a=document.querySelector("#shop-total-wishlist");if(a){var b=await B();a.textContent=k.format(b.count)}}
async function w(a){a={product:a.getAttribute("data-shop-product-pk")};a={method:"POST",headers:{"Content-Type":"application/json;charset\x3dutf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":y()},credentials:"same-origin",body:JSON.stringify(a)};a=await fetch("/api/v1/add_favorite_product/",a);a.ok?m():console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP add_favorite_product: "+a.status)}
async function x(a){a=a.getAttribute("data-shop-favorite_product-pk");var b={method:"DELETE",headers:{"Content-Type":"application/json;charset\x3dutf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":y()},credentials:"same-origin"};b=await fetch(`/api/v1/products/favorites/${a}/`,b);b.ok?((a=document.querySelector(`div[data-shop-favorite_product-pk="${a}"]`))&&a.remove(),m()):console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP /api/v1/products/favorites/: "+b.status)}
async function p(){var a=document.querySelector("input.form-range");if(a){a="?"+a.name+"\x3d"+a.value;var b=document.querySelectorAll("input.form-check-input[checked]");for(var c of b)a+="\x26"+c.name+"\x3d"+c.value;c=document.getElementById("selectSorting");a+="\x26sorting\x3d"+c.value;location.href=a}else console.log("\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430!")}
function r(){let a=document.getElementsByClassName("shop-popup-button");for(let b of a)b.setAttribute("hidden","")};
