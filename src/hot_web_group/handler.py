from common.base.handler import JsonHandler
from common.code import *
from .validator import *
from .service import *

service = HotWebGroupService()


class HotWebGroupHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = NewHotWebGroupValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.create_one(self.json_body)
        return self.return_json(code)

    def delete(self, *args, **kwargs):
        ok, err = DeleteHotWebGroupValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        service.delete_one_by_id_doc(self.json_body)

    def get(self, *args, **kwargs):
        ok, err = FindHotWebGroupValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdateHotWebGroupValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class HotWebGroupManyHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyHotWebGroupValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
