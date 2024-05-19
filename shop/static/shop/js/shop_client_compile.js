'use strict';const formatter=new Intl.NumberFormat("ru-RU",{minimumFractionDigits:2,maximumFractionDigits:2}),formatter0=new Intl.NumberFormat("ru-RU",{minimumFractionDigits:0,maximumFractionDigits:0});window.addEventListener("load",update_cart_header());window.addEventListener("load",update_wishlist_header());window.addEventListener("load",elements_listener());
async function elements_listener(){var a=document.getElementById("selectSorting");a&&a.addEventListener("change",sort_products);(a=document.getElementById("successAddProductToCartModal"))&&a.addEventListener("show.bs.modal",function(e){handlerAddProductToCart(e)});a=document.getElementsByClassName("form-check-input");for(let e of a)e.addEventListener("click",function(){popup_button_show(this,e)});a=document.getElementsByClassName("shop-popup-button");for(var b of a)b.addEventListener("click",popup_button_hidden);
let d=document.querySelector(".cart-button>.btn");d&&d.addEventListener("click",function(){add_product_to_cart(this,d)});let c=document.querySelector(".favorite-button>.btn");c&&c.addEventListener("click",function(){add_favorite_product(this,c)});(b=document.querySelector(".delete-favorite-button"))&&b.addEventListener("click",function(){delete_favorite_product(this,c)})}
function getCookie(a){return(a=document.cookie.match(new RegExp("(?:^|; )"+a.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,"\\$1")+"=([^;]*)")))?decodeURIComponent(a[1]):void 0}
async function get_cart_info(){let a={quantity:0,amount:0,products:[]};var b={method:"GET",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin"};b=await fetch("/api/v1/get_cart_info/",b);return b.ok||401==b.status?401==b.status?a:a=await b.json():(console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP: "+b.status),a)}
function clear_cart_header(){var a=document.getElementById("shop-cart-header").querySelectorAll(".shop-for-del");for(let b of a)b.remove();if(a=document.querySelector(".cart-items>.shopping-item>.bottom"))a.textContent=""}
async function update_cart_header(){let a=document.querySelector("#shop-cart-header"),b=await get_cart_info();clear_cart_header();let d=a.querySelector(".shopping-item>ul.shopping-list");a.querySelector("#shop-total-quantity-cart").textContent="\u0422\u043e\u0432\u0430\u0440\u043e\u0432: "+formatter0.format(b.quantity);for(let c of b.products){let e=document.createElement("li");e.className="shop-for-del";e.setAttribute("data-shop-product_cart-pk",c.id);let f="/shop/product-details/"+c.product.slug;
e.innerHTML=`<div>\
            <a href="javascript:void(0)" onclick="delete_cart_product(this);" class="remove" title="\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440">\
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">\
                <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>\
            </svg>\
            </a>\
            <div class="cart-img-head">\
                <a class="cart-img" href="${f}"><img src="${c.product.photo?c.product.photo:"https://via.placeholder.com/220x200"}" alt="#"></a>\
            </div>\
        </div>\
        <div class="content">\
            <p><a href="${f}">${c.product.name}</a></p>\
            <p class="quantity">${formatter0.format(c.quantity)}x - <span class="amount">${formatter.format(c.amount)}</span></p>\
        </div>`;d.append(e)}a.querySelector(".shopping-item>.bottom").innerHTML=`<div class="bottom">\
        <div class="total">\
            <span>\u0418\u0442\u043e\u0433\u043e</span>\
            <span class="total-amount">${formatter.format(b.amount)}</span>\
        </div>\
        <div class="button" hidden=false>\
            <a href="${location.hostname}/shop/checkout" class="btn animate">\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437</a>\
        </div>\
    </div>`;b.products||a.querySelector(".shopping-item>.bottom>.button").setAttribute("hidden",!0);a.querySelector("#shop-total-items").textContent=formatter0.format(b.quantity);document.querySelector("#shop-cart")&&update_cart(b)}
