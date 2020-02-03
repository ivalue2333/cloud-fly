import requests

import unittest


class TestHandler(unittest.TestCase):

    def test_post(self):
        pass

    def test_delete(self):
        pass

    def test_get(self):
        res = requests.get("http://127.0.0.1:5000/api/v1/ping?age=10", json={"name": "你好"})
        res = requests.get("http://127.0.0.1:5000/api/v1/ping?age=10")
        print(res.content)

    def test_put(self):
        pass


class TestManyHandler(unittest.TestCase):
    def test_post(self):
        pass

    def test_delete(self):
        pass

    def test_get(self):
        pass

    def test_put(self):
        pass


if __name__ == "__main__":
    unittest.main()
