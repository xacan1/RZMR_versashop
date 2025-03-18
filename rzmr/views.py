from django.views.generic import FormView
from rzmr.forms import *
from shop.mixins import DataMixin
from django.http import HttpRequest, HttpResponse, FileResponse
from django.utils.translation import gettext_lazy as _
from pathlib import Path


class RobotView(DataMixin, FormView):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        filename = 'robots.txt'
        path_file = Path(Path.cwd(), filename)
        response = FileResponse(open(path_file, 'rb'), as_attachment=True,
                                filename='robots.txt', content_type="text/plain")

        return response


class RequestPhoneCallView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_success_url(self) -> str:
        # возвращаем текущий URL при успешной отправке формы для того что бы покупатель остался на той странице откуда отправлял запрос на звонок
        current_url = self.request.META.get('HTTP_REFERER', '#')
        return current_url

    def form_valid(self, form) -> HttpResponse:
        form.send_email_for_call()
        return super().form_valid(form)


class FeedbackView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_success_url(self) -> str:
        # возвращаем текущий URL при успешной отправке формы для того что бы покупатель остался на той странице откуда отправлял запрос на звонок
        current_url = self.request.META.get('HTTP_REFERER', '#')
        return current_url

    def form_valid(self, form) -> HttpResponse:
        form.send_email_for_feedback()
        return super().form_valid(form)


