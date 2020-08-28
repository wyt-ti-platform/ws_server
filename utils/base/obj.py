class MyObj:
    @staticmethod
    def props_list(cls):
        """
        获取指定类的所有属性，不含属性的值
        也可以采用 vars(cls) 获得所有的函数、变量的 mappingproxy，再用dict转成字典
        :param cls: 类
        :return: 类属性的列表
        """
        props_list = dir(cls)
        return props_list

    @staticmethod
    def kv_list(cls):
        """
        可以获取类中属性及其值，但函数不能进行JSON序列化
        :param cls: 类
        :return: 属性及值的键值对（字典）
        """
        vars_list = vars(cls)
        props_list = dict(vars_list)
        return props_list
