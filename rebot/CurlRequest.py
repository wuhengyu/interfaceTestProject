# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 13:37
# @Author  : Walter
# @File    : CurlRequest.py
# @License : (C)Copyright Walter
# @Desc    :
import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ecd59711-cade-4fe4-9f57-960f4e5d135f"

payload = {
    "msgtype": "markdown",
    "markdown": {
        "content": "实时新增用户反馈<font color=\"warning\">132例</font>，"
                   "请相关同事注意。>类型:<font color=\"comment\">用户反馈</font>>"
                   "普通用户反馈:<font color=\"comment\">117例</font>>"
                   "VIP用户反馈:<font color=\"comment\">15例</font>"
    }
}

payload2 = {
    "msgtype": "news",
    "news": {
        "articles": [
            {
                "title": "中秋节礼品领取",
                "description": "今年中秋节公司有豪礼相送",
                "url": "www.qq.com",
                "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
            }
        ]
    }
}
response = requests.post(url, json=payload2)
