import os
import pathlib
from typing import List, Union
from send2trash import send2trash


class Win32Util:
    ###
    @classmethod
    def del_to_trash(cls, paths: Union[str, pathlib.Path, List[str], List[pathlib.Path]]):
        send2trash(paths)

    @classmethod
    def check_network_connection(cls) -> int:
        test_url: str = "www.baidu.com"
        test_command: str = fr"ping {test_url} 1>nul 2>nul"
        ret_code: int = os.system(test_command)
        return ret_code

    @classmethod
    def hibernate_computer(cls) -> int:
        command: str = r"rundll32.exe powrprof.dll,SetSuspendState"
        ret_code: int = os.system(command)
        return ret_code
