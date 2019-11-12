from common.base.service import BaseService
from .model import *


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserModel())
