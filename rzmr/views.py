from typing import Any, Dict, List
from django.views.generic import FormView
from rzmr.forms import *
from shop.mixins import DataMixin
from django.http import HttpRequest, HttpResponse, FileResponse
from django.utils.translation import gettext_lazy as _
from pathlib import Path


class RobotView(DataMixin, FormView):
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
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

    def form_valid(self, form: Any) -> HttpResponse:
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Company'))
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=_('Quality and certification system'))
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Our clients'))
        return {**context, **c_def}


class ForSuppliersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/for-suppliers.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поставщикам')
        return {**context, **c_def}


class VacanciesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/vacancies.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Career'))
        return {**context, **c_def}


class ContactsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/contacts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return {**context, **c_def}


class MetalhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Metal hoses'))
        return {**context, **c_def}


class MetalhosesFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title=_('Fittings'))
        return {**context, **c_def}


class MetalhosesCorrugationView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationStandartnayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation_standartnaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ средней гибкости', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationPovyshennoyGibkostiView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation_povishennoy_gibkosti.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ повышенной гибкости', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationTyazhelayaSeriyaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation_tyazhelaya_seriya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ тяжелой серии до 400 кгс/см2', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationSpiralnayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation_spiralnaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Спиральный гофрированный металлорукав РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesCorrugationDvuhsloinayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_corrugation_dvukhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Двухслойный гофрированный металлорукав РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(title='Оплётка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidOdnosloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid_odnosloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Стальная однослойная нержавеющая оплетка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidDvukhsloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid_dvukhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Двухслойная оплётка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesBraidTrekhsloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_braid_trekhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Трёхслойная оплётка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerTrubnyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner_trubnyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Трубный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerValtsovannyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner_valtsovannyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Вальцованный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerOpletochnyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner_opletochnyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Оплёточный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInnerPTFEView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_inner_PTFE.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(title='PTFE', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsideView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Наружная оплетка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsideTermochekholView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside_termochekhol.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Термочехол для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsideTermorukavView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside_termorukav.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Терморукав для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsideRezinovayaObolochkaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside_rezinovaya_obolochka.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Резиновая оболочка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsidePruzhinaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside_pruzhina.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Пружина для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesOutsidePletenkaMednayaLuzhenayaPmlView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_outside_pletenka_mednaya_luzhenaya_pml.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Плетенка медная луженая (ПМЛ)', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_recommendations.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Рекомендации по выбору металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_installation_safety.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Монтаж и безопасность металлорукавов серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class StandartsRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_standarts_rgm.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', _('Metal hoses')),]
        c_def = self.get_user_context(
            title='Стандарты качества на металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('PTFE Metal hoses'))
        return {**context, **c_def}


class PTFERecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_recommendations.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Рекомендации по измерениям и соответствиям стандартам', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEInstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_installation_safety.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Монтаж и безопасность фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Концевая арматура для фторопластовых рукавов серии РФ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEStandartsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_standarts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Стандарты качества на фторопластовых рукавов серии РФП, РФГ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Трубки для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_pipe_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-pipes', 'Трубка'),]
        c_def = self.get_user_context(
            title='Трубка для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFELinersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_liner.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Футеровки PTFE', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFELinerView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_liner_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-liners', 'Футеровка PTFE'),]
        c_def = self.get_user_context(
            title='Футеровка PTFE', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEInnersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_inner.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Внутренний экран для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEInnerView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_inner_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-inners', 'Внутренний экран'),]
        c_def = self.get_user_context(
            title='Внутренний экран:', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEOutsidesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_outside.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),]
        c_def = self.get_user_context(
            title='Наружная оболочка для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEOutsideView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'ptfe_outside_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe-hoses', _('PTFE Metal hoses')),
                      ('ptfe-outsides', 'Наружная оболочка'),]
        c_def = self.get_user_context(
            title='Наружная оболочка:', breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Производство изделий на заказ')
        return {**context, **c_def}


class EngineeringAccessoriesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_accessories.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('engineering', 'Производство изделий на заказ'),]
        c_def = self.get_user_context(
            title='Технологическая оснастка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class EngineeringTestView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/engineering_test.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('engineering', 'Производство изделий на заказ'),]
        c_def = self.get_user_context(
            title='Испытания на герметичность и прочность', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PrivacyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/privacy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Политика конфиденциальности')
        return {**context, **c_def}


class WorkspaceFiltersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/workspace_filters.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Рабочие среды фильтров и агрегатов')
        return {**context, **c_def}


class FittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Резьбовая арматура')
        return {**context, **c_def}


class FittingView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'fitting_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('fittings', 'Резьбовая арматура'),]
        c_def = self.get_user_context(
            title='Резьбовая арматура', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CompositesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/composite.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Композитные рукава')
        return {**context, **c_def}


class CompositeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'composite_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, '')
        breadcrumb = [('composite', 'Композитные рукава'),]
        c_def = self.get_user_context(
            title=f'Композитный рукав {slug}', breadcrumb=breadcrumb)
        return {**context, **c_def}


class FlangesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/flanges.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Фланцевые соединения')
        return {**context, **c_def}


class FlangeView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'flange_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('flanges', 'Фланцевые соединения'),]
        c_def = self.get_user_context(
            title='Фланцевое соединение', breadcrumb=breadcrumb)
        return {**context, **c_def}


class QuickReleaseCouplingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quick-release-coupling.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Быстроразъемные соединения')
        return {**context, **c_def}


class QuickReleaseCouplingView(DataMixin, FormView):
    form_class = SimpleForm
    slug_url_kwarg = 'coupling_slug'

    def get_template_names(self) -> List[str]:
        slug = self.kwargs.get(self.slug_url_kwarg, '')

        if not slug:
            return super().get_template_names()

        template_names = []
        template_names.append(f'rzmr/{slug}.html')

        return template_names

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('quick-release-coupling',
                       'Быстроразъемные соединения'),]
        c_def = self.get_user_context(
            title='Быстроразъемное соединение', breadcrumb=breadcrumb)
        return {**context, **c_def}
