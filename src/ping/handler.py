import json
from http import HTTPStatus

from common.base.handler import JsonHandler, JsonLoginedHandler


class PingHandler(JsonHandler):
    def get(self, *args, **kwargs):
        # print(self.request.arguments)
        print(self.request_json)
        self.log_keeper.set("ping", "pong")
        # return self.set_status(HTTPStatus.FORBIDDEN.value)
        return self.return_json(data="pong")

    def post(self, *args, **kwargs):
        body = self.request.body.decode("utf-8")
        body_json = json.loads(body, "utf-8")
        print(self.request.arguments)
        print(self.request.body)
        print(body_json, type(body_json))
        return self.return_json(data="pong")


class PingLoginedHandler(JsonLoginedHandler):
    def get(self, *args, **kwargs):
        # print(self.request.arguments)
        print(self.request_json)
        print(self.user_id)
        self.log_keeper.set("ping", "pong")
        return self.return_json(data="pong")

    def post(self, *args, **kwargs):
        body = self.request.body.decode("utf-8")
        body_json = json.loads(body, "utf-8")
        print(self.request.arguments)
        print(self.request.body)
        print(body_json, type(body_json))
        return self.return_json(data="pong")
