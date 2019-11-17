from bson import ObjectId
from datetime import datetime


def base_vo(data_or_datas):
    """
    性能并不好，但通用
    :param data_or_datas:
    :return:
    """
    if isinstance(data_or_datas, dict):
        if "_id" in data_or_datas:
            data_or_datas["id"] = str(data_or_datas.pop("_id"))
        if "create_time" in data_or_datas:
            data_or_datas["create_time"] = data_or_datas["create_time"].strftime("%Y-%m-%d %H:%M:%S")
        if "update_time" in data_or_datas:
            data_or_datas["update_time"] = data_or_datas["update_time"].strftime("%Y-%m-%d %H:%M:%S")

        for k, v in data_or_datas.items():
            if isinstance(v, list) or isinstance(v, dict):
                base_vo(v)

            if isinstance(v, ObjectId):
                data_or_datas[k] = str(data_or_datas[k])

            if isinstance(v, datetime):
                data_or_datas[k] = data_or_datas[k].strftime("%Y-%m-%d %H:%M:%S")

    elif isinstance(data_or_datas, list):
        for v in data_or_datas:
            base_vo(v)
