from bson import ObjectId

from common.base.model import BaseModel


class HotWebGroupModel(BaseModel):
    _fields = {
        "name": (str, True),
        "user_id": (ObjectId, True)
    }

    def __init__(self):
        super().__init__("cf", "hot_web_group")