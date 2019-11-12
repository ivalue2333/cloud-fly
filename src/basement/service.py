from common.base.service import BaseService
from .model import *


class BasementService(BaseService):
    def __init__(self):
        super().__init__(BasementModel())
