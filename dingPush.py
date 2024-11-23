import requests
import json
import argparse
import time
import hmac
import hashlib
import base64
import urllib.parse

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername', required=True, help='请输入计算机名')
parser.add_argument('--internalip', required=True, help='请输入内部IP地址')
parser.add_argument('--username', required=True, help='请输入用户名')
args = parser.parse_args()
computername = args.computername
internalip = args.internalip
username = args.username

token = "xxx"  # 替换为您的钉钉机器人access_token
secret = "xxx"  # 替换为您的钉钉机器人密钥

timestamp = str(int(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
api_url = f"https://oapi.dingtalk.com/robot/send?access_token={token}&timestamp={timestamp}&sign={sign}"

def msg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "isAtAll": True  # 如果需要@所有人，保留此行；否则，可以删除或修改为特定用户的ID
        },
        "text": {
            "content": text
        }
    }
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    response = requests.post(api_url, data=json.dumps(json_text), headers=headers)
    print(response.content)

if __name__ == '__main__':
    text = "CobaltStrike主机上线提醒+1\n计算机名: {}\nIP地址: {}\n用户名: {}\n".format(computername, internalip, username)
    msg(text)
