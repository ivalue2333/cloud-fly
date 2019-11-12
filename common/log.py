import logging


class Logger:
    """
    这样才不会重复打印（在引用的情况下）
    """
    def __init__(self, service_name, log_level=logging.INFO, path='/var/log/percy/'):
        self.logger = logging.getLogger(str(service_name))
        self.path = path + str(service_name) + ".log"

        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(self.path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'))
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(
            logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'))
        self.logger.addHandler(console_handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


logger = Logger("cloud_fly")