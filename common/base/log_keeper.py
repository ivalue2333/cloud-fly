LogKeeperTypeDict = "log_keeper_type_dict"


class LogKeeperInterface:
    def __init__(self):
        pass

    def set(self, key, value, **kwargs):
        raise NotImplementedError("to be implemented")

    def get(self):
        raise NotImplementedError("to be implemented")


class LogKeeperDict(LogKeeperInterface):
    def __init__(self):
        self.log_keeper = dict()
        super().__init__()

    def set(self, key, value, **kwargs):
        self.log_keeper[key] = value
        if kwargs:
            self.log_keeper.update(kwargs)

    def get(self):
        return self.log_keeper


class LogKeeperFactory:
    @classmethod
    def get_log_keeper(cls, log_keeper_type):
        if log_keeper_type == LogKeeperTypeDict:
            return LogKeeperDict()
        else:
            return LogKeeperDict()
