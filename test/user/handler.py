import unittest
import requests

from test.common.handler import TestCommonHandler


class TestUserHandler(TestCommonHandler):
    def setUp(self):
        self.host = "http://localhost:5000"

    def get_url(self, url):
        return self.host + url

    def test_sign_up(self):
        res = requests.post(self.get_url("/api/v1/sign_up"), json={"username": "percy", "password": "abcdef"})
        content = res.content
        print(content)

    def test_sign_in(self):
        res = requests.post(self.get_url("/api/v1/sign_in"), json={"username": "percy", "password": "abcdef"})
        content = res.content
        print(content)
        print(res.headers)


if __name__ == "__main__":
    unittest.main()