async function delete_cart_product(a){a=a.parentElement.parentElement.getAttribute("data-shop-product_cart-pk");let b={method:"DELETE",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin"};a=await fetch(`/api/v1/carts/products/${a}/`,b);a.ok?(clear_cart_header(),await update_cart_header()):console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP: "+a.status)}
function get_selected_warehouse(){let a=0;const b=document.querySelector('input[name="warehouse"]:checked');if(!b){let d=document.getElementsByClassName("warehouses")[0];if(d)return d.setAttribute("style","color: red"),a}return a=b.value}
async function handlerAddProductToCart(a){a=await add_product_to_cart(a.relatedTarget);let b=document.getElementById("shopCheckSuccess"),d=document.getElementById("shop-check-part-1"),c=document.getElementById("shop-check-part-2"),e=document.getElementById("shopCheckDecliane"),f=document.querySelector(".modal-body>h6");"error"in a?(f.textContent="\u0422\u043e\u0432\u0430\u0440 \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u0441\u044f \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435",b.className=
"",d.className="",c.className="",e.className="shop-check-decline"):(f.textContent="\u0422\u043e\u0432\u0430\u0440 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d \u0432 \u043a\u043e\u0440\u0437\u0438\u043d\u0443",b.className="shop-check-success",d.className="shop-check-sign-success",c.className="shop-check-sign-success",e.className="")}
async function add_product_to_cart(a){a={product_pk:a.getAttribute("data-shop-product-pk"),quantity:1};a={method:"POST",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin",body:JSON.stringify(a)};a=await fetch("/api/v1/update_product_to_cart/",a);if(a.ok)return a=await a.json(),clear_cart_header(),await update_cart_header(),a;console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP add_product_to_cart: "+
a.status)}function clear_cart(){let a=document.getElementById("shop-cart").querySelectorAll(".shop-for-del");for(let b of a)b.remove()}
async function after_change_quantity(a){a={product_pk:a.parentElement.parentElement.parentElement.getAttribute("data-shop-product-pk"),quantity:parseFloat(a.value),set_new_quantity:!0};a={method:"POST",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin",body:JSON.stringify(a)};a=await fetch("/api/v1/update_product_to_cart/",a);a.ok?(clear_cart_header(),await update_cart_header()):console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP after_change_quantity: "+
a.status)}function update_cart(a){var b=document.querySelector("#shop-cart");clear_cart();b=b.querySelector("#shop-cart>.cart-list-head");if(0<a.quantity){document.querySelector("#empty-cart").textContent="";var d=document.createElement("div");d.className="cart-list-title shop-for-del";d.innerHTML=`<div class="row py-2">\
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
            <div class="col-lg-2 col-md-2 col-12" ${0<a.discount?"":"hidden"}>\
                <span>\u0421\u043a\u0438\u0434\u043a\u0430</span>\
            </div>\
            <div class="col-lg-1 col-md-2 col-12">\
                <span>\u0423\u0434\u0430\u043b\u0438\u0442\u044c</span>\
            </div>\
        </div>`;b.append(d)}else document.querySelector("#empty-cart").textContent="\u041a\u043e\u0440\u0437\u0438\u043d\u0430 \u043f\u0443\u0441\u0442\u0430, \u043d\u043e \u044d\u0442\u043e \u043b\u0435\u0433\u043a\u043e \u0438\u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c ;)";for(var c of a.products){d="/shop/product-details/"+c.product.slug;let e=document.createElement("div");e.className="cart-single-list shop-for-del";e.innerHTML=`<div class="row align-items-center shop-row-cart-order" data-shop-product_cart-pk="${c.id}" data-shop-product-pk="${c.product.id}" data-shop-price="${c.price}">\
            <div class="col-lg-1 col-md-1 col-12">\
                <a href="${d}"><img src="${c.product.photo?c.product.photo:"https://via.placeholder.com/220x200"}" alt="#"></a>\
            </div>\
            <div class="col-lg-4 col-md-3 col-12">\
                <p class="product-name fw-bold">\
                    <a href="${d}">\
                    ${c.product.name}</a>\
                </p>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <div class="count-input">\
                    <input class="form-control" type="number" name="quantity" step="1" min="1" value="${formatter0.format(c.quantity)}" onchange="after_change_quantity(this);">\
                </div>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12">\
                <p class="shop-amount fs-6">${formatter.format(c.amount)}</p>\
            </div>\
            <div class="col-lg-2 col-md-2 col-12" ${0<a.discount?"":"hidden"}>\
                <p class="shop-discount">${formatter.format(c.discount)}</p>\
            </div>\
            <div class="col-lg-1 col-md-2 col-12">
                <button class="btn" onclick="delete_cart_product(this);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16">
                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
                    </svg>
                </button>
            </div>
        </div>`;b.append(e)}c=document.querySelector("#shop-total-amount-cart");b=document.createElement("div");b.className="shop-for-del";b.innerHTML=`<ul>\
        <li>\u0421\u0443\u043c\u043c\u0430 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0432 \u043a\u043e\u0440\u0437\u0438\u043d\u0435<span>${formatter.format(a.amount)}</span></li>\
        <li>\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430<span>\u0411\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e</span></li>\
        <li ${0<a.discount?"":"hidden"}>\u0421\u043a\u0438\u0434\u043a\u0430<span>${formatter.format(a.discount)}</span></li>\
        <li class="last">\u041a \u043e\u043f\u043b\u0430\u0442\u0435<span>${formatter.format(a.amount)}</span></li>\
    </ul>`;c.append(b);if(0==a.quantity){a=document.querySelectorAll(".shop-for-hidden");for(let e of a)e.setAttribute("hidden","")}}
