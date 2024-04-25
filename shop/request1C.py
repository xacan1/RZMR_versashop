from urllib import request, error
import json


def post_request_to_1C(url_request: str, data_request: bytes) -> str:
    response = '{}'

    if not url_request:
        return response

    # return response

    req = request.Request(url=url_request, data=data_request, method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        with request.urlopen(req) as resp:
            response = resp.read().decode('utf-8')

    except error.URLError:
        return response
    finally:
        return response


def create_order_in_1C(data_request: dict) -> str:
    data = json.dumps(data_request).encode('utf-8')
    url_request = 'http://62.133.174.3:8081/UT_RZM/hs/api?metod=createOrder'

    response = post_request_to_1C(url_request, data)

    data_order = json.loads(response)
    number_order = data_order.get('Code', '0')

    return number_order
