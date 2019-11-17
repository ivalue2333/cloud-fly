from common.base.handler import JsonLoginedHandler
from common.code import *
from .validator import *
from .service import *

service = BasementService()


class BasementHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        ok, err = NewBasementValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def delete(self, *args, **kwargs):
        ok, err = DeleteBasementValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def get(self, *args, **kwargs):
        ok, err = FindBasementValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdateBasementValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class BasementManyHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyBasementValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
