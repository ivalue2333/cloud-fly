from common.base.handler import JsonHandler
from common.code import *
from .validator import *
from .service import *

service = UserService()

"""
    目前密码加密没有意义
    cookie加密也没有意思
"""


class SignUpHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignUpUserValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        code = service.create_one(self.json_body)
        return self.return_json(code)


class SignInHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignInUserValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)
        user = service.find_one(self.json_body)
        if user:
            self.set_cookie("uid", str(user["_id"]))
        return self.return_json()


class SignOutHandler(JsonHandler):
    def post(self, *args, **kwargs):
        ok, err = SignOutUserValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)


class UserManyHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        ok, err = FindManyUserValidator(self.json_body).validate()
        if not ok:
            return self.return_json(ErrorCodeParamWrong, err)

    def put(self, *args, **kwargs):
        pass
