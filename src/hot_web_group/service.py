from common.base.service import BaseService
from .model import *


class HotWebGroupService(BaseService):
    def __init__(self):
        super().__init__(HotWebGroupModel())
