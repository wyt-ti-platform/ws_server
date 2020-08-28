class MyList:
    @staticmethod
    def parse_str(str, splitter=' '):
        """ 对字符串按分隔符分割，转化成列表"""
        return str.split(splitter)

    @staticmethod
    def to_str(src_list, joiner=' '):
        """ 列表各元素用指定的分隔符连接"""
        return joiner.join(src_list)

    @staticmethod
    def remove(src_list, ele):
        """从列表移除一个元素"""
        src_list.remove(ele)

    @staticmethod
    def join(list1, list2):
        """ 连接两个列表"""
        return list1 + list2

    @staticmethod
    def extend(base_list, new_list):
        """在一个列表的尾部扩展另一个列表的元素"""
        base_list.extend(new_list)