class IndexView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_context_data(self, **kwargs) -> dict:
        # self.request.get_host()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class AboutView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/about.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('About us')
        breadcrumb = [('about', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Quality and certification system')
        breadcrumb = [('quality', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Our clients')
        breadcrumb = [('our-customer', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class ForSuppliersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/for-suppliers.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Поставщикам'
        breadcrumb = [('for-suppliers', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class VacanciesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/vacancies.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Career')
        breadcrumb = [('vacancies', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class ContactsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/contacts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Contacts')
        breadcrumb = [('contacts', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class SpheresView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/spheres.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Сферы применения'
        breadcrumb = [('spheres', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = suffix_title.get(slug, "")
        breadcrumb.append((slug, title))
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = _('Metal hoses')
        breadcrumb = [('metalhoses', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesForWeldingView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_pod_privarku.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f"{_('Metal hoses')} {_('For welding')}"
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f"{_('Metal hoses')} РГМ"
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesGibkieTruboprovodyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_gibkie_truboprovody.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Гибкие трубопроводы'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesVOpletkeView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_v_opletke.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f"{_('Metal hoses')} в оплётке"
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Fittings')
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Гофрированные металлорукава РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        suffix_title = {
            'standartnaya': 'средней гибкости',
            'povishennoy_gibkosti': 'повышенной гибкости',
            'tyazhelaya_seriya': 'тяжёлой серии до 400 кгс/см²',
            'spiralnaya': 'cпиральные',
            'dvukhsloynaya': 'двухслойные',
        }
        title = f'Гофрированные металлорукава РГМ {suffix_title.get(slug, "")}'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugations', 'Гофрированные металлорукава РГМ'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Оплётка'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = f'{suffix_title.get(slug, "")} оплётка для металлорукавов'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braids', 'Оплётка'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Внутренний экран'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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

        suffix_title = {
            'trubnyy': 'Трубный',
            'valtsovannyy': 'Вальцованный',
            'opletochnyy': 'Оплёточный',
            'ptfe': 'PTFE',
        }
        title = f'{suffix_title.get(slug, "")} внутренний экран'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inners', 'Внутренний экран'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Наружная оболочка'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        suffix_title = {
            'termochekhol': 'Термочехол',
            'termorukav': 'Терморукав',
            'rezinovaya_obolochka': 'Резиновая оболочка',
            'pruzhina': 'Пружина',
            'pletenka_mednaya_luzhenaya_pml': 'Плетёнка медная лужёная (ПМЛ)',
        }
        title = f'{suffix_title.get(slug, "")} для металлорукавов'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outsides', 'Наружная оболочка'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesSpecialView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_special.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-special', 'Специальные разработки')]
        c_def = self.get_user_context(
            title='Специальные разработки', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_recommendations.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Рекомендации по выбору металлорукава серии РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-recommendations', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Монтаж и безопасность металлорукавов серии РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-installation', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesStandartsRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_standarts_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Стандарты качества на металлорукава серии РГМ'
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-standarts-rgm', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class HpressRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_hpress_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('High pressure metal hoses')
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlexiblePipelinesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/gibkie-truboprovody.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Гибкие трубопроводы'
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f"{_('PTFE Metal hoses')} серии РФ"
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEhosesGofrirovanniyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_gofrirovanniy.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f"{_('Corrugated')} {_('PTFE Metal hoses')}"
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-gofrirovanniy', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFERecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_recommendations.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Рекомендации по измерениям и соответствиям стандартам'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-recommendations', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Монтаж и безопасность фторопластовых рукавов'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-installation', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Концевая арматура для фторопластовых рукавов серии РФ'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-fittings', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEStandartsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_standarts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Стандарты качества для фторопластовых рукавов серии РФП, РФГ'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-standarts', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class HpressPTFEView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_hpress.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Фторопластовые рукава высокого давления'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-standarts', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Трубки для фторопластовых рукавов'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
            'ploskaya_standartnoe_ispolnenie': 'плоская в стандартном исполнении',
            'ploskaya_tolstostennaya': 'плоская толстостенная',
            'gofrirovannaya_standartnoe_ispolnenie': 'гофрированная в стандартном исполнении',
            'gofrirovannaya_tolstostennaya': 'гофрированная толстостенная',
        }
        title = f'Трубка для фторопластовых рукавов {suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', 'Трубки'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEBraidsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_braid.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Фторопластовые рукава в металлической оплётке серии РФ'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-braids', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = f'{suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-braids', 'Оплётки'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFELinersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_liner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Футеровки PTFE'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = f'Футеровка PTFE {suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', 'Футеровки PTFE'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Внутренние экраны для фторопластовых рукавов'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = f'Внутренний экран: {suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', 'Внутренние экраны'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Наружные оболочки для фторопластовых рукавов'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
            'termochekhol': 'термочехол',
            'rezinovaya_obolochka': 'резиновая оболочка',
            'pruzhina': 'пружина',
            'ploskaya_trubka_v_metallorukave_v_opletke': 'плоская трубка в металлорукаве в оплётке',
            'gofrirovannaya_trubka_v_metallorukave_v_opletke': 'гофрированная трубка в металлорукаве в оплётке',
        }
        title = f'Наружная оболочка: {suffix_title.get(slug, "")}'
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', 'Наружные оболочки'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Производство изделий на заказ'
        breadcrumb = [('engineering', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringAccessoriesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_accessories.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Технологическая оснастка'
        breadcrumb = [('engineering', 'Производство изделий на заказ'),
                      ('engineering-accessories', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringTestView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_test.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Испытания на герметичность и прочность'
        breadcrumb = [('engineering', 'Производство изделий на заказ'),
                      ('engineering-test', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = 'Рабочие среды фильтров и агрегатов'
        breadcrumb = [('workspace-filters', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class FittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Резьбовая арматура'
        breadcrumb = [('privacy', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = 'Резьбовая арматура'
        breadcrumb = [('fittings', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class CompositesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/composite.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Композитные рукава'
        breadcrumb = [('composite', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = f'Композитный рукав {slug}'
        breadcrumb = [('composite', 'Композитные рукава'),
                      (slug, title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlangesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/flanges.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Flange connections')
        breadcrumb = [('composite', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = _('Flange connections')
        breadcrumb = [('flanges', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class QuickReleaseCouplingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quick-release-coupling.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Быстроразъёмные соединения'
        breadcrumb = [('quick-release-coupling', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
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
        title = 'Быстроразъёмные соединения'
        breadcrumb = [('quick-release-coupling', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}
