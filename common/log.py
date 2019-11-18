import logging
import logging.config
import os

logger = logging.getLogger("app")


def init_log():
    logging.config.dictConfig(get_logging_config())


def get_logging_config(log_dir="/var/log/percy", service_name="cloud_fly", level="INFO"):
    def get_log_name(log_name):
        return service_name + "." + log_name

    def get_log_path(log_name):
        return os.path.join(log_dir, get_log_name(log_name))

    return {
        'version': 1,
        'incremental': False,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': "%(levelname)s %(asctime)s %(pathname)s %(lineno)d  %(funcName)s %(message)s"
            },
            'simple': {
                'format': "%(levelname)s %(asctime)s %(lineno)d %(message)s"
            },
        },
        'handlers': {
            'app': {
                'level': level,
                'class': "logging.handlers.WatchedFileHandler",
                'filename': get_log_path("app.log"),
                'formatter': "verbose",
            },
            'console': {
                'level': level,
                'class': "logging.StreamHandler",
                'formatter': "simple"
            },
            'tornado_access': {
                'level': level,
                'class': "logging.handlers.WatchedFileHandler",
                'filename': get_log_path("tornado.access.log"),
                'formatter': "simple"
            },
            'tornado_error': {
                'level': level,
                'class': "logging.FileHandler",
                'filename': get_log_path("tornado.error.log"),
                'formatter': "simple"
            },
        },
        'loggers': {
            'app': {
                'handlers': ["app", "console"],
                'level': level,
                'propagate': False
            },
            'tornado.access': {
                'handlers': ["tornado_access"],
                'level': level
            },
            'tornado.application': {
                'handlers': ["tornado_error"],
                'level': level
            },
            'tornado.general': {
                'handlers': ["tornado_error"],
                'level': level
            },
        }
    }
