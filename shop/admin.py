from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from shop.models import *


TokenAdmin.raw_id_fields = ['user']


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('parent', 'name', 'photo', 'external_code',)
    list_display_links = ('name',)
    search_fields = ('name', 'external_code',)
    prepopulated_fields = {'slug': ('name',)}


class UnitMeasureAdmin(admin.ModelAdmin):
    model = UnitMeasure
    list_display = ('name', 'short_name',
                    'international_short_name', 'external_code',)
    list_display_links = ('name', 'short_name',)
    search_fields = ('name', 'short_name', 'international_short_name',)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'photo', 'category', 'unit_measure',
                    'is_service', 'is_published', 'external_code',)
    list_filter = ('category', 'is_published', 'is_service',)
    search_fields = ('name', 'external_code',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


class ImageProductAdmin(admin.ModelAdmin):
    model = ImageProduct
    list_display = ('product', 'photo', 'description', 'default',)
    list_filter = ('default',)
    search_fields = ('product__name', 'product__external_code',)
    list_editable = ('default',)


class FavoriteProductAdmin(admin.ModelAdmin):
    model = FavoriteProduct
    list_display = ('user', 'product', 'id_messenger',)
    list_display_links = ('user', 'product',)
    search_fields = ('user__email', 'product__name', 'id_messenger',)


class CurrencyAdmin(admin.ModelAdmin):
    model = Currency
    list_display = ('name', 'abbreviation', 'digital_code', 'sign', 'default',)
    list_display_links = ('name', 'abbreviation', 'digital_code', 'sign',)
    list_editable = ('default',)
    search_fields = ('name', 'digital_code',)


class PriceTypeAdmin(admin.ModelAdmin):
    model = PriceType
    list_display = ('name', 'external_code', 'default',)
    list_display_links = ('name',)
    list_editable = ('default',)
    search_fields = ('name', 'external_code',)


class PricesAdmin(admin.ModelAdmin):
    model = Prices
    list_display = ('product', 'price', 'date_update', 'discount_percentage',
                    'currency', 'price_type',)
    list_filter = ('date_update',)
    search_fields = ('product__name',)


class AttributeAdmin(admin.ModelAdmin):
    model = Attribute
    list_display = ('name', 'category', 'external_code',)
    search_fields = ('name', 'external_code', 'category__name',)


class AttributeValuesAdmin(admin.ModelAdmin):
    model = AttributeValues
    list_display = ('attribute', 'string_value',
                    'numeric_value', 'external_code',)
    search_fields = ('attribute__name', 'external_code',)


class AttributeProductValuesAdmin(admin.ModelAdmin):
    model = AttributeProductValues
    list_display = ('product', 'attribute', 'value',)
    search_fields = ('product__name', 'attribute__name',
                     'value__string_value',)
    autocomplete_fields = ('attribute',)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'attribute':
    #         kwargs['limit_choices_to'] = {'id': 1}
    #         print(db_field.name)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def formfield_for_dbfield(self, db_field, request, **kwargs):

    #     if db_field.name == 'attribute':
    #         qs = Attribute.objects.filter(pk=1)
    #         return forms.ModelChoiceField(queryset=qs, **kwargs)

    #     return super().formfield_for_dbfield(db_field, request, **kwargs)


class WarehouseAdmin(admin.ModelAdmin):
    model = Warehouse
    list_display = ('name', 'country', 'province',
                    'city', 'address', 'external_code',)
    search_fields = ('name', 'country', 'province',
                     'city', 'address', 'external_code',)


class StockProductsAdmin(admin.ModelAdmin):
    model = StockProducts
    list_display = ('product', 'stock', 'warehouse',)
    list_filter = ('warehouse',)
    search_fields = ('product__name',)


class CartProductAdmin(admin.ModelAdmin):
    model = CartProduct
    list_display = ('cart', 'order', 'product', 'quantity', 'price', 'discount',
                    'discount_percentage', 'amount', 'warehouse', 'phone', 'id_messenger',)
    list_display_links = ('cart', 'order',)
    search_fields = ('phone', 'id_messenger', 'amount',)


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('user', 'currency', 'sessionid', 'quantity', 'amount',
                    'discount', 'for_anonymous_user',)
    list_filter = ('for_anonymous_user',)
    search_fields = ('user__email',)


class ContractorAdmin(admin.ModelAdmin):
    model = Contractor
    list_display = ('name', 'full_name', 'inn', 'kpp', 'registered_address',)
    list_display_links = ('name', 'full_name', 'inn',)
    search_fields = ('name', 'full_name', 'inn', 'kpp', 'registered_address',)


class ContractorUserAdmin(admin.ModelAdmin):
    model = ContractorUser
    list_display = ('user', 'contractor',)
    list_display_links = ('user', 'contractor',)
    search_fields = ('user__email', 'contractor__name',
                     'contractor__full_name', 'contractor__inn',
                     'contractor__kpp', 'contractor__registered_address',)


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ('name', 'external_code', 'for_bot', 'use',)
    list_filter = ('use', 'for_bot',)


class PaymentTypeAdmin(admin.ModelAdmin):
    model = PaymentType
    list_display = ('name', 'external_code', 'for_bot', 'use',)
    list_filter = ('use', 'for_bot',)


class DeliveryTypeAdmin(admin.ModelAdmin):
    model = DeliveryType
    list_display = ('name', 'external_code', 'for_bot', 'use',)
    list_filter = ('use', 'for_bot',)


class UserSettingsAdmin(admin.ModelAdmin):
    model = UserSettings
    list_display = ('user', 'currency', 'price_type',)


class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = ('code', 'external_code', 'valid_from',
                    'valid_to', 'for_discount', 'discount_percentage',
                    'amount', 'currency', 'active',)
    list_display_links = ('code', 'external_code',)
    list_filter = ('active',)
    list_editable = ('active',)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('pk', 'user', 'phone', 'email', 'status', 'delivery_date', 'delivery_type', 'paid', 'canceled',
                    'quantity', 'amount', 'discount', 'coupon', 'external_code', 'warehouse', 'currency', 'time_create',)
    list_display_links = ('pk', 'user', 'phone', 'status',)
    list_filter = ('status', 'delivery_type', 'payment_type',
                   'paid', 'canceled', 'time_create',)
    search_fields = ('user__email', 'phone',
                     'external_code', 'warehouse__name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(UnitMeasure, UnitMeasureAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(FavoriteProduct, FavoriteProductAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeValues, AttributeValuesAdmin)
admin.site.register(AttributeProductValues, AttributeProductValuesAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(PriceType, PriceTypeAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(StockProducts, StockProductsAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(ContractorUser, ContractorUserAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(DeliveryType, DeliveryTypeAdmin)
admin.site.register(UserSettings, UserSettingsAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Order, OrderAdmin)
