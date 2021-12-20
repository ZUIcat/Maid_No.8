import os
from common import *


def main() -> int:
    # file_max_size: int = 1
    file_max_size: int = 50 * 1024 * 1024
    delete_after_extract: bool = True
    log_file_path: str = os.path.join(CommonData.DIR_PATH, "applog.log")

    os.makedirs(CommonData.DIR_PATH, exist_ok=True)
    LogUtil.set_write_to_external(log_file_path)

    ret_code: int = BandizipHelper.check_availability()
    if ret_code == 0:
        LogUtil.log("The status of the Bandizip is fine.")
    else:
        LogUtil.error(f"Cannot find the location of the Bandizip! Error code: {ret_code}")
        return -1

    dir_path: str = PathUtil.remove_quotes(input("Drag in the root dir: "))
    file_path_list = PathUtil.walk_files(dir_path, [".rar", ".zip", ".7z"])  # TODO 分卷压缩包

    file_path_list = [file_path for file_path in file_path_list if PathUtil.get_path_size(file_path) > file_max_size]

    if len(file_path_list) == 0:
        LogUtil.log("Cannot find any files in the path.")
        return -1

    LogUtil.log("These files will be extract below: ")
    for file_path in file_path_list:
        LogUtil.log(f"{file_path}")

    if input("Press Y to confirm: ") != "Y":
        LogUtil.error("The user canceled.")
        return -1

    LogUtil.log("Start extracting: ")
    for file_path in file_path_list:
        LogUtil.log(f"Extracting the {file_path}")
        ret_code = BandizipHelper.unzip_file(file_path)
        if ret_code == 0:
            if delete_after_extract:
                LogUtil.log(f"Try to delete {file_path}")
                Win32Util.del_to_trash(file_path)  # TODO 分卷压缩包
        else:
            LogUtil.error(f"Cannot extract the file {file_path}")
    LogUtil.log("Extracting finished.")

    return 0


if __name__ == "__main__":
    LogUtil.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} Start ===")
    main_ret_code = main()
    LogUtil.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} End With {main_ret_code} ===")
    input("Press any key to exit.")
