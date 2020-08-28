import os


class MyPath:
    @staticmethod
    def work_root():
        """
        获取工作目录
        :return: 工作目录的路径
        """
        return os.getcwd()

    @staticmethod
    def mkdir(path):
        """
        创建目录，中间目录不存在时，同时创建
        :param path: 目录
        :return: True--成功；False--失败
        """
        try:
            # 去除首尾空格
            path = path.strip()
            if not os.path.exists(path):
                os.makedirs(path)
            return True
        except OSError:
            return False

    @staticmethod
    def join_file_path(file_path, folder=None):
        """
        连接目录和文件路径（在文件路径前加上父目录）
        :param file_path: 文件路径
        :param folder: 文件路径的父目录，默认无父目录
        :return: 连接目录后的新路径
        """
        if folder is not None:
            return os.path.join(folder, file_path)
        else:
            return file_path

    @staticmethod
    def is_folder(folder):
        return os.path.isdir(folder)

    @staticmethod
    def exist(folder, parent=None):
        """
        检查指定目录是否存在
        :param folder: 目录路径
        :param parent: 目录的父目录，默认无父目录
        :return: 存在 True，不存在 False
        """
        return os.path.exists(MyPath.join_file_path(folder, parent))

    @staticmethod
    def del_folder(folder):
        """
        递归地删除目录。如果子目录成功被删除，则将会成功删除父目录，子目录没成功删除，将抛异常。
        :param folder: 指定要删除的目录
        :return: 无
        """
        if MyPath.exist(folder):
            os.removedirs(folder)

    @staticmethod
    def check_filepath(path):
        """
        检查路径，没有则创建 -- obsolete
        :param path: 路径
        :return: True 新建， False 已存在
        """
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在 # 存在     True        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False



