from common.utils.dict_util.check import *


class NewHotWebGroupValidator(Validator):
    name = StringField(name="name")


class DeleteHotWebGroupValidator(Validator):
    id = ObjectField(name="id")


class FindHotWebGroupValidator(Validator):
    pass

class UpdateHotWebGroupValidator(Validator):
    pass


class FindManyHotWebGroupValidator(Validator):
    pass
