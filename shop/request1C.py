from urllib import request, error
from typing import Union
import json


def get_request_to_1C(url_request: str) -> Union[str, bytes]:
    response = '{}'

    if not url_request:
        return response

    try:
        with request.urlopen(url_request) as resp:
            if resp.headers.get('IsFile', '0') == '0':
                response = resp.read().decode('utf-8')
            else:
                response = resp.read()

    except error.URLError:
        return response
    finally:
        return response


def post_request_to_1C(url_request: str, data_request: bytes) -> str:
    response = '{}'

    if not url_request:
        return response

    req = request.Request(url=url_request, data=data_request, method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        with request.urlopen(req) as resp:
            response = resp.read().decode('utf-8')

    except error.URLError:
        return response
    finally:
        return response


# после создания Заказа или События в 1С вернем номер документа для записи в базу сайта как external_code
def create_order_in_1C(data_request: dict) -> str:
    data = json.dumps(data_request).encode('utf-8')
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=createOrder'

    response = post_request_to_1C(url_request, data)

    data_order = json.loads(response)
    number_order = data_order.get('Code', '0')

    return number_order
