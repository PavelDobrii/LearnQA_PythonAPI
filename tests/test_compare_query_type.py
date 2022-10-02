import pytest
import requests


class TestCompareQueryType:

    method = [
        'POST',
        'GET',
        'PUT',
        'DELETE',
        'HEAD'
    ]

    @pytest.mark.parametrize('method', method)
    def test_compare_query_type(self, method):
        url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
        response = requests.request(method, url)

        print(response.request)
        print(method)
        print(method.upper())
        assert method in (response.request).__str__()

