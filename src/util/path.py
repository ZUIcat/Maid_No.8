import os
import pathlib
from typing import List, Tuple


class PathUtil:
    ###
    @classmethod
    def remove_quotes(cls, input_path: str):
        if input_path.startswith('"') and input_path.endswith('"'):
            input_path = input_path[1:-1]
        return input_path

    @classmethod
    def walk_dirs(cls, father_dir_path: str):
        dir_path_list = []
        for dir_path, _, _ in os.walk(father_dir_path):
            dir_path_list.append(dir_path)
        del dir_path_list[0]
        return dir_path_list

    @classmethod
    def walk_files(cls, root_dir_path: str, file_exts: List[str]) -> List[str]:
        file_path_list = []
        for dir_path, _, file_names in os.walk(root_dir_path):
            for file_name in file_names:
                for file_ext in file_exts:
                    if file_name.lower().endswith(file_ext.lower()):
                        file_path_list.append(
                            os.path.join(dir_path, file_name))
                        break
        return file_path_list

    @classmethod
    def get_path_size(cls, file_path: str) -> int:
        path_size = pathlib.Path(file_path).stat().st_size
        return path_size
