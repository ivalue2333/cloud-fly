from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from common.log import init_log
from src.ping.handler import PingHandler, PingLoginedHandler
from src.hot_web_group import handler as hwg_handler
from src.hot_web import handler as hw_handler
from src.user import handler as user_handler

routes = [
    #  --- ping服务 ---
    (r"/api/v1/ping", PingHandler),
    (r"/api/v1/ping/logined", PingLoginedHandler),

    #  --- 注册登陆 ---
    (r"/api/v1/sign_up", user_handler.SignUpHandler),
    (r"/api/v1/sign_in", user_handler.SignInHandler),

    # --- 个人收藏云 ---
    (r"/api/v1/hot_web_group", hwg_handler.HotWebGroupHandler),
    (r"/api/v1/hot_web_group_many", hwg_handler.HotWebGroupManyHandler),
    (r"/api/v1/hot_web", hw_handler.HotWebHandler),
    (r"/api/v1/hot_web_many", hw_handler.HotWebManyHandler),
]

if __name__ == "__main__":
    app = Application(routes)
    server = HTTPServer(app, xheaders=True)

    init_log()

    ip = "127.0.0.1"
    port = 5000
    process_num = 1

    server.bind(port, address=ip)
    server.start(process_num)
    IOLoop.current().start()
