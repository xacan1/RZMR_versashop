from django.forms import BaseModelForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, FileResponse
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import io
from shop.forms import *
from shop import services
from shop.models import *
from shop.mixins import DataMixin
from shop import request1C


class IndexShopView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        top_products = services.get_top_sales()
        context['top_products'] = top_products
        c_def = self.get_user_context(title=_('Shop'))
        return {**context, **c_def}


# class AboutAsView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/about-us.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='О нас')
#         return {**context, **c_def}


class CartView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Cart'))
        return {**context, **c_def}


class WishlistView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/wishlist.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        wishlist = services.get_favorite_products_info(self.request.user)
        c_def = self.get_user_context(
            title='Избранные товары', wishlist=wishlist)
        return {**context, **c_def}


# class ContactView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/contact.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Обратная связь')
#         return {**context, **c_def}


# class FaqView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/faq.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='FAQ')
#         return {**context, **c_def}


# class PrivacyPolicyView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/privacy-policy.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Политика конфиденциальности')
#         return {**context, **c_def}


# class UserAgreementView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/user-agreement.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Пользовательское соглашение')
#         return {**context, **c_def}


# class PurchaseReturnsView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'shop/purchase-returns.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Пользовательское соглашение')
#         return {**context, **c_def}


# выводит либо список категорий либо список номенклатуры если в категории больше нет подкатегорий
# products_exist - признак что товары есть в категории, даже если и не найдены из-за фильтров
class CategoryProductListView(DataMixin, FormView):
    slug_url_kwarg = 'category_slug'
    price_products = Product.objects.none()
    products_exist = False

    # проверяет если товары есть, то выбирает класс формы для списка товаров иначе класс пустой формы
    def get_form_class(self):
        form_class = super().get_form_class()
        slug = self.kwargs.get('category_slug', '')

        if slug and slug != 'root':
            self.price_products, self.products_exist = services.filter_products_for_category(
                slug, self.request.GET)
            self.price_products = services.sorted_products_for_category(
                self.price_products, self.request.GET)

        form_class = ProductListForm if self.products_exist else SimpleForm
        return form_class

    # передадим данные в форму
    def get_initial(self):
        initial = super().get_initial()
        slug = self.kwargs.get('category_slug', '')
        min_max_price = services.get_min_max_price_category(slug)
        initial = {**initial, **min_max_price}
        initial['get_params'] = self.request.GET
        self.attribute_groups = services.get_attributes_category_with_values(
            slug)
        initial['attribute_groups'] = self.attribute_groups
        return initial

    def get_template_names(self) -> list[str]:
        template_names = []

        if self.products_exist:
            template_names.append('shop/product-list.html')
        else:
            template_names.append('shop/category-grids.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('category_slug', '')
        parent_categories = services.get_parents_category(slug, [])

        subdomain = self.get_subdomain()
        city_pre, _ = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        description, title, h1 = services.get_info_about_category_for_seo(slug, city_pre, phone)

        if slug == 'root':
            root_categories = services.get_root_categories()
            c_def = self.get_user_context(title='Каталог',
                                          nested_categories=root_categories)
        elif self.products_exist:
            paginate_by = 12
            paginator = Paginator(self.price_products, paginate_by)
            page_number = self.request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            amount_product_total = paginator.count
            amount_product_from, amount_product_upto = services.count_product_from_to(paginate_by,
                                                                                      int(page_number),
                                                                                      len(page_obj.object_list))

            # добавляю к адресам пагинации параметры запроса, что бы при переходе на другую страницу
            # GET запрос не только содержал номер страницы, но и в точности повторялся по всем параметрам
            add_for_pagination = ''

            for get_param, value in self.request.GET.items():
                if get_param == 'page':
                    continue
                
                if add_for_pagination:
                    add_for_pagination += f'&{get_param}={value}'
                else:
                    add_for_pagination = f'{get_param}={value}'

            c_def = self.get_user_context(title=title,
                                          description=description,
                                          h1=h1,
                                          amount_product_from=amount_product_from,
                                          amount_product_upto=amount_product_upto,
                                          amount_product_total=amount_product_total,
                                          parent_categories=parent_categories,
                                          add_for_pagination=add_for_pagination,
                                          page_obj=page_obj)
        else:
            category, nested_categories = services.get_nested_categories(slug)
            c_def = self.get_user_context(title=title,
                                          current_category=category,
                                          description=description,
                                          h1=h1,
                                          nested_categories=nested_categories,
                                          parent_categories=parent_categories)

        return {**context, **c_def}


class SearchView(DataMixin, ListView):
    template_name = 'shop/product-list.html'
    paginate_by = 10
    min_max_price = {'price__min': 0, 'price__max': 0}
    amount_product_from = 0
    amount_product_upto = 0
    amount_product_total = 0

    # def get_paginate_by(self, queryset: _BaseQuerySet[Any]) -> Optional[int]:
    #     return super().get_paginate_by(queryset)

    def paginate_queryset(self, queryset, page_size) -> tuple[Paginator, int, models.QuerySet[Product], bool]:
        paginator, page, page_obj, has_other_pages = super(
        ).paginate_queryset(queryset, page_size)
        self.amount_product_total = paginator.count
        self.amount_product_from, self.amount_product_upto = services.count_product_from_to(
            self.paginate_by, page.number, page_obj.count())
        return paginator, page, page_obj, has_other_pages

    def get_queryset(self) -> models.QuerySet[Product]:
        q = self.request.GET.get('q')
        queryset, self.min_max_price = services.search_products(q)
        return queryset

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        add_for_pagination = f'&q={q}'

        c_def = self.get_user_context(title=f"{_('search')}: {q}",
                                      search_text=q,
                                      amount_product_from=self.amount_product_from,
                                      amount_product_upto=self.amount_product_upto,
                                      amount_product_total=self.amount_product_total,
                                      add_for_pagination=add_for_pagination,
                                      min_max_price=self.min_max_price,
                                      total_show_product=self.paginate_by)
        return {**context, **c_def}


class ProductDetailView(DataMixin, DetailView):
    model = Product
    template_name = 'shop/product-details.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product_data'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        product_pk = kwargs['object'].pk
        slug = kwargs['object'].category.slug
        images = kwargs['object'].get_images.all()
        stocks = kwargs['object'].get_stock_product.all()
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f"{kwargs['object'].name}, купить в городе {city_pre}"
        phone = self.get_company_phone(subdomain)
        description = f"""{kwargs['object'].name} — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}.
          Гибкая ценовая политика. 100% гарантия качества. Вся продукция сертифицирована. 
          Узнать подробности оформить заказ можно на нашем сайте или по тел.:{ phone }"""

        prices = kwargs['object'].get_prices.all()  # пока нет выбора типов цен
        attributes = services.get_attributes_product(product_pk)
        parent_categories = services.get_parents_category(slug, [])
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      parent_categories=parent_categories,
                                      product_images=images,
                                      product_stocks=stocks,
                                      product_prices=prices,
                                      product_attributes=attributes)
        return {**context, **c_def}


