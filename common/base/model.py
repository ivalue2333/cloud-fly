from datetime import datetime

from pymongo import MongoClient
from pymongo.collection import Collection

from common.code import ErrorCodeMongoValidate
from common.config import MongoConfigDict


def get_mongo_conn():
    return MongoClient(**MongoConfigDict)


def get_mongo_database(db_name):
    return get_mongo_conn().get_database(db_name)


class BaseModel(Collection):
    _fields = {}

    def __init__(self, db_name, table_name, *args, **kwargs):
        super().__init__(get_mongo_database(db_name), table_name, *args, **kwargs)

    def create(self, doc_or_docs):
        if isinstance(doc_or_docs, dict):
            self._filter_none_value(doc_or_docs)
            self._validate(doc_or_docs)
            if "create_time" not in doc_or_docs:
                doc_or_docs["create_time"] = datetime.now()
            if "update_time" not in doc_or_docs:
                doc_or_docs["update_time"] = doc_or_docs["create_time"]
            result = super().insert_one(doc_or_docs)
            return result.inserted_id
        elif isinstance(doc_or_docs, list):
            for v in doc_or_docs:
                self._filter_none_value(v)
                self._validate(v)
                if "create_time" not in v:
                    v["create_time"] = datetime.now()
                if "create_time" not in v:
                    v["update_time"] = v["create_time"]
            result = super().insert_many(doc_or_docs)
            return result.inserted_ids

    def modify_one(self, spec: dict, doc: dict):
        self._filter_none_value(doc)
        self._validate(doc, False)
        doc["update_time"] = datetime.now()
        to_set_doc = {"$set": doc}
        return super().update_one(spec, to_set_doc)

    def modify_many(self, spec: dict, doc: dict):
        self._filter_none_value(doc)
        self._validate(doc, False)
        doc["update_time"] = datetime.now()
        to_set_doc = {"$set": doc}
        return super().update_many(spec, to_set_doc)

    @classmethod
    def _validate(cls, doc: dict, required=True):
        if not cls._fields:
            return True

        for k, v in doc.items():
            if "." in k:
                continue

            if k not in cls._fields:
                raise MongoValidateException("{} not in fields".format(k))

            _type, _ = cls._fields[k]
            if _type is not None and not isinstance(v, _type):
                raise MongoValidateException("field '{}' should be a '{}' type".format(k, _type))

            if required:
                fields = [k for k, v in cls._fields.items() if v[1]]
                for v in fields:
                    if v not in doc:
                        raise MongoValidateException("field '{}' is required".format(v))

    @staticmethod
    def _filter_none_value(doc: dict):
        if not isinstance(doc, dict):
            raise MongoValidateException("doc should be a dict")

        # 这样可以在遍历中删除，因为已经从生成器中获取了全部数据
        for k, v in list(doc.items()):
            if v is None:
                del doc[k]
        return doc


class MongoValidateException(Exception):
    def __init__(self, message, code=ErrorCodeMongoValidate):
        super().__init__(message, code)
        self.message = message
        self.code = code
