import unittest

from src.hot_web.service import HotWebService
from src.hot_web_group.service import HotWebGroupService
from test.common.handler import TestCommonHandler

hwg_service = HotWebGroupService()
hw_service = HotWebService()


class TestHotWebHandler(TestCommonHandler):

    def test_post(self):
        session = self.get_session()
        try:
            data = hwg_service.find_one({})
            res = session.post(self.get_url("/api/v1/hot_web"),
                               json={"desc": "链接1", "url": "http://www.baidu.com",
                                     "hot_web_group_id": str(data["_id"])})
            print(res.content)
        finally:
            session.close()

    def test_delete(self):
        session = self.get_session()
        try:
            data = hw_service.find_one({})
            res = session.delete(self.get_url("/api/v1/hot_web"), json={"id": str(data["_id"])})
            print(res.content)
        finally:
            session.close()

    def test_get(self):
        pass

    def test_put(self):
        pass


class TestHotWebManyHandler(TestCommonHandler):
    def test_post(self):
        pass

    def test_delete(self):
        pass

    def test_get(self):
        session = self.get_session()
        try:
            data = hwg_service.find_one({})
            res = session.get(self.get_url("/api/v1/hot_web_many"), params={"hot_web_group_id": str(data["_id"])})
            print(res.content)
        finally:
            session.close()

    def test_put(self):
        pass


if __name__ == "__main__":
    unittest.main()
