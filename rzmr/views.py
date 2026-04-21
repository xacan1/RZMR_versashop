from django.views.generic import FormView, RedirectView
from django.http import HttpRequest, HttpResponse, FileResponse
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rzmr.forms import *
from shop.mixins import DataMixin
# from pathlib import Path


# class FileView(FormView):
#     def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         filename = 'robots.txt'
#         path_file = Path(Path.cwd(), filename)
#         response = FileResponse(open(path_file, 'rb'), as_attachment=True,
#                                 filename='robots.txt', content_type='text/plain')

#         return response


class RobotsView(FormView):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        lines = [
            'User-Agent: Yandex',
            'Disallow: /metalhose-constructor/',
            'Disallow: /admin-rzmr/',
            'Disallow: /privacy/',
            'Disallow: /login/',
            'Disallow: /registration/',
            'Disallow: /passwords/reset/',
            'Disallow: /shop/cart/',
            'Disallow: /shop/checkout/',
            'Disallow: /*page=1',
            '',
            'Clean-param: price_range_max&sorting',
            '',
            'User-Agent: *',
            'Disallow: /metalhose-constructor/',
            'Disallow: /admin-rzmr/',
            'Disallow: /privacy/',
            'Disallow: /login/',
            'Disallow: /registration/',
            'Disallow: /passwords/reset/',
            'Disallow: /shop/cart/',
            'Disallow: /shop/checkout/',
            'Disallow: /*page=1',
            'Disallow: /*price_range_max=',
            'Disallow: /*sorting=',
            '',
            f'Sitemap: https://{request.get_host()}/sitemap.xml',
            '',
        ]
        response = HttpResponse('\n'.join(lines), content_type='text/plain')

        return response


class RequestPhoneCallView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_success_url(self) -> str:
        # возвращаем текущий URL при успешной отправке формы для того что бы покупатель остался на той странице откуда отправлял запрос
        current_url = self.request.META.get('HTTP_REFERER', '#')
        return current_url


# class RedirectToCityView(RedirectView):
#     permanent = True
#     query_string = False
#     pattern_name = 'redirect-to-city'

#     def get_redirect_url(self, *args, **kwargs):
#         url = super().get_redirect_url(*args, **kwargs)
#         company_cities = settings.COMPANY_CITIES
#         current_city = self.request.GET.get('city', '')

#         for prefix, city in company_cities.items():
#             if current_city == city:
#                 url = f'https://{prefix}.{settings.COMPANY_HOST}{self.request.get_full_path()}'
#                 break

#         return url


class FeedbackView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_success_url(self) -> str:
        # возвращаем текущий URL при успешной отправке формы для того что бы покупатель остался на той странице откуда отправлял запрос
        current_url = self.request.META.get('HTTP_REFERER', '#')
        return current_url

    def form_valid(self, form) -> HttpResponse:
        form.send_email_for_feedback()
        return super().form_valid(form)


class IndexView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Металлорукава от производителя по высоким стандартам 🥇 {settings.COMPANY_NAME}'
        description = f'{settings.COMPANY_NAME} является одним из крупнейших поставщиков металлорукавов(гибких трубопроводов), рукавов высокого давления, компенсаторов сильфонных и фланцевых и др. высокотехнологичной продукции. Наша продукция востребована на рынке России и стран ближнего зарубежья.'
        c_def = self.get_user_context(title=title, description=description)
        return {**context, **c_def}


