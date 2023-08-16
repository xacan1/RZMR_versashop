from django.urls import path
from shop.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about-us/', AboutAsView.as_view(), name='about-us'),
    path('cart/', CartView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('user-agreement/', UserAgreementView.as_view(), name='user-agreement'),
    path('purchase-returns/', PurchaseReturnsView.as_view(), name='purchase-returns'),
    path('product-list/<slug:category_slug>', CategoryProductListView.as_view(), name='product-list'),
    path('search/', SearchView.as_view(), name='search'),
    path('product-details/<slug:product_slug>', ProductDetailView.as_view(), name='product-details'),
    path('checkout/', AddOrderView.as_view(), name='checkout'),
    path('new-order-success/', AddOrderSuccessView.as_view(), name='new-order-success'),
    path('order/<int:order_pk>', OrderView.as_view(), name='order'),
    path('order-cancel-confirm/<int:order_pk>', OrderCancelConfirmView.as_view(), name='order-cancel-confirm'),
    path('order-cancel-complete/<int:order_pk>', OrderCancelCompleteView.as_view(), name='order-cancel-complete'),
]
