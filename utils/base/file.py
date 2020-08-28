import base64
import os
import shutil
from .path import MyPath
from .str import MyStr


class MyFile:

    @staticmethod
    def read(file_path, folder=None, read_len=0):
        """
        按二进制格式读取文件内容
        :param file_path: 文件路径
        :param folder: 文件路径的父目录，默认无父目录
        :param read_len: 读取数据长度，默认所有内容
        :return: 读取的内容（二进制），IO 异常时返回 None
        """
        file_path = MyPath.join_file_path(file_path, folder)
        try:
            with open(file_path, 'rb') as file:
                if read_len == 0:
                    contents = file.read()
                else:
                    contents = file.read(read_len)
        except IOError as io_err:
            return None

        return contents

    @staticmethod
    def read_text(file_path, folder=None, read_len=0):
        """按文本格式（可打印字符）读取文件内容，参数含义参见 read() """
        contents = MyFile.read(file_path, folder, read_len)
        if contents is None:
            return None
        return MyStr.bytes2str(contents)

    @staticmethod
    def read_and_b64encode(file_path, folder=None, read_len=0):
        """
        从文件中读取二进制数据后，采用base64编码后，返回编码结果
        :param file_path: 文件路径
        :param folder: 文件路径的父目录，默认无父目录
        :param read_len: 读取数据长度，默认所有内容
        :return: 读取数据的 base64 编码，或 None
        """
        contents = MyFile.read(file_path, folder, read_len)
        if contents is None:
            return None
        return base64.b64encode(contents).decode()

    @staticmethod
    def write(file_path, bin_data, folder=None):
        """
        在文件中写入二进制数据
        :param file_path: 文件路径
        :param bin_data: 二进制数据
        :param folder: 文件路径的父目录，默认无父目录
        :return: 成功 True，失败或异常 False
        """
        file_path = MyPath.join_file_path(file_path, folder)
        try:
            with open(file_path, 'wb') as file:
                w_len = file.write(bin_data)
        except IOError as io_err:
            return False

        return w_len > 0

    @staticmethod
    def exist(file_path, folder=None):
        """
        检查指定文件是否存在
        :param file_path: 文件路径
        :param folder: 文件路径的父目录，默认无父目录
        :return: 存在 True，不存在 False
        """
        return os.path.exists(MyPath.join_file_path(file_path, folder))

    @staticmethod
    def is_file(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def del_file(file_path):
        """
        删除文件，只有存在的文件才会删除，如果是目录不做任何操作
        :param file_path: 文件路径
        :return: 无
        """
        if MyFile.exist(file_path):
            os.remove(file_path)

    @staticmethod
    def get_folder(file_path):
        return os.path.dirname(file_path)

    @staticmethod
    def get_folder_and_file(file_path):
        path_list = os.path.split(file_path)
        if len(path_list) > 1:
            return path_list[0], path_list[1]
        elif len(path_list) == 1:
            return path_list[0], ''
        else:
            return '', ''

    @staticmethod
    def get_drive(file_path):
        file_drive = os.path.splitdrive(file_path)
        return file_drive[0] if len(file_drive) > 0 else ''

    @staticmethod
    def get_suffix(file_path):
        path_list = os.path.splitext(file_path)
        if len(path_list) > 1:
            return path_list[1]
        else:
            return ''

    @staticmethod
    def file_path_to_folder_list(file_path):
        """
        返回 folders list 和 file_name
        :param file_path: file_path
        :return: 一个目录列表，一个文件名
        """
        # 判断文件路径的分隔符
        delimiter = '\\' if file_path.find('\\') >= 0 else '/'

        # 移除首尾的分隔符
        file_path = file_path.strip(delimiter)

        # 空串，folders_list 和 file_name 都为空
        if len(file_path) == 0:
            return [], ''
        # elif file_path.find(delimiter) < 0:
        #     # 非空串，但找不到分隔符，则当前 file_path 即为 file_name
        #     return [], file_path

        # 分隔字符串成字符串列表
        folders_list = file_path.split(delimiter)
        # 列表最后一个元素为 file_name，剩余的留作 folders_list
        file_name = folders_list[-1]
        folders_list.pop()
        return folders_list, file_name

    @staticmethod
    def copy(src_file, dest_path):
        """
        拷贝文件
        :param src_file: 源文件
        :param dest_path: 目标文件或目标路径，如果是路径，则在其中创建一个与源文件相同名称的新文件
        :return: True: 拷贝成功；False：拷贝失败
        """
        try:
            shutil.copy(src_file, dest_path)
        except IOError as e:
            return False
        return True

