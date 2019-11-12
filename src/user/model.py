from common.base.model import BaseModel


class UserModel(BaseModel):
    _fields = {
        "name": (str, True)
    }

    def __init__(self):
        super().__init__("api1", "hot_web_group")
