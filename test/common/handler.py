import unittest

import requests


class TestCommonHandler(unittest.TestCase):
    def setUp(self):
        self.host = "http://localhost:5000"

    def get_url(self, url):
        return self.host + url

    def get_session(self):
        session = requests.session()
        session.post(self.get_url("/api/v1/sign_in"), json={"username": "percy", "password": "abcdef"})
        return session
