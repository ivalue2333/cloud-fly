from bson import ObjectId

from common.code import *
from common.log import logger
from common.base.model import BaseModel


class BaseService(object):
    def __init__(self, model_class_obj: BaseModel):
        self.model = model_class_obj

    def create_one(self, doc):
        try:
            self.model.create(doc)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("create_one failed. doc : {}, error : {}".format(doc, e))
            return ErrorCodeMongoCreate

    def delete_one(self, spec):
        try:
            self.model.delete_one(spec)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("delete_one failed. spec : {}, error : {}".format(spec, e))
            return ErrorCodeMongoOperate

    def delete_one_by_id(self, _id):
        try:
            self.model.delete_one({"_id": ObjectId(_id)})
            return ErrorCodeNotError
        except Exception as e:
            logger.error("delete_one_by_id failed. _id : {}, error : {}".format(_id, e))
            return ErrorCodeMongoOperate

    def delete_one_by_id_doc(self, doc):
        if "id" not in doc:
            logger.error("delete_one_by_id_doc failed. doc : {}, error : {}".format(doc, "id not in doc"))
            return ErrorCodeMongoOperate
        else:
            try:
                self.model.delete_one({"_id": ObjectId(doc["id"])})
                return ErrorCodeNotError
            except Exception as e:
                logger.error("delete_one_by_id_doc failed. doc : {}, error : {}".format(doc, e))
                return ErrorCodeMongoOperate

    def delete_many(self, spec):
        try:
            self.model.delete_many(spec)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("delete_many failed. spec : {}, error : {}".format(spec, e))
            return ErrorCodeMongoOperate

    def find_one(self, spec):
        return self.model.find_one(spec)

    def find_one_by_id(self, _id):
        return self.model.find_one({"_id": ObjectId(_id)})

    def find_one_by_id_doc(self, doc):
        if "id" not in doc:
            logger.error("find_one_by_id_doc failed. doc : {}, error : {}".format(doc, "id not in doc"))
            return None
        else:
            return self.model.find_one({"_id": ObjectId(doc["id"])})

    def find_many(self, spec, skip=0, limit=0, user_id=""):
        if user_id:
            spec["user_id"] = user_id
        cursor = self.model.find(spec)
        count = cursor.count()
        if skip != 0:
            cursor = cursor.skip(skip=skip)
        if limit != 0:
            cursor = cursor.limit(limit)
        return count, list(cursor)

    def update_one(self, spec, doc):
        try:
            self.model.modify_one(spec, doc)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("update_one failed. spec : {}, doc : {}, error : {}".format(spec, doc, e))
            return ErrorCodeMongoOperate

    def update_one_by_id(self, _id, doc):
        try:
            self.model.modify_one({"_id": _id}, doc)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("update_one_by_id failed. _id : {}, doc : {}, error : {}".format(_id, doc, e))
            return ErrorCodeMongoOperate

    def update_one_by_id_doc(self, doc):
        if "id" not in doc:
            logger.error("update_one_by_id_doc failed. doc : {}, error : {}".format(doc, "id not in doc"))
            return ErrorCodeMongoOperate
        else:
            try:
                spec = {"_id": ObjectId(doc.pop("id"))}
                self.model.update_one(spec, doc)
                return ErrorCodeNotError
            except Exception as e:
                return ErrorCodeMongoOperate

    def update_many(self, spec, doc):
        try:
            self.model.modify_many(spec, doc)
            return ErrorCodeNotError
        except Exception as e:
            logger.error("update_many failed. spec : {}, doc : {}, error : {}".format(spec, doc, e))
            return ErrorCodeMongoOperate