class AddOrderView(DataMixin, CreateView):
    form_class = AddOrderForm
    template_name = 'shop/checkout.html'
    success_url = reverse_lazy('new-order-success')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cart_info = services.get_cart_full_info(user=self.request.user,
                                                session_key=self.request.session.session_key)
        if not cart_info['products']:
            # вдруг корзина пустая, что бы не создавать пустой заказ
            return redirect('cart')

        form.instance.user = self.request.user if self.request.user.is_authenticated else None
        response = super().form_valid(form)
        order = form.instance
        services.changing_cart_rows_to_order_rows(self.request.user, order,
                                                  self.request.session.session_key)
        services.send_email_for_order_success(order.pk)

        # тут надо вызвать функцию createOrder для формирования заказа в 1С
        services.create_order_in_1C(order)

        return response

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        cart = services.get_cart_full_info(user=self.request.user,
                                           session_key=self.request.session.session_key)

        # установим значения формы если пользователь уже залогинен
        if self.request.user.is_authenticated:
            form = self.form_class(initial={'first_name': self.request.user.first_name,
                                            'last_name': self.request.user.last_name,
                                            'email': self.request.user.email,
                                            'phone': self.request.user.phone,
                                            'user': self.request.user})
            context['form'] = form

        c_def = self.get_user_context(title='Оформление заказа', cart=cart)
        return {**context, **c_def}


class AddOrderSuccessView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/new-order-success.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заказ оформлен')
        return {**context, **c_def}


class OrderView(LoginRequiredMixin, DataMixin, DetailView):
    model = Order
    template_name = 'shop/order.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_pk'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        order = kwargs['object']
        breadcrumb = [
            ('personal-account', _('Personal account')),
            ('user-orders', _('Orders')),
        ]
        c_def = self.get_user_context(title=f'{order}', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OrderCancelConfirmView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/order-cancel-confirm.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        order_pk = self.kwargs.get('order_pk', 0)
        c_def = self.get_user_context(title='Отмена заказа', order_pk=order_pk)
        return {**context, **c_def}


class OrderCancelCompleteView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'shop/order-cancel-complete.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        order_pk = int(self.kwargs.get('order_pk', 0))
        services.cancel_order(self.request.user, order_pk)
        services.send_email_for_order_cancel(order_pk)
        c_def = self.get_user_context(
            title='Заказ отменен', order_number=order_pk)
        return {**context, **c_def}


class ContractorUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
    model = Contractor
    form_class = AddContractorForm
    template_name = 'shop/contractor-update.html'
    context_object_name = 'contractor'
    pk_url_kwarg = 'contractor_pk'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('user-companies')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        kwargs = self.get_form_kwargs()
        contractor = kwargs['instance']
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-companies', 'Организации'),]
        c_def = self.get_user_context(title=f'Редактирование организации: {contractor.name}',
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class ContractorCreateView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddContractorForm
    template_name = 'shop/contractor-create.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('user-companies')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-companies', 'Организации'),]
        c_def = self.get_user_context(title='Добавление организации',
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


# Прокси запросы к серверу 1С как в конструкторе, не везде есть конструктор в магазине, так что придется дублировать логику тут
class ProxyRequestView(FormView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.buffer = io.BytesIO()

    def __del__(self) -> None:
        if self.buffer:
            self.buffer.close()

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        url_request = request.headers.get('Request1C', '')
        response_data = request1C.get_request_to_1C(url_request)

        if type(response_data) is str:
            response = HttpResponse(response_data)
        else:
            self.buffer.write(response_data)
            self.buffer.seek(0)
            response = FileResponse(
                self.buffer, as_attachment=True, filename='order.pdf')

        return response
