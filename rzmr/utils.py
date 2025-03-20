from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
import pymorphy3


MORPH = pymorphy3.MorphAnalyzer()
GEO_INFO = GeoIP2()


# преобразует слово из именительного падежа в предложный падеж. Москва -> Москве
def get_word_loct(word: str) -> str:
    word_parse = MORPH.parse(word)[0]
    word_loct = word_parse.inflect({'loct'}).word
    return word_loct


def get_geo_country(ip: str) -> dict:
    country_info = GEO_INFO.country(ip)
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
    return city_name
