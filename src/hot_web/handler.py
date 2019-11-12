from common.base.handler import JsonHandler


class BaseHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass


class BaseManyHandler(JsonHandler):
    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass
