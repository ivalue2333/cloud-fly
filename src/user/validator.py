from common.utils.dict_util.check import *


class SignUpUserValidator(Validator):
    username = StringField(range_=(1, 20))
    password = StringField(range_=(6, 18))


class SignInUserValidator(Validator):
    username = StringField(range_=(1, 20))
    password = StringField(range_=(6, 18))


class SignOutUserValidator(Validator):
    pass


class FindManyUserValidator(Validator):
    pass
