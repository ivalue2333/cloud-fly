import os


def get_logging_config(log_env, service_name):
    def __get_name(name):
        return service_name + "." + name

    level = log_env["level"]
    log_dir = log_env["dir"]
    return {
        'version': 1,
        'incremental': False,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': "%(levelname)s %(asctime)s %(pathname)s %(lineno)d \
    %(funcName)s \"%(message)s\""
            },
            'simple': {
                'format': "%(levelname)s %(asctime)s \"%(message)s\""
            },
            'raw': {
                'format': "%(asctime)s %(message)s"
            },
        },
        'handlers': {
            'null': {
                'level': level,
                'class': "logging.NullHandler",
            },
            'console': {
                'level': level,
                'class': "logging.StreamHandler",
                'formatter': "simple"
            },
            'app': {
                'level': level,
                'class': "logging.handlers.WatchedFileHandler",
                'filename': os.path.join(log_dir, __get_name("app.log")),
                'formatter': "verbose",
            },
            'app_err': {
                'level': "ERROR",
                'class': "logging.handlers.WatchedFileHandler",
                'filename': os.path.join(log_dir, __get_name("err.log")),
                'formatter': "verbose",
            },
            'command': {
                'level': level,
                'class': "logging.FileHandler",
                'filename': os.path.join(log_dir, __get_name("command.log")),
                'formatter': "verbose",
            },
            'remote': {
                'level': level,
                'class': "logging.FileHandler",
                'filename': os.path.join(log_dir, __get_name("remote.log")),
                'formatter': "verbose",
            },
            'tornado_access': {
                'level': level,
                'class': "logging.handlers.WatchedFileHandler",
                'filename': os.path.join(log_dir, __get_name("tornado.access.log")),
                'formatter': "simple"
            },
            'tornado_error': {
                'level': level,
                'class': "logging.FileHandler",
                'filename': os.path.join(log_dir, __get_name("tornado.err.log")),
                'formatter': "simple"
            },
            'request': {
                'level': level,
                'class': "logging.handlers.WatchedFileHandler",
                'filename': os.path.join(log_dir, __get_name("request.log")),
                'formatter': "raw"
            },
        },
        'loggers': {
            'app': {
                'handlers': ["app", "app_err"],
                'level': level,
                'propagate': False
            },
            'command': {
                'handlers': ["command", "console", "app_err"],
                'level': level,
                'propagate': False
            },
            'remote': {
                'handlers': ["remote", "app_err"],
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
            'request': {
                'handlers': ["request", "app_err"],
                'level': level,
                'propagate': False
            },
        }
    }
