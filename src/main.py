import os
import time

from common import *


def main():
    lag_time: float = 10 * 60
    log_file_path: str = os.path.join(CommonData.DIR_PATH, "applog.log")
    connection_error_lag_time: float = 30
    connection_error_max_retry_num: int = 5
    hibernate_lag_time: float = 60

    os.makedirs(CommonData.DIR_PATH, exist_ok=True)
    LogUtil.set_write_to_external(log_file_path)

    LogUtil.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} Start ===")

    while True:
        network_connection = Win32Util.check_network_connection() == 0
        LogUtil.log(f"The network connection state is: {network_connection}")

        if not network_connection:
            LogUtil.error("Retry start...")
            retry_ret: bool = False
            for i in range(connection_error_max_retry_num):
                network_connection = Win32Util.check_network_connection() == 0
                LogUtil.log(f"(Retry {i + 1:02}) The network connection state is: {network_connection}")
                if network_connection:
                    retry_ret = True
                    break
                time.sleep(connection_error_lag_time)
            LogUtil.error("Retry end...")

            if not retry_ret:
                LogUtil.error("Try to hibernate the computer.")
                Win32Util.hibernate_computer()
                time.sleep(hibernate_lag_time)

        time.sleep(lag_time)

    LogUtil.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} End ===")


if __name__ == "__main__":
    main()
