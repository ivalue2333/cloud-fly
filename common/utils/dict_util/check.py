import bson

ErrorMsgDataMustDict = "data must dict"
ErrorMsgKeyNotExists = "key '{}' not exists"
ErrorMsgTypeError = "value type error, key: '{}', type: {}, right type: {}"
ErrorMsgLengthRangeError = "value length range error, key: '{}', length: {}, right range: {}"
ErrorMsgNumberRangeError = "value number range error, key: '{}', number: {}, right range: {}"
NeedTransportTypes = [bson.ObjectId]


class Field(object):
    _json_field = None

    def __init__(self, name="", default=None, type_=None, range_=tuple(), prefix="", hooks=tuple()):
        self.name = name
        self.default = default
        self.type = type_
        self.range = range_
        self.prefix = prefix
        self.hooks = hooks

    def set_name(self, name):
        self.name = name

    def validate(self, data_dict: dict) -> (bool, str):
        ok = True
        error_msg = ""

        for i in range(1):
            if not isinstance(data_dict, dict):
                ok, error_msg = False, ErrorMsgDataMustDict
                break

            #  name and default validate
            if self.name not in data_dict:
                if self.default is None:
                    ok, error_msg = False, ErrorMsgKeyNotExists.format(self.name)
                    break
                else:
                    data_dict[self.name] = self.default

            #  type validate
            if not isinstance(data_dict[self.name], self.type):
                if self.type in NeedTransportTypes:
                    try:
                        data_dict[self.name] = self.type(data_dict[self.name])
                    except Exception as e:
                        ok, error_msg = False, ErrorMsgTypeError.format(self.name, type(data_dict[self.name]),
                                                                        self.type)
                        break
                else:
                    ok, error_msg = False, ErrorMsgTypeError.format(self.name, type(data_dict[self.name]),
                                                                    self.type)
                    break

            # range validate
            if self.type in [str, list]:
                length = len(data_dict[self.name])
                if len(self.range) > 2:
                    raise FieldException()
                elif len(self.range) == 2:
                    if length > self.range[1] or length < self.range[0]:
                        ok, error_msg = False, ErrorMsgLengthRangeError.format(self.name, length, self.range)
                        break
                elif len(self.range) == 1:
                    if length < self.range[0]:
                        ok, error_msg = False, ErrorMsgLengthRangeError.format(self.name, length, self.range)
                        break
            elif self.type in [int, float]:
                data = data_dict[self.name]
                if len(self.range) > 2:
                    raise FieldException()
                elif len(self.range) == 2:
                    if data > self.range[1] or data < self.range[0]:
                        ok, error_msg = False, ErrorMsgNumberRangeError.format(self.name, data, self.range)
                        break
                elif len(self.range) == 1:
                    if data < self.range[0]:
                        ok, error_msg = False, ErrorMsgNumberRangeError.format(self.name, data, self.range)
                        break

            # prefix add
            if self.prefix:
                data_dict[self.name] = self.prefix + data_dict[self.name]

            if self.hooks:
                for hook in self.hooks:
                    hook(data_dict)
        return ok, error_msg


class FieldException(Exception):
    def __init__(self, message="Please refer to doc"):
        super().__init__(message)
        self.message = message


class StringField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, str, range_, prefix, hooks)


class IntegerField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, int, range_, prefix, hooks)


class FloatField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, float, range_, prefix, hooks)


class BooleanField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, bool, range_, prefix, hooks)


class ListField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, list, range_, prefix, hooks)


class JsonField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, dict, range_, prefix, hooks)


class ObjectField(Field):
    def __init__(self, name="", default=None, range_=tuple(), prefix="", hooks=tuple()):
        super().__init__(name, default, bson.ObjectId, range_, prefix, hooks)


class ValidatorMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._unbound_fields = None

    def __call__(cls, *args, **kwargs):
        """
        JsonMeta搞成单例，这样可以让JsonMeta的对象被多次利用
        :param args:
        :param kwargs:
        :return:
        """
        if cls._unbound_fields is None:
            fields = []
            for name in dir(cls):
                if not name.startswith("_"):
                    unbound_field = getattr(cls, name)
                    if hasattr(unbound_field, "_json_field"):
                        unbound_field.set_name(name)
                        fields.append(unbound_field)
            cls._unbound_fields = fields
            return super().__call__(*args, **kwargs)
        return super().__call__(*args, **kwargs)


class Validator(metaclass=ValidatorMeta):
    def __new__(cls, data_dict: dict):
        return super().__new__(cls)

    def __init__(self, data_dict: dict):
        self.data_dict = data_dict

    def validate(self):
        ok, err = True, ""
        for field in self._unbound_fields:
            ok, err = field.validate(self.data_dict)
            if not ok:
                break
        return ok, err


def test():
    class StringValidator(Validator):
        age = StringField(name="age", range_=(3, 5))

    class IntegerValidator(Validator):
        num = IntegerField(name="num", default=3, range_=(10, 23))

    class JsonValidator(Validator):
        json_ = JsonField()

    print(StringValidator({"age": "abcde"}).validate())
    print('----')
    print(StringValidator({"age": "a"}).validate())
    print('----')
    print(IntegerValidator({"num": 132}).validate())
    print('----')
    print(JsonValidator({"json_": "ac"}).validate())


if __name__ == "__main__":
    test()
