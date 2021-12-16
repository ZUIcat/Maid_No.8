import os
from typing import Optional


# https://www.bandisoft.com/bandizip/help/parameter/
class BandizipHelper:
    @classmethod
    def check_availability(cls) -> bool:
        command: str = r"where bandizipd 1>nul 2>nul"
        ret_code: int = os.system(command)
        return ret_code == 0

    @classmethod
    def unzip_file_auto(cls, file_path: str, password: Optional[str]) -> bool:
        file_dir: str = ""
        file_name: str = ""
        command: str = fr"bandizip bx -target:auto -o:{file_dir} {file_name}" if password is None else fr"bandizip bx -target:auto -p:{password} -o:{file_dir} {file_name}"
        ret_code: int = os.system(command)
        return ret_code == 0
