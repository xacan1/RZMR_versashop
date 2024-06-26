from shop.models import Product
from constructor import request1C
import json


def find_product_on_site(external_code: str) -> tuple[int, str]:
    product_pk = 0
    product_name = ''
    queryset = Product.objects.filter(external_code=external_code)

    if queryset.exists():
        product_pk = queryset[0].pk
        product_name = queryset[0].name

    return product_pk, product_name


# response_data - строка JSON с кодом сгенерированного товара из 1С
def load_new_product_from_1C(response_data: str) -> str:
    external_code = json.loads(response_data).get('Code', '0')

    if external_code == '0':
        response_data = json.dumps({'id': 0, 'Value': 'Not created'})
        return response_data

    # сначала поищу сгенерированный в 1С товар на сайте
    product_pk, product_name = find_product_on_site(external_code)

    if product_pk:
        response_data = json.dumps({'id': product_pk, 'Value': product_name})
        return response_data

    # если не найден, то его надо выгрузить из 1С на сайт
    response_data = request1C.upload_product_from_1C(external_code)

    return response_data
