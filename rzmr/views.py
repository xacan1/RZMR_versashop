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


class RequestPhoneCall(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_success_url(self) -> str:
        # возвращаем текущий URL при успешной отправке формы для того что бы покупатель остался на той странице откуда отправлял запрос на звонок
        current_url = self.request.META.get('HTTP_REFERER', '#')
        return current_url

    def form_valid(self, form) -> HttpResponse:
        form.send_email()
        return super().form_valid(form)


class IndexView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class AboutView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/about.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Company'))
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=_('Quality and certification system'))
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Our clients'))
        return {**context, **c_def}


class ForSuppliersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/for-suppliers.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поставщикам')
        return {**context, **c_def}


class VacanciesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/vacancies.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Career'))
        return {**context, **c_def}


class ContactsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/contacts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return {**context, **c_def}


class MetalhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Metal hoses'))
        return {**context, **c_def}


class MetalhosesForWeldingView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_pod_privarku.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title=f"{_('Metal hoses')} {_('For welding')}", breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class MetalhosesRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title=f"{_('Metal hoses')} РГМ", breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class MetalhosesGibkieTruboprovodyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_gibkie_truboprovody.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Гибкие трубопроводы', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class MetalhosesVOpletkeView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_v_opletke.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title=f"{_('Metal hoses')} в оплетке", breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title=_('Fittings'), breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ', breadcrumb=breadcrumb)
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
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugations', 'Гофра')]
        suffix_title = {
            'standartnaya': 'средней гибкости',
            'povishennoy_gibkosti': 'повышенной гибкости',
            'tyazhelaya_seriya': 'тяжёлой серии до 400 кгс/см²',
            'spiralnaya': 'cпиральные',
            'dvukhsloynaya': 'двухслойные',
        }
        title = f'Гофрированные металлорукава РГМ {suffix_title.get(slug, "")}'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title='Оплётка', breadcrumb=breadcrumb)
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
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braids', 'Оплётка')]
        suffix_title = {
            'odnosloynaya': 'Однослойная',
            'dvukhsloynaya': 'Двухслойная',
            'trekhsloynaya': 'Трёхслойная',
        }
        title = f'{suffix_title.get(slug, "")} оплётка для металлорукавов'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Внутренний экран', breadcrumb=breadcrumb)
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
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inners', 'Внутренний экран')]
        suffix_title = {
            'trubnyy': 'Трубный',
            'valtsovannyy': 'Вальцованный',
            'opletochnyy': 'Оплёточный',
            'ptfe': 'PTFE',
        }
        title = f'{suffix_title.get(slug, "")} внутренний экран'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Наружная оплётка', breadcrumb=breadcrumb)
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
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outsides', 'Наружная оплётка')]
        suffix_title = {
            'termochekhol': 'Термочехол',
            'termorukav': 'Терморукав',
            'rezinovaya_obolochka': 'Резиновая оболочка',
            'pruzhina': 'Пружина',
            'pletenka_mednaya_luzhenaya_pml': 'Плетёнка медная лужёная (ПМЛ)',
        }
        title = f'{suffix_title.get(slug, "")} для металлорукавов'
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
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Рекомендации по выбору металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Монтаж и безопасность металлорукавов серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class StandartsRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_standarts_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Стандарты качества на металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class HpressRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_hpress_rgm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('High pressure metal hoses')
        c_def = self.get_user_context(title=title)
        return {**context, **c_def}


class PTFEhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=f"{_('PTFE Metal hoses')} серии РФ")
        return {**context, **c_def}


class PTFEhosesGofrirovanniyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_gofrirovanniy.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=f"{_('Corrugated')} {_('PTFE Metal hoses')}")
        return {**context, **c_def}


class PTFERecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_recommendations.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Рекомендации по измерениям и соответствиям стандартам', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_installation_safety.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Монтаж и безопасность фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Концевая арматура для фторопластовых рукавов серии РФ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEStandartsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_standarts.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Стандарты качества на фторопластовых рукавов серии РФП, РФГ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Трубки для фторопластовых рукавов', breadcrumb=breadcrumb)
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
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', 'Трубки'),]
        suffix_title = {
            'ploskaya_standartnoe_ispolnenie': 'плоская в стандартном исполнении',
            'ploskaya_tolstostennaya': 'плоская толстостенная',
            'gofrirovannaya_standartnoe_ispolnenie': 'гофрированная в стандартном исполнении',
            'gofrirovannaya_tolstostennaya': 'гофрированная толстостенная',
        }
        title = f'Трубка для фторопластовых рукавов {suffix_title.get(slug, "")}'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFELinersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_liner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Футеровки PTFE', breadcrumb=breadcrumb)
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
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', 'Футеровки PTFE'),]
        suffix_title = {
            'gofrirovannoy_trubki_na_flanets': 'гофрированной трубки на фланец',
            'ploskoy_trubki_na_flanets': 'плоской трубки на фланец',
            'ploskoy_trubki_na_nippel_gayki': 'плоской трубки на ниппель гайки',
        }
        title = f'Футеровка PTFE {suffix_title.get(slug, "")}'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_inner.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Внутренний экран для фторопластовых рукавов', breadcrumb=breadcrumb)
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
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', 'Внутренние экраны'),]
        suffix_title = {
            'antistaticheskaya_prisadka_ploskaya': 'антистатическая присадка плоская',
            'antistaticheskaya_prisadka_gofrirovannaya': 'антистатическая присадка гофрированная',
        }
        title = f'Внутренний экран: {suffix_title.get(slug, "")}'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_outside.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Наружная оболочка для фторопластовых рукавов', breadcrumb=breadcrumb)
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
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', 'Наружная оболочка'),]
        suffix_title = {
            'termochekhol': 'термочехол',
            'rezinovaya_obolochka': 'резиновая оболочка',
            'pruzhina': 'пружина',
            'ploskaya_trubka_v_metallorukave_v_opletke': 'плоская трубка в металлорукаве в оплетке',
            'gofrirovannaya_trubka_v_metallorukave_v_opletke': 'гофрированная трубка в металлорукаве в оплетке',
        }
        title = f'Наружная оболочка: {suffix_title.get(slug, "")}'
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Производство изделий на заказ')
        return {**context, **c_def}


class EngineeringAccessoriesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_accessories.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('engineering', 'Производство изделий на заказ'),]
        c_def = self.get_user_context(
            title='Технологическая оснастка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringTestView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_test.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('engineering', 'Производство изделий на заказ'),]
        c_def = self.get_user_context(
            title='Испытания на герметичность и прочность', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PrivacyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/privacy.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Политика конфиденциальности')
        return {**context, **c_def}


class WorkspaceFiltersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/workspace_filters.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Рабочие среды фильтров и агрегатов')
        return {**context, **c_def}


class FittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/fittings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Резьбовая арматура')
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
        breadcrumb = [('fittings', 'Резьбовая арматура'),]
        c_def = self.get_user_context(
            title='Резьбовая арматура', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CompositesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/composite.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Композитные рукава')
        return {**context, **c_def}


class CompositeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'composite_slug'

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
        breadcrumb = [('composite', 'Композитные рукава'),]
        c_def = self.get_user_context(
            title=f'Композитный рукав {slug}', breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlangesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/flanges.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Фланцевые соединения')
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
        breadcrumb = [('flanges', 'Фланцевые соединения'),]
        c_def = self.get_user_context(
            title='Фланцевое соединение', breadcrumb=breadcrumb)
        return {**context, **c_def}


class QuickReleaseCouplingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quick-release-coupling.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Быстроразъемные соединения')
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
        breadcrumb = [('quick-release-coupling',
                       'Быстроразъемные соединения'),]
        c_def = self.get_user_context(
            title='Быстроразъемное соединение', breadcrumb=breadcrumb)
        return {**context, **c_def}
