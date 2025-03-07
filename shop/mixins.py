from django.conf import settings
from shop import services


user_menu = {'Войти': 'login',
             'Регистрация': 'registration', 'Выйти': 'logout'}
main_menu = {'Главная': 'home', 'О нас': 'about-us',
             'Часто задаваемые вопросы': 'faq', 'Обратная связь': 'contact'}


class DataMixin:
    def get_user_context(self, **kwargs) -> dict:
        context = kwargs
        context_main_menu = main_menu.copy()
        context_user_menu = user_menu.copy()

        context['company_name'] = settings.COMPANY_NAME
        context['company_name_short'] = settings.COMPANY_NAME_SHORT
        context['company_email'] = settings.COMPANY_EMAIL
        context['company_address'] = settings.COMPANY_ADDRESS
        context['DEBUG'] = settings.DEBUG
        context['EXCESS_STOCK_OF_GOODS'] = settings.EXCESS_STOCK_OF_GOODS
        context['show_feedback'] = self.show_feedback_form()

        if 'breadcrumb' not in context:
            context['breadcrumb'] = []

        if 'title' not in context:
            context['title'] = settings.COMPANY_NAME

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
        context['categories'] = context['categories'][0][2] # это костыль что бы исключить категорию самого верхнего уровня, хотя она нужна, это все фильтры, в будущем надо убрать
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
