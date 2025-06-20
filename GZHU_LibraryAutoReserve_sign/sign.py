"""
签到
"""
from libs.info import infos
from libs.source import ZWYT


def main(*args, **kwargs):
    # 遍历 info 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段、推送token（推送可以为空）
    for stu in infos:
        retry_count = 100  # 设置最大重试次数
        while retry_count > 0:
            try:
                # 初初始化类示例，传入昵称、用户名、密码、时间段、推送token（推送可以为空）
                yy = ZWYT(stu['name'], stu['sno'], stu['pwd'], stu['periods'], stu['pushplus'])

                # 调用签到函数进行签到，传入预约座位号
                yy.sign(stu['devName'])
                break
            except Exception as e:
                retry_count -= 1
                print(f"剩余重试次数:{retry_count}")
                print(e)
                if stu['pushplus']:
                    yy.pushplus(f"{stu['name']} {stu['devName']} 签到失败", e)
                continue


if __name__ == '__main__':
    main()
