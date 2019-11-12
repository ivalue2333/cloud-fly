import hashlib

SaltWord = "uevoli"


def generate_password(name, password):
    """
    生成密码
    name.salt.password -> md5
    :param name:
    :param password:
    :return:
    """
    if not name or not password:
        return None
    pass_str = name + "." + SaltWord + "." + password
    md5_obj = hashlib.md5()
    md5_obj.update(pass_str.encode())
    return md5_obj.hexdigest()


def auth_password(name, password, password_md5):
    """
    验证密码是否正确
    :param name:
    :param password:
    :param password_md5:
    :return:
    """
    pass_str = name + "." + SaltWord + "." + password
    md5_obj = hashlib.md5()
    md5_obj.update(pass_str.encode())
    return md5_obj.hexdigest() == password_md5
