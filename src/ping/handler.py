import json

from common.base.handler import JsonHandler


class PingHandler(JsonHandler):
    def get(self, *args, **kwargs):
        # print(self.request.arguments)
        print(self.json_body)
        return self.return_json(data="pong")

    def post(self, *args, **kwargs):
        body = self.request.body.decode("utf-8")
        body_json = json.loads(body, "utf-8")
        print(self.request.arguments)
        print(self.request.body)
        print(body_json, type(body_json))
        return self.return_json(data="pong")
