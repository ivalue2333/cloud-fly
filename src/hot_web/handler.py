from common.base.handler import JsonLoginedHandler
from common.code import *
from .validator import *
from .service import *

service = HotWebService()


class HotWebHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        ok, err = NewHotWebValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.create_one(self.request_json)
        return self.return_json(code)

    def delete(self, *args, **kwargs):
        ok, err = DeleteHotWebValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.delete_one_by_id_doc(self.request_json)
        return self.return_json(code)

    def get(self, *args, **kwargs):
        ok, err = FindHotWebValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdateHotWebValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class HotWebManyHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyHotWebValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        _, data_list = service.find_many({"hot_web_group_id": self.request_json["hot_web_group_id"]})
        return self.return_json(hot_web_list=data_list)

    def put(self, *args, **kwargs):
        pass
