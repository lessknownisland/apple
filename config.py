#!/usr/bin/env python3
#-_- coding: utf-8 -_-

# 各家 超级签接口
super_signature = {
    "ali": {
        "url": "https://alisuper.le079.com/apple/getAllAppleAccounts",
        "error": ""
        },
    "leying": {
        "url": "https://lysuper.le079.com/apple/getAllAppleAccounts",
        "error": ""
        },
    "guangda": {
        "url": "https://gdsuper.le079.com/apple/getAllAppleAccounts",
        "error": ""
        },
    "uc": {
        "url": "https://ucsuper.le079.com/apple/getAllAppleAccounts",
        "error": ""
        },
    "58yl": {
        "url": "https://58ylsuper.le079.com/apple/getAllAppleAccounts",
        "error": ""
        },
    }

apple_url = "https://api.appstoreconnect.apple.com/v1/apps"

remind_count = 100

# telegram 信息
message = {} # 信息主体
message['group'] = 'arno_test2'
message['bot']   = 'sa_monitor_bot'
message['text']  = ""
message['doc']   = False
message['doc_name'] = "warning.txt"

if "__name__" == "__main__":
    print ("no no no")