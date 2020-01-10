#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys
import os
import time
import base64
import jwt
import gzip

from middleware.telegram import send_telegram
from middleware.supersign import SuperSign
from middleware.logger import logger
from config import super_signature, apple_url, remind_count, message

# 获取上级目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取当前脚本路径
cur_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 复制超级签接口数据
super_signature_d = super_signature.copy()

# 循环获取超级签账号信息
logger.info(f"\n"*5)
for customer in super_signature_d.keys():

    # 测试一些数据
    # if customer != "leying": continue

    message['text'] = f"超级签\r\n业主: {customer}\r\n"

    logger.info(f"#"*100)
    logger.info(f"开始操作 业主: {customer}")
    
    super_url = super_signature_d[customer]["url"]
    logger.info(f"超级签URL: {super_url}")

    # 获取超级签账号信息
    ss = SuperSign(super_url)
    data = ss.get_data()['data']

    # 循环数据，筛选得到所剩名额
    remain_all = 0

    if data:
        for acc in data:
            account = acc['account']
            count = acc['count']
            message['text'] += f"{account}: {str(count)}\r\n"
            logger.info(f"{account}: {str(count)}")
            remain_all += count

        message['text'] += "\r\n".join([
                "所剩名额总数: %s" %remain_all,
                # "%s: %s" %(department.department, ", ".join(name)),
            ])

        # 发送预警信息
        message['group'] = "arno_test2"
        if remain_all <= remind_count:
            message['group'] = "yunwei"
        send_telegram(message)

