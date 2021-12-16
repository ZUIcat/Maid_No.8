import os
import time

from common import *


def check_network_connection() -> bool:
    test_url: str = "www.baidu.com"
    test_command: str = f"ping {test_url} >> nul"
    ret_code: int = os.system(test_command)
    return ret_code == 0


def hibernate_computer() -> None:
    command: str = "rundll32.exe powrprof.dll,SetSuspendState"
    os.system(command)


def main():
    lag_time: float = 10 * 60
    log_file_path: str = os.path.join(CommonData.DIR_PATH, "applog.log")
    connection_error_lag_time: float = 30
    connection_error_max_retry_num: int = 5
    hibernate_lag_time: float = 60

    os.makedirs(CommonData.DIR_PATH, exist_ok=True)
    logger.set_write_to_external(log_file_path)

    logger.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} Start ===")

    while True:
        network_connection = check_network_connection()
        logger.log(f"The network connection state is: {network_connection}")

        if not network_connection:
            logger.error("Retry start...")
            retry_ret: bool = False
            for i in range(connection_error_max_retry_num):
                network_connection = check_network_connection()
                logger.log(f"(Retry {i + 1:02}) The network connection state is: {network_connection}")
                if network_connection:
                    retry_ret = True
                    break
                time.sleep(connection_error_lag_time)
            logger.error("Retry end...")

            if not retry_ret:
                logger.error("Try to hibernate the computer.")
                hibernate_computer()
                time.sleep(hibernate_lag_time)

        time.sleep(lag_time)

    logger.log(f"=== The {CommonData.APP_NAME} v{CommonData.APP_VER} End ===")


if __name__ == "__main__":
    main()
