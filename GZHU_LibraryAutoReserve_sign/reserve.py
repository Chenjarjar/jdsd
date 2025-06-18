"""
预约
"""

from libs.info import infos
from libs.source import ZWYT
import time

def main(*args, **kwargs):
    # 遍历 info 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段、推送token（推送可以为空）
    for stu in infos:
        retry_count = 100  # 设置最大重试次数
        while retry_count > 0:
            try:
                # 初始化类示例，传入昵称、用户名、密码、时间段、推送token（推送可以为空）
                yy = ZWYT(
                    stu["name"], stu["sno"], stu["pwd"], stu["periods"], stu["pushplus"]
                )

                # 调用预约函数预约，传入预约座位号
                yy.reserve(stu["devName"])
                break  # 如果成功，跳出重试循环
            except Exception as e:
                print(f"尝试失败: {e}")
                retry_count -= 1  # 减少重试次数
                if retry_count == 0:  # 如果重试次数用完
                    print(f"{stu['name']} {stu['devName']} 预约失败，已达到最大重试次数")
                    if stu["pushplus"]:
                        yy.pushplus(f"{stu['name']} {stu['devName']} 预约失败", e)
                else:
                    print(f"重试中，剩余次数: {retry_count}")
                    time.sleep(5)  # 每次重试前等待 5 秒
                continue


if __name__ == "__main__":
    main()