class AboutView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/about.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("About us")} - {settings.COMPANY_NAME_SHORT}'
        description = f'{settings.COMPANY_NAME} ({settings.COMPANY_NAME_SHORT}) является одним из крупнейших поставщиков промышленного оборудования на рынке России и стран ближнего зарубежья. Наш опыт, наличие производственных мощностей позволяет в короткие сроки разрабатывать и производить уникальные, высоконадежные и долговечные изделия.'
        breadcrumb = [('about', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("Quality and certification system")} - {settings.COMPANY_NAME_SHORT}'
        description = f'Продукция {settings.COMPANY_NAME} отвечает самым высоким стандартам в отрасли. Ключевым элементом поддержания надежности и долговечности производимых изделий является принятая система менеджмента качества ISO 9001-2015.'
        breadcrumb = [('quality', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("Our clients")} - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться с клиентами компании {settings.COMPANY_NAME}.'
        breadcrumb = [('our-customer', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class ForSuppliersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/for-suppliers.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Поставщикам - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться с информацией для поставщиков компании {settings.COMPANY_NAME}.'
        breadcrumb = [('for-suppliers', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class VacanciesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/vacancies.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("Vacancies")} - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться с актуальными вакансиями компании {settings.COMPANY_NAME}.'
        breadcrumb = [('vacancies', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class ContactsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/contacts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("Contacts")} - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться с контактной информацией компании {settings.COMPANY_NAME}.'
        breadcrumb = [('contacts', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class SpheresView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/spheres.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Сферы применения металлорукавов — {settings.COMPANY_NAME}'
        description = f'В данном разделе вы можете ознакомиться со сферами применения металлорукавов компании {settings.COMPANY_NAME}.'
        h1 = 'Сферы применения'
        breadcrumb = [('spheres', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class SphereView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'spheres_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/sphere_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        breadcrumb = [('spheres', 'Сферы применения'),]
        suffix_title = {
            'mechanical_engineering': 'Применение металлорукавов в машиностроении',
            'aviation_industry': 'Металлорукава и авиационная промышленность',
            'gas_industry': 'Газовая отрасль: применение металлорукавов',
            'chemical_industry': 'Металлорукава: эффективное решение для химической промышленности',
            'oil_refining': 'Использование металлорукавов в нефтепереработке',
            'food_industry': 'Металлорукава: гигиеничность и функциональность для пищевой промышленности',
        }
        title = f'{suffix_title.get(slug, "")} - {settings.COMPANY_NAME}'
        description = ''

        if slug == 'mechanical_engineering':
            description = 'Использование металлических рукавов в машиностроении. Преимущества, конструктивные особенности и свойства металлорукавов для машиностроения.'
        elif slug == 'aviation_industry':
            description = 'Использование металлических рукавов в авиационной промышленности. Преимущества, конструктивные особенности и свойства металлорукавов для авиационного производства и обслуживания.'
        elif slug == 'gas_industry':
            description = 'Использование металлических рукавов в газовой отрасли. Преимущества, конструктивные особенности и свойства металлорукавов для транспортировки газа.'
        elif slug == 'chemical_industry':
            description = 'Использование металлических рукавов в химической промышленности. Преимущества, конструктивные особенности и свойства металлорукавов для химического производства.'
        elif slug == 'oil_refining':
            description = 'Использование металлических рукавов в нефтеперерабатывающей промышленности. Преимущества, конструктивные особенности и свойства металлорукавов для нефтепереработки.'
        elif slug == 'food_industry':
            description = 'Использование металлических рукавов в пищевой промышленности. Преимущества, конструктивные особенности и свойства металлорукавов для производства продуктов питания.'

        h1 = f'{suffix_title.get(slug, "")}'
        breadcrumb.append((slug, title))
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class SphereMechanicalEngineeringView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/sphere_mechanical_engineering.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Применение металлорукавов в машиностроении'
        breadcrumb = [('spheres', 'Сферы применения'),
                      ('spheres-mechanical-engineering', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class SphereAviationIndustryView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/sphere_mechanical_engineering.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Применение металлорукавов в машиностроении'
        breadcrumb = [('spheres', 'Сферы применения'),
                      ('spheres-mechanical-engineering', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("Metal hoses")} в {city_pre}, заказать металлические рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать металлорукава в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить гибкие герметичные металлические рукава можно на сайте или по тел.: {phone}.'
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesForWeldingView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_pod_privarku.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("Metal hoses")} {_("For welding")} в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать {_("Metal hoses")} {_("For welding")} в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить металлорукава под приварку можно на сайте или по тел.: {phone}.'
        h1 = f'{_("Metal hoses")} {_("For welding")} в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("Metal hoses")} РГМ в {city_pre} заказать {_("Metal hoses")} в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать {_("Metal hoses")} РГМ в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и заказать гибкие металлические рукава можно на сайте или по тел.: {phone}.'
        h1 = f'Гибкие {_("Metal hoses")} (РГМ) в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


# class MetalhosesGibkieTruboprovodyView(DataMixin, FormView):
#     form_class = SimpleForm
#     template_name = 'rzmr/metalhoses_gibkie_truboprovody.html'

#     def get_context_data(self, **kwargs) -> dict:
#         context = super().get_context_data(**kwargs)
#         title = 'Гибкие трубопроводы'
#         breadcrumb = [('metalhoses', _('Metal hoses')),
#                       ('', title),]
#         c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
#         return {**context, **c_def}


class MetalhosesVOpletkeView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_v_opletke.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'{_("Metal hoses")} в оплётке - {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'{_("Fittings")} для металлорукавов в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'{_("Fittings")} (фитинги) от {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        h1 = f'{_("Fittings")} для металлорукавов серии РГМ производства {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', h1),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'Гофрированные металлорукава РГМ в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'Гофра для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        h1 = 'Гофрированные металлорукава РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', h1),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'metalhoses_corrugation_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/metalhoses_corrugation_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        suffix_title = {
            'standartnaya': 'средней гибкости',
            'povishennoy_gibkosti': 'повышенной гибкости',
            'tyazhelaya_seriya': 'тяжёлой серии до 400 кгс/см²',
            'spiralnaya': 'cпиральные',
            'dvukhsloynaya': 'двухслойные',
        }
        title = f'Гофрированные металлорукава РГМ {suffix_title.get(slug, "")} в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'Гофры {suffix_title.get(slug, "")} для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        h1 = f'Гофрированные металлорукава РГМ {suffix_title.get(slug, "")}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugations', 'Гофрированные металлорукава РГМ'),
                      ('', h1),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'Металлорукава в оплётке в {city_pre}, заказать металлические рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать металлические рукава в оплётке из нержавеющей стали в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить металлорукава в металлической оплетке можно на сайте или по тел.: {phone}.'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', 'Металлорукава в оплетке'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'metalhoses_braid_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/metalhoses_braid_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'odnosloynaya': 'Однослойная',
            'dvukhsloynaya': 'Двухслойная',
            'trekhsloynaya': 'Трёхслойная',
        }
        title = f'{suffix_title.get(slug, "")} оплётка для металлорукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'Оплётка {suffix_title.get(slug, "")} для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braids', 'Оплётка'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Внутренний экран для металлорукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'Внутренний экран для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'metalhoses_inner_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/metalhoses_inner_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        suffix_title = {
            'trubnyy': 'Трубный',
            'valtsovannyy': 'Вальцованный',
            'opletochnyy': 'Оплёточный',
            'ptfe': 'PTFE',
        }
        title = f'{suffix_title.get(slug, "")} внутренний экран для металлорукавов РГМ в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} внутренний экран для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inners', 'Внутренний экран'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'Оболочки для металлорукавов РГМ - {settings.COMPANY_NAME_SHORT}'
        description = f'Оболочки для металлорукавов РГМ — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsideView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'metalhoses_outside_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/metalhoses_outside_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        suffix_title = {
            'termochekhol': 'Термочехол',
            'termorukav': 'Терморукав',
            'rezinovaya_obolochka': 'Резиновая оболочка',
            'pruzhina': 'Пружина',
            'pletenka_mednaya_luzhenaya_pml': 'Плетёнка медная лужёная (ПМЛ)',
        }
        title = f'{suffix_title.get(slug, "")} для металлорукавов в {city_pre} - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} для металлорукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        h1 = f'{suffix_title.get(slug, "")} для металлорукавов'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outsides', 'Наружная оболочка'),
                      ('', h1),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesSpecialView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_special.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Специальные разработки - {settings.COMPANY_NAME}'
        description = f'В данном разделе вы можете ознакомиться со специальными разработками компании {settings.COMPANY_NAME}.'
        h1 = 'Специальные разработки'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-special', 'Специальные разработки')]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_recommendations.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Рекомендации по выбору металлорукава серии РГМ - {settings.COMPANY_NAME_SHORT}'
        description = f'Рекомендации по выбору металлорукава РГМ на сайте {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        h1 = f'Рекомендации по выбору металлорукава серии РГМ производства {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-recommendations', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Монтаж и безопасность металлорукавов серии РГМ производства {settings.COMPANY_NAME_SHORT}'
        description = f'Монтаж и безопасность металлорукавов РГМ от {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        h1 = 'Монтаж и безопасность металлорукавов серии РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-installation', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesStandartsRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_standarts_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Стандарты качества на металлорукава серии РГМ выпускаемые {settings.COMPANY_NAME_SHORT}'
        description = f'Стандарты качества на металлорукава РГМ производства {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        h1 = 'Стандарты качества на металлорукава серии РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-standarts-rgm', h1),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesHpressRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_hpress_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("High pressure metal hoses")} в {city_pre}, заказать металлические рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать {_("High pressure metal hoses")} в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить гибкие герметичные металлические рукава можно на сайте или по тел.: {phone}.'
        h1 = f'{_("High pressure metal hoses")} в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlexiblePipelinesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/gibkie-truboprovody.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'Гибкие трубопроводы в {city_pre}, заказать металлические рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать гибкие трубопроводы в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Изготовление по индивидуальным параметрам. Узнать подробности и купить гибкие металлические и фторопластовые трубопроводы можно на сайте или по тел.: {phone}.'
        h1 = f'Гибкие трубопроводы в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("PTFE Metal hoses")} в {city_pre}, заказать PTFE рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать герметичные фторопластовые рукава высокого давления (до 500 атм) в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить фторопластовые рукава (PTFE) можно на сайте или по тел.: {phone}.'
        h1 = f'{_("PTFE Metal hoses")} серии РФ в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEhosesGofrirovanniyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_gofrirovanniy.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("Corrugated")} {_("PTFE Metal hoses")} в {city_pre}, заказать PTFE рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать {_("Corrugated")} {_("PTFE Metal hoses")} высокого давления серии РФГ в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить гофрированные фторопластовые рукава (PTFE) можно на сайте или по тел.: {phone}.'
        h1 = f'{_("Corrugated")} {_("PTFE Metal hoses")} в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-gofrirovanniy', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFERecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_recommendations.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Рекомендации по измерениям и соответствиям стандартам - {settings.COMPANY_NAME_SHORT}'
        description = f'Рекомендации по выбору фторопластовых рукавов серии РФ от {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-recommendations', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Монтаж и безопасность фторопластовых рукавов серии РФ - {settings.COMPANY_NAME_SHORT}'
        description = f'Монтаж и безопасность фторопластовых рукавов серии РФ от {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-installation', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Концевая арматура для фторопластовых рукавов серии РФ - {settings.COMPANY_NAME_SHORT}'
        description = f'{_("PTFE Metal hoses")} серии РФ - Концевая арматура от {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        h1 = 'Концевая арматура для фторопластовых рукавов серии РФ'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-fittings', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEStandartsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_standarts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Стандарты качества для фторопластовых рукавов серии РФП, РФГ - {settings.COMPANY_NAME_SHORT}'
        description = f'Стандарты качества для фторопластовых рукавов серии РФП, РФГ выпускаемых {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-standarts', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class HpressPTFEView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_hpress.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'{_("PTFE Metal hoses")} высокого давления в {city_pre}, заказать PTFE рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Купить {_("PTFE Metal hoses")} высокого давления (до 500 атм) в {city_pre} можно на заводе {settings.COMPANY_NAME_SHORT}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и заказать фторопластовые рукава (PTFE) высокого давления можно на сайте или по тел.: {phone}.'
        h1 = f'{_("PTFE Metal hoses")} высокого давления в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-standarts', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Трубка для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'Трубка для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_pipe_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/ptfe_pipe_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'ploskaya_standartnoe_ispolnenie': 'Плоская в стандартном исполнении',
            'ploskaya_tolstostennaya': 'Плоская толстостенная',
            'gofrirovannaya_standartnoe_ispolnenie': 'Гофрированная в стандартном исполнении',
            'gofrirovannaya_tolstostennaya': 'Гофрированная толстостенная',
        }
        title = f'{suffix_title.get(slug, "")} трубка для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} трубка для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', 'Трубки'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEBraidsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_braid.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'Фторопластовые рукава в оплётке в {city_pre}, заказать PTFE рукава в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать фторопластовые рукава в оплётке из нержавеющей стали в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить фторопластовые рукава в металлической оплетке можно на сайте или по тел.: {phone}.'
        h1 = f'Фторопластовые рукава в металлической оплётке серии РФ в {city_pre} от производителя {settings.COMPANY_NAME_SHORT}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-braids', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEBraidView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_braid_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/ptfe_braid_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'odnosloynaya': 'Однослойная оплётка для фторопластовых рукавов',
            'dvukhsloynaya': 'Двухслойная оплётка для фторопластовых рукавов',
            'trekhsloynaya': 'Трёхслойная оплётка для фторопластовых рукавов',
        }
        title = f'{suffix_title.get(slug, "")} - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        h1 = f'{suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-braids', 'Оплётки'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFELinersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_liner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Футеровки PTFE - {settings.COMPANY_NAME_SHORT}'
        description = f'Футеровка PTFE для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована.'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFELinerView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_liner_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/ptfe_futerovka_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'gofrirovannoy_trubki_na_flanets': 'гофрированной трубки на фланец',
            'ploskoy_trubki_na_flanets': 'плоской трубки на фланец',
            'ploskoy_trubki_na_nippel_gayki': 'плоской трубки на ниппель гайки',
        }
        title = f'PTFE футеровка {suffix_title.get(slug, "")} для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'PTFE футеровка {suffix_title.get(slug, "")} для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', 'Футеровки PTFE'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Внутренний экран для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'Внутренний экран для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInnerView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_inner_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/ptfe_inner_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'antistaticheskaya_prisadka_ploskaya': 'антистатическая присадка плоская',
            'antistaticheskaya_prisadka_gofrirovannaya': 'антистатическая присадка гофрированная',
        }
        title = f'Внутренний экран: {suffix_title.get(slug, "")} для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', 'Внутренние экраны'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Наружная оболочка для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'Наружная оболочка для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована.'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEOutsideView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_outside_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/ptfe_outside_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'termochekhol': 'Термочехол',
            'rezinovaya_obolochka': 'Резиновая оболочка',
            'pruzhina': 'Пружина',
            'ploskaya_trubka_v_metallorukave_v_opletke': 'Плоская трубка в металлорукаве в оплётке',
            'gofrirovannaya_trubka_v_metallorukave_v_opletke': 'Гофрированная трубка в металлорукаве в оплётке',
        }
        title = f'{suffix_title.get(slug, "")} для фторопластовых рукавов - {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} для фторопластовых рукавов производства {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', 'Наружные оболочки'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Производство изделий на заказ - {settings.COMPANY_NAME_SHORT}'
        description = f'Принимаем заказы на изготовление нестандартное оборудование по чертежам заказчика - {settings.COMPANY_NAME} - Наша продукция востребована на рынке России и стран ближнего зарубежья'
        breadcrumb = [('engineering', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringAccessoriesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_accessories.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Технологическая оснастка - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться с технологической оснасткой компании {settings.COMPANY_NAME}.'
        breadcrumb = [('engineering', 'Производство изделий на заказ'),
                      ('engineering-accessories', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringTestView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_test.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Испытания на герметичность и прочность - {settings.COMPANY_NAME_SHORT}'
        description = f'{settings.COMPANY_NAME} на договорной основе проводит испытаний всех типов рукавов на герметичность и прочность - Наша продукция востребована на рынке России и стран ближнего зарубежья.'
        breadcrumb = [('engineering', 'Производство изделий на заказ'),
                      ('engineering-test', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PrivacyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/privacy.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Privacy policy')
        breadcrumb = [('privacy', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class WorkspaceFiltersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/workspace_filters.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Рабочие среды фильтров и агрегатов - {settings.COMPANY_NAME_SHORT}'
        description = f'Рабочие среды фильтров и агрегатов. {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика.✔️Индивидуальный подход.✔️Вся продукция сертифицирована'
        breadcrumb = [('workspace-filters', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class FittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, _ = self.get_client_city(subdomain)
        title = f'Резьбовая арматура, купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'Резьбовая арматура — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = 'Резьбовая арматура'
        breadcrumb = [('privacy', 'Резьбовая арматура'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class FittingView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'fitting_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'gayka-nakidnaya-pod-tortsevoe-uplotnenie': 'Гайка накидная под торцевое уплотнение',
            'mufta-amerikanka-bp-bp': 'Муфта "американка" BP-BP',
            'mufta-amerikanka-s-vnutrenney-rezboy-hp-bp': 'Муфта "американка" с внутренней резьбой HP-BP',
            'mufta-amerikanka-s-naruzhnoy-rezboy-hp-hp': 'Муфта "американка" с наружной резьбой HP-HP',
            'nakidnaya-gayka-s-nippelem-konus-s-uglom-74': 'Накидная гайка с ниппелем конус с углом 74°',
            'nakidnaya-gayka-s-nippelem-konus-s-uglom-24': 'Накидная гайка с ниппелем конус с углом 24°',
            'nakidnaya-gayka-s-nippelem-sfera-pod-konus-s-uglom-60': 'Накидная гайка с ниппелем сфера под конус с углом 60°',
            'perekhodnik-gayka-gayka': 'Переходник гайка-гайка',
            'perekhodnik-gayka-shtutser': 'Переходник гайка-штуцер',
            'perekhodnik-shtutser-shtutser': 'Переходник штуцер-штуцер',
            'fitting-dk0': 'Фитинг DK',
            'fitting-dk-shtutser': 'Фитинг DK-штуцер',
            'fitting-dki': 'Фитинг DKI',
            'fitting-dkol': 'Фитинг DKOL',
            'shtutser-s-vnutrenney-rezboy': 'Штуцер с внутренней резьбой',
            'shtutser-s-naruzhnoy-rezboy': 'Штуцер с наружной резьбой',
        }
        subdomain = self.get_subdomain()
        city_pre, _ = self.get_client_city(subdomain)
        title = f'{suffix_title.get(slug, "")} , купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = suffix_title.get(slug, "")
        breadcrumb = [('fittings', 'Резьбовая арматура'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class CompositesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/composite.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, _ = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'Композитные рукава в {city_pre}, заказать композитные шланги в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать композитные рукава в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить композитные рукава для нефтепродуктов и других жидкостей и газов можно на сайте или по тел.: {phone}.'
        breadcrumb = [('composite', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class CompositeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'composite_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/composite_{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        subdomain = self.get_subdomain()
        city_pre, _ = self.get_client_city(subdomain)
        phone = self.get_company_phone(subdomain)
        title = f'Композитные рукава серии {slug} в {city_pre}, заказать композитные шланги в {settings.COMPANY_NAME_SHORT}'
        description = f'Заказать композитные рукава серии {slug} в {city_pre} можно в {settings.COMPANY_NAME}. Высокое качество и гибкая ценовая политика. Минимальная партия от 1 шт. Узнать подробности и купить композитные шланги {slug} можно на сайте или по тел.: {phone}.'
        breadcrumb = [('composite', 'Композитные рукава'),
                      (slug, f'Композитные рукава серии {slug}'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      slug=slug,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlangesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/flanges.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'{_("Flange connections")}, купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'{_("Flange connections")} — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = _('Flange connections')
        breadcrumb = [('composite', _('Flange connections')),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlangeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'flange_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'flantsevoe-soedinenie-gost-12821-80': 'Фланцевое соединение ГОСТ 12821-80',
            'flantsevoe-soedinenie-gost-12822-80': 'Фланцевое соединение ГОСТ 12822-80',
            'flantsevoe-soedinenie-s-otkidnymi-boltami': 'Фланцевое соединение с откидными болтами',
            'flantsevoe-soedinenie-svobodnoe-na-otbortovke': 'Фланцевое соединение свободное на отбортовке',
            'flantsevoe-soedinenie-tip-01-po-gost-33259-2015': 'Фланцевое соединение тип 01 по ГОСТ 33259-2015',
            'flantsy-iz-nalichiya': 'Фланцы из наличия',
        }
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'{suffix_title.get(slug, "")}, купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = suffix_title.get(slug, "")
        breadcrumb = [('flanges', _('Flange connections')),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class QuickReleaseCouplingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quick-release-coupling.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'Быстроразъемные соединения, купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'Быстроразъемные соединения — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = 'Быстроразъемные соединения'
        breadcrumb = [('quick-release-coupling',
                       'Быстроразъемные соединения'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class QuickReleaseCouplingView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'coupling_slug'

    def get_template_names(self) -> list[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        suffix_title = {
            'adaptor-bystrorazyemnogo-soedineniya-tipa-kamlok-mufta': 'Адаптор быстроразъёмного соединения типа "Камлок" (муфта)',
            'adaptor-bystrorazyemnogo-soedineniya-tipa-kamlok-shtutser': 'Адаптор быстроразъёмного соединения типа "Камлок" (штуцер)',
            'armatura-pmt': 'Арматура "ПМТ"',
            'gayka-rot-isp-1': 'Гайка РОТ исп. 1',
            'gayka-rot-isp-2': 'Гайка РОТ исп. 2',
            'gayka-rot-isp-3': 'Гайка РОТ исп. 3',
            'kamlok-tipa-b': 'Камлок типа B',
            'kamlok-tipa-d0': 'Камлок типа D',
            'kamlok-tipa-dc': 'Камлок типа DC',
            'kamlok-tipa-dp': 'Камлок типа DP',
            'kamlok-tipa-e': 'Камлок типа E',
            'kamlok-tipa-f': 'Камлок типа F',
            'kamlok-tipa-a': 'Камлок типа А',
            'kamlok-tipa-c': 'Камлок типа С',
            'koltso-uplotnitelnoe-dlya-gayki-rot': 'Кольцо уплотнительное для гайки РОТ',
            'strubtsina-s-prizhimnym-ustroystvom-sug': 'Струбцина с прижимным устройством (СУГ)',
        }
        subdomain = self.get_subdomain()
        city_pre, city_location = self.get_client_city(subdomain)
        title = f'{suffix_title.get(slug, "")}, купить в {city_pre} по выгодной цене в {settings.COMPANY_NAME_SHORT}'
        description = f'{suffix_title.get(slug, "")} — купить в {city_pre} по выгодной цене от производителя {settings.COMPANY_NAME_SHORT}. ✔️Гибкая ценовая политика. ✔️100% гарантия качества. ✔️Вся продукция сертифицирована. Узнайте подробности и оформите заказ на нашем сайте.'
        h1 = suffix_title.get(slug, "")
        breadcrumb = [('quick-release-coupling',
                       'Быстроразъемные соединения'),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      h1=h1,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}
