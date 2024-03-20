from urllib import request, error
import json


def get_request_to_1C(url_request: str) -> str:
    response = '{}'

    if not url_request:
        return response

    with request.urlopen(url_request) as resp:
        response = resp.read().decode('utf-8')

    return response


def post_request_to_1C(url_request: str, data_request: dict) -> str:
    pass


def get_types() -> list[tuple[str, str]]:
    types = []
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListProductType'
    response = get_request_to_1C(url_request)

    types = json.loads(response).get('list', [])

    if types:
        types = [(elem.get('Code', ''), elem.get('Value', ''))
                    for elem in types]

    return types


def get_diameters() -> list[tuple[str, str]]:
    diameters = []
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListDiameters'
    response = get_request_to_1C(url_request)

    diameters = json.loads(response).get('list', [])

    if diameters:
        diameters = [(elem.get('Code', ''), elem.get('Value', ''))
                    for elem in diameters]

    return diameters


def get_pressures() -> list[tuple[str, str]]:
    pressures = []
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListPressures'
    response = get_request_to_1C(url_request)

    pressures = json.loads(response).get('list', [])

    if pressures:
        pressures = [(elem.get('Code', ''), elem.get('Value', ''))
                    for elem in pressures]

    return pressures


def get_lengths() -> list[tuple[str, str]]:
    lengths = []
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListLengthsHoses'
    response = get_request_to_1C(url_request)

    lengths = json.loads(response).get('list', [])

    if lengths:
        lengths = [(elem.get('Code', ''), elem.get('Value', ''))
                    for elem in lengths]

    return lengths


# получает фиттинги в форме списка кортежей пригодного для поля select формы
def get_fittings() -> list[tuple[str, str]]:
    fittings = []
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=getListGroupsEndFittings'
    response = get_request_to_1C(url_request)

    fittings = json.loads(response).get('list', [])

    if fittings:
        fittings = [(elem.get('Code', ''), elem.get('Value', ''))
                    for elem in fittings]

    return fittings
