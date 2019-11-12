from common.base.handler import JsonHandler
from common.code import *
from .validator import *
from .service import *

service = BasementService()


class BasementHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = NewBasementValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def delete(self, *args, **kwargs):
        ok, err = DeleteBasementValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def get(self, *args, **kwargs):
        ok, err = FindBasementValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdateBasementValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class BasementManyHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyBasementValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
