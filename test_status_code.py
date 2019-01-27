import pytest
import requests
from urllib.parse import urljoin
import logging

logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG, filename='logs_status_code.txt')
allow_redirects = False
testdata = [101, 102, 103, 122, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226,
            300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 404,
            405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418,
            421, 422, 423, 424, 425, 426, 428, 429, 431, 444, 449, 450, 451, 499,
            500, 501, 502, 503, 504, 505, 506, 507, 509, 510, 511]  # status code 100 always failed


@pytest.mark.parametrize("status_code", testdata)
def test_status_code(status_code):
    logging.info(f"------ Starting test with status code = {status_code} ------")
    host = 'https://httpbin.org'
    endpoint = f'status/{status_code}'
    final_url = urljoin(host, endpoint)
    response = requests.get(final_url, allow_redirects=False)
    assert response.status_code == status_code
