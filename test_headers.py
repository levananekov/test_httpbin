import pytest
import requests
import json
from urllib.parse import urljoin
import logging

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)-70s (%(filename)s:%(lineno)d)',
                    level=logging.DEBUG, filename='logs_headers.txt')
headers_valid = {'User-Agent': 'Random'}
headers_invalid = {'Host': 'ya.ru'}
testdata = [
    (True, headers_valid),
    (False, headers_invalid),
]


@pytest.mark.parametrize("response_success, headers", testdata)
def test_headers(response_success, headers):
    logging.info(f"------ Starting test with headers = {headers}, expecting response.ok == {response_success} ------")
    host = 'https://httpbin.org'
    endpoint = 'headers'
    final_url = urljoin(host, endpoint)
    response = requests.get(final_url, headers=headers)
    assert response.ok == response_success
    if response.ok:
        response_dict = json.loads(response.text)
        headers_from_response = response_dict['headers']
        for key in headers.keys():
            assert headers[key] == headers_from_response[key]
