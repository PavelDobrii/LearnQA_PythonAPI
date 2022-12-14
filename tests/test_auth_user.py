import pytest
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        url = 'https://playground.learnqa.ru/api/user/login'
        response = requests.post(url, data=data)

        self.auth_sid = self.get_cooclie(response, 'auth_sid')
        self.token = self.get_heder(response, 'x-csrf-token')
        self.user_id_from_auth_method = self.get_json_value(response, 'user_id')
        self.user_id = response.json()['user_id']

    def test_auth_user(self):
        url2 = 'https://playground.learnqa.ru/api/user/auth'
        response2 = requests.get(
            url2,
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid':  self.auth_sid},
            )

        Assertions.assert_json_value_name(
            response2,
            'user_id',
            self.user_id_from_auth_method,
            'Error. user_id_from_method != user_id'
        )

    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_chack(self, condition):
        url2 = 'https://playground.learnqa.ru/api/user/auth'
        if condition == 'no_cookie':
            response2 = requests.get(
                url2,
                headers={'x-csrf-token': self.token},
            )
        else:
            response2 = requests.get(
                url2,
                cookies={'auth_sid':  self.auth_sid},
            )

        Assertions.assert_json_value_name(
            response2,
            'user_id',
            0,
            'Error. User is authorisation'
        )
