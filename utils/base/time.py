from datetime import date, datetime, timedelta
# from dateutil.relativedelta import relativedelta
import json
import time


class TimeEncoder(json.JSONEncoder):
    """
    用于 json.dumps 中对时间性的对象格式化成字符串
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class MyTime:
    @staticmethod
    def sleep(seconds):
        """
        当前进程或线程睡眠 seconds 秒，可以是浮点数
        :param seconds: 睡眠秒数，比如2秒、0.05秒
        :return: 无
        """
        time.sleep(seconds)

    @staticmethod
    def get_now_time():
        return datetime.now()

    @staticmethod
    def get_now_time_str():
        return MyTime.get_now_time().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def parse_time_str(time_str):
        """
        对输入字符串按时间格式解析成时间对象
        :param time_str: 含时间的字符串
        :return: 时间
        """
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def elapsed_time_ms(start_time):
        """
        从指定的起始时间，计算当前已用去多少毫秒
        :param start_time: 起始时间 （datetime 类型）
        :return: 已用毫秒数
        """
        now_time = MyTime.get_now_time()
        delta_time = now_time - start_time
        return delta_time.seconds * 1000.0 + delta_time.microseconds / 1000.0

    @staticmethod
    def get_time_delta_days(delta_days):
        """
        从当前时间开始，计算 n 天后的时间
        :param delta_days: 天数
        :return: n 天后的时间 （datetime 类型）
        """
        now = datetime.now()
        new_time = now + timedelta(days=delta_days)
        return new_time

    # @staticmethod
    # def get_time_delta_years(delta_years):
    #     now = datetime.now()
    #     new_time = now + relativedelta(years=delta_years)
    #     return new_time

    @staticmethod
    def print_time(time):
        print(time)
