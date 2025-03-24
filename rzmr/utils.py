from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
import pymorphy3
import json


MORPH = pymorphy3.MorphAnalyzer()
GEO_INFO = GeoIP2()


def load_ru_cities() -> None:
    if settings.CITIES_RU:
        return

    ru_cities = {}
    json_file = 'russia-cities.json'

    with open(json_file, 'r') as f:
        try:
            cities_info = json.loads(f.read())
        except json.JSONDecodeError:
            pass

    if not cities_info:
        return

    for city_info in cities_info:
        eng_name = city_info.get('label', 'nolabel').title()
        ru_name = city_info.get('name', 'noname')
        ru_cities[eng_name] = ru_name

    if ru_cities:
        settings.CITIES_RU = ru_cities


# преобразует слово из именительного падежа в предложный падеж. Москва -> Москве
def get_word_loct(word: str) -> str:
    word_parse = MORPH.parse(word)[0]
    word_loct = word_parse.inflect({'loct'}).word
    return word_loct


def get_geo_country(ip: str) -> dict:
    country_info = {}

    try:
        country_info = GEO_INFO.country(ip)
    except AddressNotFoundError:
        pass

    return country_info


def get_geo_city(ip: str) -> dict:
    city_info = {}

    try:
        city_info = GEO_INFO.city(ip)
    except AddressNotFoundError:
        pass

    return city_info


def get_geo_country_name(ip: str) -> str:
    country_info = get_geo_country(ip)
    country_name = country_info.get('country_name', '')
    return country_name


def get_geo_city_name(ip: str) -> str:
    city_info = get_geo_city(ip)
    city_name = city_info.get('city', '')
    country_name = city_info.get('country_name', '')
    print(city_info)

    if city_name is None:
        city_name = ''

    if country_name == 'Russian Federation':
        city_name_ru = settings.CITIES_RU.get(city_name, '')

        if city_name_ru:
            city_name = city_name_ru

    return city_name
