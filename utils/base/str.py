import uuid
import base64


class MyStr:
    @staticmethod
    def is_blank(str_input):
        """
        判断字符串是否空
        :param str_input: 字符串对象
        :return: True 空字符串，False 不为空
        """
        return str_input is None or not isinstance(str_input, str) or len(str_input) == 0

    @staticmethod
    def to_int(str_input, def_value):
        """
        将字符串转换为整数
        :param str_input:
        :param def_value: 转换失败时设置为默认值
        :return: 整数
        """
        if MyStr.is_blank(str_input) or not str_input.isdigit():
            value = def_value
        else:
            value = int(str_input)

        return value

    @staticmethod
    def bytes2str(bytes, encoded='utf-8'):
        return bytes.decode(encoded)

    @staticmethod
    def uuid():
        """
        生成 uuid 字符串
        :return: uuid 字符串
        """
        return str(uuid.uuid4())

    @staticmethod
    def b64_encode(bytes):
        """
        对二进制数据进行 base64 编码，并返回编码结果
        :param bytes: 原始数据
        :return: base64 编码
        """
        return base64.b64encode(bytes).decode()


