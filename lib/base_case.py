import json.decoder

from requests import Response


class BaseCase:
    def get_cooclie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'Error. Cookie is not in response'
        return response.cookies[cookie_name]

    def get_heder(self, response: Response, headers_name):
        assert headers_name in response.headers, f'Error. Headers is not in response'
        return response.headers_name[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, 'Erro. JSON'

        assert name in response_as_dict, 'Error. Json 2'

        return response_as_dict[name]