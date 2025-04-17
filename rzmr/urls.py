from django.urls import path
from rzmr.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('robots.txt', RobotsView.as_view()),
    # path('select_city/', RedirectToCityView.as_view(), name='redirect-to-city'),
    path('request-phone-call/', RequestPhoneCallView.as_view(), name='request-phone-call'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('about/', AboutView.as_view(), name='about'),
    path('about/quality/', QualityView.as_view(), name='quality'),
    path('about/our-customer/', OurCustomerView.as_view(), name='our-customer'),
    path('about/for-suppliers/', ForSuppliersView.as_view(), name='for-suppliers'),
    path('about/vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('about/contacts/', ContactsView.as_view(), name='contacts'),
    path('about/spheres/', SpheresView.as_view(), name='spheres'),
    path('about/spheres/<slug:spheres_slug>/', SphereView.as_view(), name='sphere'),
    path('metalhoses/', MetalhosesView.as_view(), name='metalhoses'),
    path('metalhoses/fittings/', MetalhosesFittingsView.as_view(), name='metalhoses-fittings'),
    path('metalhoses/corrugation/', MetalhosesCorrugationsView.as_view(), name='metalhoses-corrugations'),
    path('metalhoses/corrugation/<slug:metalhoses_corrugation_slug>/', MetalhosesCorrugationView.as_view(), name='metalhoses-corrugation'),
    path('metalhoses/braid/', MetalhosesBraidsView.as_view(), name='metalhoses-braids'),
    path('metalhoses/braid/<slug:metalhoses_braid_slug>/', MetalhosesBraidView.as_view(), name='metalhoses-braid'),
    path('metalhoses/inner/', MetalhosesInnersView.as_view(), name='metalhoses-inners'),
    path('metalhoses/inner/<slug:metalhoses_inner_slug>/', MetalhosesInnerView.as_view(), name='metalhoses-inner'),
    path('metalhoses/outside/', MetalhosesOutsidesView.as_view(), name='metalhoses-outsides'),
    path('metalhoses/outside/<slug:metalhoses_outside_slug>/', MetalhosesOutsideView.as_view(), name='metalhoses-outside'),
    path('metalhoses/special/', MetalhosesSpecialView.as_view(), name='metalhoses-special'),
    path('metalhoses/recommendations/', MetalhosesRecommendationsView.as_view(), name='metalhoses-recommendations'),
    path('metalhoses/installation/', MetalhosesInstallationSafetyView.as_view(), name='metalhoses-installation'),
    path('metalhoses/standarts/', MetalhosesStandartsRGMView.as_view(), name='metalhoses-standarts-rgm'),
    path('metalhoses/hpress/', MetalhosesHpressRGMView.as_view(), name='metalhoses-hpress-rgm'),
    path('metalhoses/for-welding/', MetalhosesForWeldingView.as_view(), name='metalhoses-for-welding'),
    path('metalhoses/rgm/', MetalhosesRGMView.as_view(), name='metalhoses-rgm'),
    path('metalhoses/gibkie-truboprovody/', MetalhosesGibkieTruboprovodyView.as_view(), name='metalhoses-gibkie-truboprovody'),
    path('metalhoses/v-opletke/', MetalhosesVOpletkeView.as_view(), name='metalhoses-v-opletke'),
    path('gibkie-truboprovody/', FlexiblePipelinesView.as_view(), name='gibkie-truboprovody'),
    path('ptfe/', PTFEhosesView.as_view(), name='ptfe-hoses'),
    path('ptfe/gofrirovanniy/', PTFEhosesGofrirovanniyView.as_view(), name='ptfe-gofrirovanniy'),
    path('ptfe/recommendations/', PTFERecommendationsView.as_view(), name='ptfe-recommendations'),
    path('ptfe/installation/', PTFEInstallationSafetyView.as_view(), name='ptfe-installation'),
    path('ptfe/fittings/', PTFEFittingsView.as_view(), name='ptfe-fittings'),
    path('ptfe/standarts/', PTFEStandartsView.as_view(), name='ptfe-standarts'),
    path('ptfe/hpress/', HpressPTFEView.as_view(), name='ptfe-hpress'),
    path('ptfe/pipe/', PTFEPipesView.as_view(), name='ptfe-pipes'),
    path('ptfe/pipe/<slug:ptfe_pipe_slug>/', PTFEPipeView.as_view(), name='ptfe-pipe'),
    path('ptfe/braid/', PTFEBraidsView.as_view(), name='ptfe-braids'),
    path('ptfe/braid/<slug:ptfe_braid_slug>/', PTFEBraidView.as_view(), name='ptfe-braid'),
    path('ptfe/liner/', PTFELinersView.as_view(), name='ptfe-liners'),
    path('ptfe/liner/<slug:ptfe_liner_slug>/', PTFELinerView.as_view(), name='ptfe-liner'),
    path('ptfe/inner/', PTFEInnersView.as_view(), name='ptfe-inners'),
    path('ptfe/inner/<slug:ptfe_inner_slug>/', PTFEInnerView.as_view(), name='ptfe-inner'),
    path('ptfe/outside/', PTFEOutsidesView.as_view(), name='ptfe-outsides'),
    path('ptfe/outside/<slug:ptfe_outside_slug>/', PTFEOutsideView.as_view(), name='ptfe-outside'),
    path('engineering/', EngineeringView.as_view(), name='engineering'),
    path('engineering/accessories/', EngineeringAccessoriesView.as_view(), name='engineering-accessories'),
    path('engineering/test/', EngineeringTestView.as_view(), name='engineering-test'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('filters/workspace-filters/', WorkspaceFiltersView.as_view(), name='workspace-filters'),
    path('composite/', CompositesView.as_view(), name='composite'),
    path('composite/<slug:composite_slug>/', CompositeView.as_view(), name='composite'),
    path('fittings/', FittingsView.as_view(), name='fittings'),
    path('fittings/<slug:fitting_slug>/', FittingView.as_view(), name='fitting'),
    path('flanges/', FlangesView.as_view(), name='flanges'),
    path('flange/<slug:flange_slug>/', FlangeView.as_view(), name='flange'),
    path('quick-release-coupling/', QuickReleaseCouplingsView.as_view(), name='quick-release-coupling'),
    path('quick-release-coupling/<slug:coupling_slug>/', QuickReleaseCouplingView.as_view(), name='quick-release-coupling'),
]
