import os
import chardet


class MiscUtil:
    ###
    @classmethod
    def detect_file_encoding(cls, file_path: str):
        with open(file_path, "rb") as fp:
            file_encoding = chardet.detect(fp.read())["encoding"]
        return file_encoding
