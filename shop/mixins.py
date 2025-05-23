from django.conf import settings
from shop import services
from rzmr import utils


user_menu = {'Войти': 'login',
             'Регистрация': 'registration', 'Выйти': 'logout'}
main_menu = {'Главная': 'home', 'О нас': 'about-us',
             'Часто задаваемые вопросы': 'faq', 'Обратная связь': 'contact'}


class DataMixin:
    def get_user_context(self, **kwargs) -> dict:
        context = kwargs
        context_main_menu = main_menu.copy()
        context_user_menu = user_menu.copy()

        subdomain = self.get_subdomain()

        context['author'] = settings.AUTHOR
        context['publisher_email'] = settings.PUBLISHER_EMAIL
        context['publisher_url'] = settings.PUBLISHER_URL

        context['company_micromarkup'] = settings.COMPANY_MICROMARKUP
        context['company_name'] = settings.COMPANY_NAME
        context['company_name_short'] = settings.COMPANY_NAME_SHORT
        context['company_email'] = settings.COMPANY_EMAIL
        context['hosts_and_cities'] = self.get_hosts_and_cities()

        context['EXCESS_STOCK_OF_GOODS'] = settings.EXCESS_STOCK_OF_GOODS
        context['show_feedback'] = self.show_feedback_form()
        context['company_address'] = self.get_company_address(subdomain)
        context['city_pre'], context['city_location'] = self.get_client_city(
            subdomain)
        context['company_phone'] = self.get_company_phone(subdomain)

        if 'breadcrumb' not in context:
            context['breadcrumb'] = []

        if 'title' not in context:
            context['title'] = settings.COMPANY_NAME

        if 'description' not in context:
            context['description'] = 'Производство метталорукавов, фильтров, фторопластовых рукавов, онлайн конструктор и продажа изделий'

        if self.request.user.is_anonymous:
            self.request.session['sessionid'] = self.request.session.session_key

        if not self.request.user.is_authenticated:
            context_main_menu.pop('Обратная связь')
            context_user_menu.pop('Выйти')
        elif not self.request.user.is_staff:
            context_user_menu[self.request.user.email] = 'profile'
            context_user_menu.pop('Войти')
            context_user_menu.pop('Регистрация')
        else:
            context_user_menu[self.request.user.email] = 'profile'
            context_user_menu.pop('Войти')
            context_user_menu.pop('Регистрация')

        context['user_menu'] = context_user_menu
        context['main_menu'] = context_main_menu
        context['categories'] = services.get_categories()
        # это костыль что бы исключить категорию самого верхнего уровня, хотя она нужна, это все фильтры, в будущем надо убрать
        context['categories'] = context['categories'][0][2]
        context['currencies'] = services.get_currencies()
        return context

    def show_feedback_form(self) -> bool:
        show_feedback = True
        elements = ('shop', 'constructor', 'login', 'registration',)
        current_path = self.request.path

        if current_path == '/':
            show_feedback = False
        elif any(e for e in elements if e in current_path):
            show_feedback = False

        return show_feedback

    # Возвращает город пользователя выбранный им вручную или определенный по базе GeoIP в предложном и именительном падеже
    def get_client_city(self, subdomain: str) -> tuple[str, str]:
        city_pre = ''
        city_location = ''

        company_cities = settings.COMPANY_CITIES
        company_cities_pre = settings.COMPANY_CITIES_PRE
        city_location = company_cities.get(subdomain, '')
        city_pre = company_cities_pre.get(subdomain, 'вашем городе')

        # if city_location:
        #     city_pre = utils.get_word_loct(city_location).title()

        if not city_location:
            ip = self.get_client_ip()
            city_location = utils.get_geo_city_name(ip)

        if not city_location:
            city_location = 'ваш город'

        return city_pre, city_location

    def get_hosts_and_cities(self) -> dict:
        company_cities = settings.COMPANY_CITIES
        company_host = settings.COMPANY_HOST
        hosts_and_cities = {}
        full_path = self.request.get_full_path()

        for prefix, city in company_cities.items():
            if prefix:
                url = f'https://{prefix}.{company_host}{full_path}'
            else:
                url = f'https://{company_host}{full_path}'

            hosts_and_cities[city] = url

        return hosts_and_cities

    def get_company_address(self, subdomain: str) -> str:
        company_addresses = settings.COMPANY_ADDRESSES
        address = company_addresses.get(subdomain, settings.COMPANY_ADDRESS)

        return address

    def get_company_phone(self, subdomain: str) -> str:
        company_phones = settings.COMPANY_PHONES
        phone = company_phones.get(subdomain, settings.COMPANY_PHONE)

        return phone

    def get_subdomain(self) -> str:
        host = self.request.get_host()
        subdomain = host.replace('www.', '').replace(
            settings.COMPANY_HOST, '').replace('.', '')

        return subdomain

    def get_client_ip(self) -> str:
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR', '0.0.0.0')

        return ip
