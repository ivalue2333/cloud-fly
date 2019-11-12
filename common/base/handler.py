import json
from datetime import datetime

from tornado.web import RequestHandler

from common.code import ErrorCodeMap
from common.log import logger
from .view import *


class LogKeeper:
    def __init__(self):
        self.keeper = []

    def set(self, key, value):
        self.keeper.append({key, value})

    def set_dict(self, data: dict):
        if len(data) > 1:
            raise Exception("data length should be one")
        self.keeper.append(data)

    def set_dict_many(self, data: dict):
        keys = sorted(data)
        for key in keys:
            self.keeper.append({key: data[key]})

    def get(self):
        return self.keeper


class BaseHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # log_keeper used to log all the logs in one request
        self.log_keeper = LogKeeper()

    def return_json(self, code=0, msg=None, **kwargs):
        data = {
            "code": code,
            "msg": msg if msg else ErrorCodeMap.get(code, None),
        }
        data.update(kwargs)
        base_vo(data)
        json_data = json.dumps(data)
        self.finish(json_data)

    def on_finish(self):
        _info = {
            "time_now": str(datetime.now()),
            "url": self.request.path,
            "time_served": self.request.request_time()
        }

        logger.debug(json.dumps(_info))

    def data_received(self, chunk):
        """Implement this method to handle streamed request data.

        Requires the `.stream_request_body` decorator.
        """
        pass


class JsonHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        self.json_body = {}
        super().__init__(*args, **kwargs)

    def prepare(self):
        body = self.request.body.decode("utf-8")
        json_body = json.loads(body, "utf-8")
        self.json_body = json_body
