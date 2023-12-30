from typing import Any, Dict, List
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rzmr.forms import *
from shop.mixins import DataMixin


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
        c_def = self.get_user_context(title='О заводе')
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Система качества и сертификации')
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши клиенты')
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
        c_def = self.get_user_context(title='Вакансии')
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
        c_def = self.get_user_context(title='Металлорукава')
        return {**context, **c_def}


class MetalhosesFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Концевая арматура для металлорукавов')
        return {**context, **c_def}


class CorrugationView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CorrugationStandartnayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_standartnaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ средней гибкости', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CorrugationPovyshennoyGibkostiView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_povishennoy_gibkosti.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ повышенной гибкости', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CorrugationTyazhelayaSeriyaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_tyazhelaya_seriya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ тяжелой серии до 400 кгс/см2', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CorrugationSpiralnayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_spiralnaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Спиральный гофрированный металлорукав РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class CorrugationDvuhsloinayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_dvukhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-corrugation', 'Гофра')]
        c_def = self.get_user_context(
            title='Двухслойный гофрированный металлорукав РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class BraidView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/braid.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(title='Оплётка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class BraidOdnosloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/braid_odnosloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Стальная однослойная нержавеющая оплетка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class BraidDvukhsloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/braid_dvukhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Двухслойная оплётка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class BraidTrekhsloynayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/braid_trekhsloynaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-braid', 'Оплётка')]
        c_def = self.get_user_context(
            title='Трёхслойная оплётка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InnerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/inner.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InnerTrubnyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/inner_trubnyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Трубный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InnerValtsovannyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/inner_valtsovannyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Вальцованный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InnerOpletochnyyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/inner_opletochnyy.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(
            title='Оплёточный внутренний экран', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InnerPTFEView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/inner_PTFE.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-inner', 'Внутренний экран')]
        c_def = self.get_user_context(title='PTFE', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsideView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Наружная оплетка', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsideTermochekholView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside_termochekhol.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Термочехол для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsideTermorukavView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside_termorukav.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Терморукав для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsideRezinovayaObolochkaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside_rezinovaya_obolochka.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Резиновая оболочка для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsidePruzhinaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside_pruzhina.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Пружина для металлорукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class OutsidePletenkaMednayaLuzhenayaPmlView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/outside_pletenka_mednaya_luzhenaya_pml.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),
                      ('metalhoses-outside', 'Наружная оплетка')]
        c_def = self.get_user_context(
            title='Плетенка медная луженая (ПМЛ)', breadcrumb=breadcrumb)
        return {**context, **c_def}


class MetalhosesRecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_recommendations.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Рекомендации по выбору металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class InstallationSafetyView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_installation_safety.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Монтаж и безопасность металлорукавов серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class StandartsRGMView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses_standarts_rgm.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('metalhoses', 'Металлорукава'),]
        c_def = self.get_user_context(
            title='Стандарты качества на металлорукава серии РГМ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Фторопластовые рукава')
        return {**context, **c_def}


class PTFERecommendationsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_recommendations.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),]
        c_def = self.get_user_context(
            title='Рекомендации по измерениям и соответствиям стандартам', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),]
        c_def = self.get_user_context(
            title='Концевая арматура для фторопластовых рукавов серии РФ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEStandartsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_standarts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),]
        c_def = self.get_user_context(
            title='Стандарты качества на фторопластовых рукавов серии РФП, РФГ', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPipeView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', ' Фторопластовые рукава'),]
        c_def = self.get_user_context(
            title='Трубка для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPloskayaStandartnoeIspolnenieView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe_ploskaya_standartnoe_ispolnenie.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-pipe', 'Трубка')]
        c_def = self.get_user_context(
            title='Плоская стандартное исполнение', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEPloskayaTolstostennayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe_ploskaya_tolstostennaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-pipe', 'Трубка')]
        c_def = self.get_user_context(
            title='Плоская толстостенная трубка для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEGofrirovannayaStandartnoeIspolnenieView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe_gofrirovannaya_standartnoe_ispolnenie.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-pipe', 'Трубка')]
        c_def = self.get_user_context(
            title='Гофрированная стандартное исполнение', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEGofrirovannayaTolstostennayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_pipe_gofrirovannaya_tolstostennaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-pipe', 'Трубка')]
        c_def = self.get_user_context(
            title='Гофрированная толстостенная трубка для фторопластовых рукавов', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFELinerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_liner.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),]
        c_def = self.get_user_context(
            title='Футеровка PTFE', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEFuterovkaPloskoyTrubkiNaFlanetsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_futerovka_ploskoy_trubki_na_flanets.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-liner', 'Футеровка PTFE')]
        c_def = self.get_user_context(
            title='PTFE футеровка плоской трубки на фланец', breadcrumb=breadcrumb)
        return {**context, **c_def}
    

class PTFEFuterovkaGofrirovannoyTrubkiNaFlanetsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_futerovka_gofrirovannoy_trubki_na_flanets.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-liner', 'Футеровка PTFE')]
        c_def = self.get_user_context(
            title='PTFE футеровка гофрированной трубки на фланец', breadcrumb=breadcrumb)
        return {**context, **c_def}


class PTFEFuterovkaPloskoyTrubkiNaNippelGaykiView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/ptfe_futerovka_ploskoy_trubki_na_nippel_gayki.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('ptfe', 'Фторопластовые рукава'),
                      ('ptfe-liner', 'Футеровка PTFE')]
        c_def = self.get_user_context(
            title='PTFE футеровка плоской трубки на ниппель гайки', breadcrumb=breadcrumb)
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
