from common.base.model import BaseModel


class BasementModel(BaseModel):
    _fields = {
        "name": (str, True)
    }

    def __init__(self):
        super().__init__("api1", "basement")
