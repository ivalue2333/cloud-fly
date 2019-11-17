import json
from datetime import datetime

from tornado.web import RequestHandler

from common.code import *
from common.config import CookieName
from common.log import logger
from .view import *
from .log_keeper import *


class BaseHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # log_keeper used to log all the logs in one request
        self.log_keeper = LogKeeperFactory().get_log_keeper(LogKeeperTypeDict)

    def return_json(self, code=0, msg=None, **kwargs):
        data = {
            "code": code,
            "msg": msg if msg else ErrorCodeMap.get(code, None),
        }
        data.update(kwargs)
        base_vo(data)
        self.log_keeper.set("return_json", data)
        json_data = json.dumps(data)
        self.finish(json_data)

    def on_finish(self):
        _info = {
            "request_time_end": str(datetime.now()),
            "url": self.request.path,
            "request_time_served": self.request.request_time()
        }

        _info.update(self.log_keeper.get())

        logger.info(_info)

    def data_received(self, chunk):
        """Implement this method to handle streamed request data.

        Requires the `.stream_request_body` decorator.
        """
        pass


class JsonHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        self.request_json = {}
        super().__init__(*args, **kwargs)

    def prepare(self):
        self.log_keeper.set("request_time_start", str(datetime.now()))
        body = self.request.body.decode("utf-8")
        if body:
            request_json = json.loads(body, "utf-8")
            self.request_json = request_json
            self.log_keeper.set("request_body", request_json)
        if self.request.arguments:
            for k, items in self.request.arguments.items():
                self.request_json[k] = items[0].decode("utf-8")


class JsonLoginedHandler(JsonHandler):
    def __init__(self, *args, **kwargs):
        self.user_id = ""
        super().__init__(*args, **kwargs)

    def prepare(self):
        """
        judge if need login
        :return:
        """
        if self.get_cookie(CookieName):
            self.user_id = ObjectId(self.get_cookie(CookieName))
            super().prepare()
        else:
            self.return_json(ErrorCodeAuthNotSignIn)
