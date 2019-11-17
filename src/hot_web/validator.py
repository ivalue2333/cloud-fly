from common.utils.dict_util.check import *


class NewHotWebValidator(Validator):
    desc = StringField()
    url = StringField()
    hot_web_group_id = ObjectField()


class DeleteHotWebValidator(Validator):
    id = ObjectField()


class FindHotWebValidator(Validator):
    pass


class UpdateHotWebValidator(Validator):
    pass


class FindManyHotWebValidator(Validator):
    hot_web_group_id = ObjectField()
