from common.base.handler import JsonLoginedHandler
from common.code import *
from .validator import *
from .service import *

service = PriceService()


class PriceHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        ok, err = NewPriceValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def delete(self, *args, **kwargs):
        ok, err = DeletePriceValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def get(self, *args, **kwargs):
        ok, err = FindPriceValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        ok, err = UpdatePriceValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class PriceManyHandler(JsonLoginedHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyPriceValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
