from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from src.ping.handler import PingHandler
from src.hot_web_group import handler as hwg_handler

routes = [
    (r"/api/v1/ping", PingHandler),


    (r"/api/v1/hot_web_group", hwg_handler.HotWebGroupHandler),
]

if __name__ == "__main__":
    app = Application(routes)
    server = HTTPServer(app, xheaders=True)

    ip = "127.0.0.1"
    port = 5000
    process_num = 1

    server.bind(port, address=ip)
    server.start(process_num)
    IOLoop.current().start()
