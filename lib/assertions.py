from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, 'ERROR JSON'

        assert name in response_as_dict, 'ERROR JSON 2'
        assert response_as_dict[name] == expected_value, error_message

