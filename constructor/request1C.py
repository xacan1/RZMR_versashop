from urllib import request


def get_request_to_1C(url_request: str) -> str:
    response = '{}'

    if not url_request:
        return response

    with request.urlopen(url_request) as resp:
        response = resp.read().decode('utf-8')

    return response
