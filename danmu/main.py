# 部分弹幕功能代码来自项目：https://github.com/IsoaSFlus/danmaku，感谢大佬
# 快手弹幕代码来源及思路：https://github.com/py-wuhao/ks_barrage，感谢大佬
# 仅抓取用户弹幕，不包括入场提醒、礼物赠送等。

import asyncio
import danmaku
from datetime import datetime
from time import sleep

records = []


async def recorder(q):
    global records
    while True:
        if len(records) < 10:
            m = await q.get()
            if m['msg_type'] == 'danmaku':
                cur_time = datetime.now()
                print(str(cur_time.strftime("%Y-%m-%d %H:%M:%S")) + " " + f'{m["name"]}：{m["content"]}')
                records.append(cur_time.strftime("%Y-%m-%d %H:%M:%S") + " " + f'{m["name"]}：{m["content"]}')
        else:
            await save_records()


async def save_records():
    record_path = "D:\\PycharmProjects\\real-url\\danmu\\records\\"
    global records
    with open(record_path + gen_record_filename(), "a", encoding="UTF-8") as f:
        f.write("\n".join(records) + "\n")
    print("##### RECORDS SAVED #####")
    records = []


async def main(url):
    q = asyncio.Queue()
    dmc = danmaku.DanmakuClient(url, q)
    asyncio.create_task(recorder(q))
    await dmc.start()


def gen_record_filename():
    return str(datetime.now().strftime("%Y_%m_%d_%H")) + "_00_00.txt"


if __name__ == '__main__':
    streaming_flag = True
    # room_url = input('请输入直播间地址：\n')
    # room_url = "https://www.huya.com/16844387"
    # room_url = "https://www.huya.com/sgjsheng"
    room_url = "https://www.huya.com/100"

    print("直播间地址：" + room_url)
    while True:
        try:
            asyncio.run(main(room_url))
        except AttributeError:
            if streaming_flag:
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " 未开播")
            streaming_flag = False
            sleep(3)

# 虎牙直播：https://www.huya.com/11352915
# 斗鱼直播：https://www.douyu.com/85894
# B站直播：https://live.bilibili.com/70155
# 快手直播：https://live.kuaishou.com/u/jjworld126
# 火猫直播：
# 企鹅电竞：https://egame.qq.com/383204988
# 花椒直播：https://www.huajiao.com/l/303344861?qd=hu
# 映客直播：https://www.inke.cn/liveroom/index.html?uid=87493223&id=1593906372018299
# CC直播：https://cc.163.com/363936598/
# 酷狗直播：https://fanxing.kugou.com/1676290
# 战旗直播：
# 龙珠直播：http://star.longzhu.com/wsde135864219
# PPS奇秀直播：https://x.pps.tv/room/208337
# 搜狐千帆直播：https://qf.56.com/520208a
# 来疯直播：https://v.laifeng.com/656428
# LOOK直播：https://look.163.com/live?id=196257915
# AcFun直播：https://live.acfun.cn/live/23682490
# 艺气山直播：http://www.173.com/96
