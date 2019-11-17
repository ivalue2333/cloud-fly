import unittest
import requests

from src.hot_web_group.service import HotWebGroupService
from test.common.handler import TestCommonHandler
service = HotWebGroupService()


class TestHotWebGroupHandler(TestCommonHandler):

    def test_post(self):
        session = self.get_session()
        res = session.post(self.get_url("/api/v1/hot_web_group"), json={"name": "test中文2"})
        print(res.content)

        session.close()

    def test_delete(self):
        session = self.get_session()
        print(session.headers)
        print(session.cookies)
        data = service.find_one({})
        res = session.delete(self.get_url("/api/v1/hot_web_group"), json={"id": str(data["_id"])})
        print(res.content)

    def test_get(self):
        pass

    def test_put(self):
        pass


class TestHotWebGroupManyHandler(TestCommonHandler):
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
