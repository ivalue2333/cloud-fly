from common.base.handler import JsonHandler
from common.code import *
from common.config import CookieName
from .validator import *
from .service import *

service = UserService()

"""
    目前密码加密没有意义
    cookie加密也没有意思
"""


class SignUpHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignUpUserValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.create_one(self.request_json)
        return self.return_json(code)


class SignInHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignInUserValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        user = service.find_one(self.request_json)
        if user:
            self.set_cookie(CookieName, str(user["_id"]))
        return self.return_json()


class SignOutHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignOutUserValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class UserManyHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyUserValidator(self.request_json).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
