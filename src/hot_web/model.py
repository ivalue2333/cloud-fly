from bson import ObjectId

from common.base.model import BaseModel


class HotWebModel(BaseModel):
    _fields = {
        "desc": (str, True),
        "url": (str, True),

        "hot_web_group_id": (ObjectId, True),
    }

    def __init__(self):
        super().__init__("cf", "hot_web")
