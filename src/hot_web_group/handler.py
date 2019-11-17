from common.base.handler import JsonLoginedHandler
from common.code import *
from src.hot_web.service import HotWebService
from .validator import *
from .service import *

service = HotWebGroupService()
hot_web_service = HotWebService()


class HotWebGroupHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        ok, err = NewHotWebGroupValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        self.request_json["user_id"] = self.user_id
        code = service.create_one(self.request_json)
        return self.return_json(code)

    def delete(self, *args, **kwargs):
        ok, err = DeleteHotWebGroupValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.delete_one_by_id_doc(self.request_json)
        return self.return_json(code)

    def get(self, *args, **kwargs):
        ok, err = FindHotWebGroupValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdateHotWebGroupValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class HotWebGroupManyHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyHotWebGroupValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        _, data_list = service.find_many({"user_id": self.user_id})
        return self.return_json(hot_web_group_list=data_list)

    def put(self, *args, **kwargs):
        pass
