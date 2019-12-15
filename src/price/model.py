from common.base.model import BaseModel


class PriceModel(BaseModel):
    _fields = {
        "name": (str, True),
        "price": (float, True),
        "location": (str, True),
        "date": (str, True),
    }

    def __init__(self):
        super().__init__("cf", "price")
