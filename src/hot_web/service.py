from common.base.service import BaseService
from .model import *


class HotWebService(BaseService):
    def __init__(self):
        super().__init__(HotWebModel())
