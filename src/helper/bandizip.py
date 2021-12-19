import os
from pathlib import Path
from typing import Optional


# https://www.bandisoft.com/bandizip/help/parameter/
class BandizipHelper:
    @classmethod
    def check_availability(cls) -> int:
        command: str = r"where bandizip 1>nul 2>nul"
        ret_code: int = os.system(command)
        return ret_code

    @classmethod
    def unzip_file(cls, file_path: str, password: Optional[str] = None) -> int:
        file_self_path: Path = Path(file_path).resolve(True)
        file_parent_dir: Path = file_self_path.parent
        command: str = ""
        if password is None:
            command = fr'bandizip bx -target:name -o:"{file_parent_dir}" "{file_self_path}"'
        else:
            command = fr'bandizip bx -target:name -p:{password} -o:"{file_parent_dir}" "{file_self_path}"'
        ret_code: int = os.system(command)
        return ret_code

    @classmethod
    def unzip_file_auto(cls, file_path: str, password: Optional[str] = None) -> int:
        file_self_path: Path = Path(file_path).resolve(True)
        file_parent_dir: Path = file_self_path.parent
        command: str = ""
        if password is None:
            command = fr'bandizip bx -target:auto -o:"{file_parent_dir}" "{file_self_path}"'
        else:
            command = fr'bandizip bx -target:auto -p:{password} -o:"{file_parent_dir}" "{file_self_path}"'
        ret_code: int = os.system(command)
        return ret_code
