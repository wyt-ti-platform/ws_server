from bs4 import BeautifulSoup
import dicttoxml
import xmltodict
from xml.dom.minidom import parseString


class MyDict:
    @staticmethod
    def copy_dict(src_dict, key_list):
        """
        从源字典中，按照指定的键列表，拷贝对应的元素，组合成一个新字典返回
        :param src_dict: 源字典
        :param key_list: 指定拷贝的列表
        :return: 拷贝出来的字典
        """
        dest_dict = {}
        for key in key_list:
            if key in src_dict.keys():
                dest_dict[key] = src_dict[key]
            else:
                dest_dict[key] = None
        return dest_dict

    @staticmethod
    def copy_keys(src, dest, keys):
        """
        按照 keys 指定的键列表，从源字典中拷贝 KV 键值对到目标字典中
        :param src: 源字典
        :param dest: 目标字典
        :param keys: 需拷贝的键列表
        :return: True--成功；False--失败
        """
        if not isinstance(src, dict) or not isinstance(dest, dict):
            return False
        for key in keys:
            dest[key] = src[key] if key in src.keys() else None
        return True

    @staticmethod
    def dict2obj(dict_obj):
        """
        转换字典成为对象，可以用"."方式访问对象属性
        :param dict_obj: 要转换的字典对象
        :return: 可使用"."方式访问属性的对象
        """
        if not isinstance(dict_obj, dict):
            return dict_obj
        d = Dict()
        for k, v in dict_obj.items():
            d[k] = MyDict.dict2obj(v)
        return d

    @staticmethod
    def clear(dict_obj):
        """
        清空字典中所有元素
        :param dict_obj: 字典对象
        :return: 无
        """
        dict_obj.clear()

    @staticmethod
    def remove_keys(dict_obj, keys):
        """
        移除字典中键值对，由 keys 列表指定
        :param dict_obj: 字典对象
        :param keys: 键列表
        :return: 无
        """
        for key in keys:
            # 设置默认返回值 'default_rv'，以免 key 不存在时报错
            dict_obj.pop(key, 'default_rv')

    @staticmethod
    def exist_key(dict_obj, key_name):
        if dict_obj is None:
            return False
        return key_name in dict_obj.keys()

    @staticmethod
    def parse_xml(xml):
        """
        解析XML
        :param xml: XML 数据
        :return: 字典
        """
        dict_obj = xmltodict.parse(xml)
        return dict_obj

    @staticmethod
    def simple_parse_xml(xml):
        """
        简单解析XML，不支持数组和层次嵌套
        采用bs，要预先安装lxml，pip install lxml
        BeautifulSoup常用操作: https://www.jianshu.com/p/c1f5e6b658f8
        :param xml: XML 数据
        :return: 字典
        """
        soup = BeautifulSoup(xml, features='xml')
        items = soup.find_all()
        # item_dict = dict([(item.name, item.attrs['text']) for item in items])
        item_dict = {}
        for item in items:
            # 不含属性，或名称为空的，跳过
            if len(item.attrs) > 0 and item.name is not None:
                item_dict[item.name] = item.attrs
        return item_dict

    @staticmethod
    def to_xml(dict_obj, custom_root='root'):
        bxml = dicttoxml.dicttoxml(dict_obj, custom_root=custom_root)
        xml = bxml.decode('utf-8')
        dom = parseString(xml)
        pxml = dom.toprettyxml(indent='   ')
        return pxml

    @staticmethod
    def get(dict_obj, key, default_val=''):
        if MyDict.exist_key(dict_obj, key):
            return dict_obj[key]
        else:
            return default_val


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