async function get_wishlist_info(){let a={count:0,products:[]};var b={method:"GET",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin"};b=await fetch("/api/v1/get_favorite_products_info/",b);return b.ok||401==b.status?a=await b.json():(console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP get_wishlist_info: "+b.status),a)}
async function update_wishlist_header(){let a=document.querySelector("#shop-total-wishlist");if(a){var b=await get_wishlist_info();a.textContent=formatter0.format(b.count)}}
async function add_favorite_product(a){a={product:a.getAttribute("data-shop-product-pk")};a={method:"POST",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin",body:JSON.stringify(a)};a=await fetch("/api/v1/add_favorite_product/",a);a.ok?update_wishlist_header():console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP add_favorite_product: "+a.status)}
async function delete_favorite_product(a){a=a.getAttribute("data-shop-favorite_product-pk");var b={method:"DELETE",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin"};b=await fetch(`/api/v1/products/favorites/${a}/`,b);b.ok?((a=document.querySelector(`div[data-shop-favorite_product-pk="${a}"]`))&&a.remove(),update_wishlist_header()):console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP /api/v1/products/favorites/: "+
b.status)}async function cancel_order(a){a=a.getAttribute("data-shop-order-pk");var b={method:"PATCH",headers:{"Content-Type":"application/json;charset=utf-8","X-Requested-With":"XMLHttpRequest","X-CSRFToken":getCookie("csrftoken")},credentials:"same-origin",body:JSON.stringify({canceled:!0})};b=await fetch(`/api/v1/orders/${a}/`,b);b.ok||console.log("\u041e\u0448\u0438\u0431\u043a\u0430 HTTP "+`/api/v1/orders/${a}/ `+b.status)}
async function sort_products(){var a=document.querySelector("input.form-range");if(a){a="?"+a.name+"="+a.value;var b=document.querySelectorAll("input.form-check-input[checked]");for(var d of b)a+="&"+d.name+"="+d.value;d=document.getElementById("selectSorting");a+="&sorting="+d.value;location.href=a}else console.log("\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430!")}
function popup_button_show(a){popup_button_hidden();a=a.getAttribute("id");document.querySelector(`[data-shop-button-id="${a}"]`).removeAttribute("hidden")}function popup_button_hidden(){let a=document.getElementsByClassName("shop-popup-button");for(let b of a)b.setAttribute("hidden","")};