from common.base.model import BaseModel


class UserModel(BaseModel):
    _fields = {
        "username": (str, True),
        "password": (str, True)
    }

    def __init__(self):
        super().__init__("cf", "user")
