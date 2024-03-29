from django.urls import path
from rzmr.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('robot.txt/', RobotView.as_view()),
    path('about/', AboutView.as_view(), name='about'),
    path('about/quality/', QualityView.as_view(), name='quality'),
    path('about/our-customer/', OurCustomerView.as_view(), name='our-customer'),
    path('about/for-suppliers/', ForSuppliersView.as_view(), name='for-suppliers'),
    path('about/vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('about/contacts/', ContactsView.as_view(), name='contacts'),
    path('metalhoses/', MetalhosesView.as_view(), name='metalhoses'),
    path('metalhoses/fittings/', MetalhosesFittingsView.as_view(),
         name='metalhoses-fittings'),
    path('metalhoses/corrugation/', MetalhosesCorrugationView.as_view(),
         name='metalhoses-corrugation'),
    path('metalhoses/corrugation/standartnaya/', MetalhosesCorrugationStandartnayaView.as_view(),
         name='metalhoses-corrugation-standartnaya'),
    path('metalhoses/corrugation/povishennoy-gibkosti/', MetalhosesCorrugationPovyshennoyGibkostiView.as_view(),
         name='metalhoses-corrugation-povishennoy_gibkosti'),
    path('metalhoses/corrugation/tyazhelaya-seriya/', MetalhosesCorrugationTyazhelayaSeriyaView.as_view(),
         name='metalhoses-corrugation-tyazhelaya_seriya'),
    path('metalhoses/corrugation/spiralnaya/', MetalhosesCorrugationSpiralnayaView.as_view(),
         name='metalhoses-corrugation-spiralnaya'),
    path('metalhoses/corrugation/dvukhsloynaya/', MetalhosesCorrugationDvuhsloinayaView.as_view(),
         name='metalhoses-corrugation-dvukhsloynaya'),
    path('metalhoses/braid/', MetalhosesBraidView.as_view(),
         name='metalhoses-braid'),
    path('metalhoses/braid/odnosloynaya/', MetalhosesBraidOdnosloynayaView.as_view(),
         name='metalhoses-braid-odnosloynaya'),
    path('metalhoses/braid/dvukhsloynaya/', MetalhosesBraidDvukhsloynayaView.as_view(),
         name='metalhoses-braid-dvukhsloynaya'),
    path('metalhoses/braid/trekhsloynaya/', MetalhosesBraidTrekhsloynayaView.as_view(),
         name='metalhoses-braid-trekhsloynaya'),
    path('metalhoses/inner/', MetalhosesInnerView.as_view(),
         name='metalhoses-inner'),
    path('metalhoses/inner/trubnyy/', MetalhosesInnerTrubnyyView.as_view(),
         name='metalhoses-inner-trubnyy'),
    path('metalhoses/inner/valtsovannyy/', MetalhosesInnerValtsovannyyView.as_view(),
         name='metalhoses-inner-valtsovannyy'),
    path('metalhoses/inner/opletochnyy/', MetalhosesInnerOpletochnyyView.as_view(),
         name='metalhoses-inner-opletochnyy'),
    path('metalhoses/inner/ptfe/', MetalhosesInnerPTFEView.as_view(),
         name='metalhoses-inner-ptfe'),
    path('metalhoses/outside/', MetalhosesOutsideView.as_view(),
         name='metalhoses-outside'),
    path('metalhoses/outside/termochekhol/', MetalhosesOutsideTermochekholView.as_view(),
         name='metalhoses-outside-termochekhol'),
    path('metalhoses/outside/termorukav/', MetalhosesOutsideTermorukavView.as_view(),
         name='metalhoses-outside-termorukav'),
    path('metalhoses/outside/rezinovaya-obolochka/', MetalhosesOutsideRezinovayaObolochkaView.as_view(),
         name='metalhoses-outside-rezinovaya_obolochka'),
    path('metalhoses/outside/pruzhina/', MetalhosesOutsidePruzhinaView.as_view(),
         name='metalhoses-outside-pruzhina'),
    path('metalhoses/outside/pletenka-mednaya-luzhenaya-pml/', MetalhosesOutsidePletenkaMednayaLuzhenayaPmlView.as_view(),
         name='metalhoses-outside-pletenka_mednaya_luzhenaya_pml'),
    path('metalhoses/recommendations/', MetalhosesRecommendationsView.as_view(),
         name='metalhoses-recommendations'),
    path('metalhoses/installation/', InstallationSafetyView.as_view(),
         name='metalhoses-installation'),
    path('metalhoses/standarts/', StandartsRGMView.as_view(),
         name='metalhoses-standarts-grm'),
    path('ptfe/', PTFEView.as_view(), name='ptfe'),
    path('ptfe/recommendations/', PTFERecommendationsView.as_view(),
         name='ptfe-recommendations'),
    path('ptfe/fittings/', PTFEFittingsView.as_view(), name='ptfe-fittings'),
    path('ptfe/standarts/', PTFEStandartsView.as_view(), name='ptfe-standarts'),
    path('ptfe/pipe/', PTFEPipeView.as_view(), name='ptfe-pipe'),
    path('ptfe/pipe/ploskaya-standartnoe-ispolnenie/', PTFEPloskayaStandartnoeIspolnenieView.as_view(),
         name='ptfe-ploskaya-standartnoe-ispolnenie'),
    path('ptfe/pipe/ploskaya-tolstostennaya/', PTFEPloskayaTolstostennayaView.as_view(),
         name='ptfe-ploskaya-tolstostennaya'),
    path('ptfe/pipe/gofrirovannaya-standartnoe-ispolnenie/', PTFEGofrirovannayaStandartnoeIspolnenieView.as_view(),
         name='ptfe-gofrirovannaya-standartnoe-ispolnenie'),
    path('ptfe/pipe/gofrirovannaya-tolstostennaya/', PTFEGofrirovannayaTolstostennayaView.as_view(),
         name='ptfe-gofrirovannaya-tolstostennaya'),
    path('ptfe/liner/', PTFELinerView.as_view(), name='ptfe-liner'),
    path('ptfe/liner/ptfe-futerovka-ploskoy-trubki-na-flanets/', PTFEFuterovkaPloskoyTrubkiNaFlanetsView.as_view(),
         name='ptfe-futerovka-ploskoy-trubki-na-flanets'),
    path('ptfe/liner/ptfe-futerovka-gofrirovannoy-trubki-na-flanets/', PTFEFuterovkaGofrirovannoyTrubkiNaFlanetsView.as_view(),
         name='ptfe-futerovka-gofrirovannoy-trubki-na-flanets'),
    path('ptfe/liner/ptfe-futerovka-ploskoy-trubki-na-nippel-gayki/', PTFEFuterovkaPloskoyTrubkiNaNippelGaykiView.as_view(),
         name='ptfe-futerovka-ploskoy-trubki-na-nippel-gayki'),
    path('ptfe/inner/', PTFEInnerView.as_view(), name='ptfe-inner'),
    path('ptfe/inner/antistaticheskaya-prisadka-ploskaya/', PTFEAntistaticheskayaPrisadkaPloskayaView.as_view(),
         name='ptfe-antistaticheskaya-prisadka-ploskaya'),
    path('ptfe/inner/antistaticheskaya-prisadka-gofrirovannaya/', PTFEAntistaticheskayaPrisadkaGofrirovannayaView.as_view(),
         name='ptfe-antistaticheskaya-prisadka-gofrirovannaya'),
    path('ptfe/outside/', PTFEOutsideView.as_view(), name='ptfe-outside'),
    path('ptfe/outside/termochekhol/', PTFEOutsideTermochekholView.as_view(),
         name='ptfe-outside-termochekhol'),
    path('ptfe/outside/rezinovaya-obolochka/', PTFEOutsideRezinovayaObolochkaView.as_view(),
         name='ptfe-outside-rezinovaya-obolochka'),
    path('ptfe/outside/pruzhina/', PTFEOutsidePruzhinaView.as_view(),
         name='ptfe-outside-pruzhina'),
    path('ptfe/outside/ploskaya-trubka-v-metallorukave-v-opletke/', PTFEOutsidePloskayaTrubkaVMetallorukaveVOpletkeView.as_view(),
         name='ptfe-outside-ploskaya-trubka-v-metallorukave-v-opletke'),
    path('ptfe/outside/gofrirovannaya-trubka-v-metallorukave-v-opletke/', PTFEOutsideGofrirovannayaTrubkaVMetallorukaveVOpletkeView.as_view(),
         name='ptfe-outside-gofrirovannaya-trubka-v-metallorukave-v-opletke'),
    path('engineering/', EngineeringView.as_view(), name='engineering'),
    path('engineering/accessories/', EngineeringAccessoriesView.as_view(),
         name='engineering-accessories'),
    path('engineering/test/', EngineeringTestView.as_view(),
         name='engineering-test'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]
