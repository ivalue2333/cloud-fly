from common.base.service import BaseService
from .model import *


class PriceService(BaseService):
    def __init__(self):
        super().__init__(PriceModel())
