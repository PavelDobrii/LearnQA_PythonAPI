import requests


class TestLongRedirect:

    def test_long_redirect(self):
        url = 'https://playground.learnqa.ru/api/long_redirect'
        response = requests.get(url)
        assert len(response.history) == 2
