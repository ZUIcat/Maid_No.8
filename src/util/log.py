import threading
import datetime
from typing import Optional


class LogUtil:
    ###
    # __instance = None
    # __instance_lock = threading.Lock()

    ###
    log_msg = {"tag": "LOG", "level": 1}
    warn_msg = {"tag": "WAR", "level": 1}
    error_msg = {"tag": "ERR", "level": 1}
    dev_msg = {"tag": "DEV", "level": 2}

    ###
    __msg_level: int = 1  # 1:normal 2:dev
    __write_to_external_path: Optional[str] = None

    # @classmethod
    # def instance(cls):
    #     with cls. __instance_lock:
    #         if cls.__instance is None:
    #             cls.__instance = cls()
    #     return cls.__instance

    # def __init__(self):
    #     print("__init__")

    @classmethod
    def set_msg_level(cls, msg_level: int):
        cls.__msg_level = msg_level

    @classmethod
    def get_msg_level(cls) -> int:
        return cls.__msg_level

    @classmethod
    def set_write_to_external(cls, write_to_external: Optional[str]):
        cls.__write_to_external_path = write_to_external

    @classmethod
    def get_write_to_external(cls) -> Optional[str]:
        return cls.__write_to_external_path

    @classmethod
    def __output_msg(cls, msg_type, *args: object):
        tag = msg_type["tag"]
        level = msg_type["level"]
        if level > cls.__msg_level:
            return
        print(f"[{tag}][{cls.get_now_time_str()}]", *args)
        if cls.__write_to_external_path is not None:
            # TODO 始终持有文件句柄 而不是每次打开
            with open(cls.__write_to_external_path, mode="a+", encoding="UTF-8") as fp:
                print(f"[{tag}][{cls.get_now_time_str()}]", *args, file=fp)

    @classmethod
    def log(cls, *args: object):
        cls.__output_msg(cls.log_msg, *args)

    @classmethod
    def warn(cls, *args: object):
        cls.__output_msg(cls.warn_msg, *args)

    @classmethod
    def error(cls, *args: object):
        cls.__output_msg(cls.error_msg, *args)

    @classmethod
    def dev(cls, *args: object):
        cls.__output_msg(cls.dev_msg, *args)

    ###
    @classmethod
    def get_now_time_str(cls) -> str:
        # return time.strftime("%Y/%m/%d %H:%M:%S")
        now_time: datetime.datetime = datetime.datetime.now()
        return f"{now_time.year:04}/{now_time.month:02}/{now_time.day:02} {now_time.hour:02}.{now_time.minute:02}.{now_time.second:02}.{now_time.microsecond:06}"
