import pytest
import requests
from urllib.parse import urljoin
import logging

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)-70s (%(filename)s:%(lineno)d)',
                    level=logging.DEBUG, filename='logs_redirects.txt')
testdata = [1, 5, 10]


@pytest.mark.parametrize("redirects_counter", testdata)
def test_redirects(redirects_counter):
    logging.info(f"------ Starting test with redirects_counter = {redirects_counter} ------")
    host = 'https://httpbin.org/'
    endpoint = f'redirect/{redirects_counter}'
    final_url = urljoin(host, endpoint)
    response = requests.get(final_url)
    assert redirects_counter == len(response.history)
