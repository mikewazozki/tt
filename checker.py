import requests
import SignerPy
import json
import secrets
import uuid
import binascii
import os
import time
import random
import re
from user_agent import generate_user_agent
import base64
from colorama import Fore
""" ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ """
telegram_anasxzer00 = 0
ssss = 0
sdfg = 0
anasUrFatherIfYouEditThisTool = 0
""" ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ """
def anasxzer00(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }
    for _ in range(10):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                html = response.text
                try:
                    data_part = html.split('''"userInfo":{"user":{''')[1].split('''</sc''')[0]
                    followers = data_part.split('"followerCount":')[1].split(',')[0]
                    likes = data_part.split('"heart":')[1].split(',')[0]
                    return followers, likes
                except Exception:
                    continue
        except Exception:
            continue
    return "N/A", "N/A"
def coincap(sessionid):
    cookies = {
        'sessionid': sessionid,
        'store-idc': 'alisg',
        'tt-target-idc': 'alisg',
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.tiktok.com',
        'priority': 'u=1, i',
        'referer': 'https://www.tiktok.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': generate_user_agent(),
    }
    params = {'aid': '1988'}
    try:
        response = requests.get(
            'https://webcast.tiktok.com/webcast/wallet_api/fs/diamond_buy/permission_v2',
            params=params,
            cookies=cookies,
            headers=headers,
            timeout=100
        )
        if response.status_code == 200:
            match = re.search(r'"coins_balance":(.*?),', response.text)
            if match:
                return match.group(1)
        return "N/A"
    except requests.exceptions.RequestException:
        return "N/A"
def xor(string):
    return "".join([hex(ord(c) ^ 5)[2:] for c in string])
url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
cog = secrets.token_hex(6*2+4)
email = input(" -- @anasxzer00 | TikTok Otp Login\n\n [+] Enter Email: ")
if not email:
    print("[-] Email is not registered.")
    exit()
params = {
    "": "",
    "request_tag_from": "h5",
    "fixed_mix_mode": "1",
    "mix_mode": "1",
    "account_param": xor(email),
    "scene": "4",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    'cdid': str(uuid.uuid4()),
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "300",
    "device_type": "G011A",
    "device_brand": "google",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "IQ",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752856167",
    "mcc_mnc": "41805",
    "timezone_name": "Kurdistan/Anas",
    "residence": "IQ",
    "app_language": "en",
    "carrier_region": "IQ",
    "timezone_offset": "28800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "IQ",
    "build_number": "37.8.5",
    "region": "GB",
    'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    'iid': str(random.randint(1, 10**19)),
    'device_id': str(random.randint(1, 10**19)),
    'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5"
}
cookies = {
    "store-idc": "alisg",
    "store-country-code": "iq",
    "store-country-code-src": "did",
    "store-country-sign": "MEIEDLeEK_cONptaosCixAQg5kOgozbqp-KCBg0OD5H9lk6kFUsnhLAIjAOEurGB52oEEK1IESIfzZeMzgqLA6denHg",
    "install_id": params["iid"],
    "ttreq": "1$ec4bb57aa77b1b98cdbbadd7bb9005108fed7e94",
    "odin_tt": "609e0b09c64907b11b9888f543fbe43c76e9b497f351a53a96a7030d66a88d66103a858283bd8ed51577848f4173baf707d1492fe813b01e4d8f18d16720bd0d227fb7fff4487f30eddd4f7bcdf80d76",
    "passport_csrf_token": cog,
    "passport_csrf_token_default": cog,
    "msToken": "p4XhlOoh4S7THTMLr_uwS2gs52Fx9s3bd5CFQuQ0xf6Q5AiYlguQKIgj9lQkckJYwAUNq3GGB1N-yXvFyZXUDzKZFnJUVPns8ZUvOgN-qhg=",
    "myCookie": "rap",
    "tt-target-idc": "useast1a"
}
client = requests.session()
client.cookies.update(cookies)
m = SignerPy.sign(params=params, cookie=cookies)
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-ss-stub': m['x-ss-stub'],
    'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
    'x-tt-pba-enable': "1",
    'x-tt-dm-status': "login=0;ct=1;rt=7",
    'x-ss-req-ticket': m['x-ss-req-ticket'],
    'x-tt-passport-csrf-token': cog,
    'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'passport-sdk-version': "6031990",
    'oec-vc-sdk-version': "3.0.5.i18n",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-request-tag': "n=0;nr=011;bg=0",
    'x-tt-pba-enable': "1",
    'x-ladon': m['x-ladon'],
    'x-khronos': m['x-khronos'],
    'x-argus': m['x-argus'],
    'x-gorgon': m['x-gorgon'],
    'content-type': "application/x-www-form-urlencoded",
    'content-length': m['content-length'],
}
response = client.post(url, headers=headers, params=params)
try:
    response_data = response.json()
    if (response.status_code != 200 or 
        "data" not in response_data or 
        not response_data["data"].get("accounts")):
        print("[-] Email is not registered.")
        exit()
    passport_ticket = response_data["data"]["accounts"][0]["passport_ticket"]
except (KeyError, IndexError, ValueError) as e:
    print("[-] Error parsing response:", e)
    print("[-] Email is not registered or API response format changed.")
    exit()
url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
params = {
    "": "",
    "request_tag_from": "h5",
    "passport_ticket": passport_ticket,
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": params["_rticket"],
    "cdid": params["cdid"],
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "300",
    "device_type": "G011A",
    "device_brand": "google",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "IQ",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752856167",
    "mcc_mnc": "41805",
    "timezone_name": "Kurdistan/Anas",
    "residence": "IQ",
    "app_language": "en",
    "carrier_region": "IQ",
    "timezone_offset": "28800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "IQ",
    "build_number": "37.8.5",
    "region": "GB",
    "ts": params["ts"],
    "iid": params["iid"],
    "device_id": params["device_id"],
    "openudid": params["openudid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5"
}
m = SignerPy.sign(params=params, cookie=cookies)
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-ss-stub': m['x-ss-stub'],
    'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
    'x-tt-pba-enable': "1",
    'x-tt-dm-status': "login=0;ct=1;rt=7",
    'x-ss-req-ticket': m['x-ss-req-ticket'],
    'x-tt-passport-csrf-token': cog,
    'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'passport-sdk-version': "6031990",
    'oec-vc-sdk-version': "3.0.5.i18n",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-request-tag': "n=0;nr=011;bg=0",
    'x-tt-pba-enable': "1",
    'x-ladon': m['x-ladon'],
    'x-khronos': m['x-khronos'],
    'x-argus': m['x-argus'],
    'x-gorgon': m['x-gorgon'],
    'content-type': "application/x-www-form-urlencoded",
    'content-length': m['content-length'],
}
response = client.post(url, headers=headers, params=params)
try:
    data = response.headers['X-Tt-Verify-Idv-Decision-Conf']
    loads = json.loads(data)
    passport_ticket2 = loads["passport_ticket"]
    pseudo_id = loads["extra"][0]["pseudo_id"]
except (KeyError, json.JSONDecodeError) as e:
    print("[-] Error parsing verification data:", e)
    exit()
url = "https://api16-normal-c-alisg.tiktokv.com/passport/aaas/authenticate/"
params = {
    "": "",
    "request_tag_from": "h5",
    "challenge_type": "2",
    "fixed_mix_mode": "0",
    "skip_handler": "error_handler",
    "pseudo_id": pseudo_id,
    "mix_mode": "0",
    "passport_ticket": passport_ticket2,
    "action": "3",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": params["_rticket"],
    "cdid": params["cdid"],
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "900*1600",
    "dpi": "300",
    "device_type": "G011A",
    "device_brand": "google",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "IQ",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752856167",
    "mcc_mnc": "41805",
    "timezone_name": "Kurdistan/Anas",
    "residence": "IQ",
    "app_language": "en",
    "carrier_region": "IQ",
    "timezone_offset": "28800",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "IQ",
    "build_number": "37.8.5",
    "region": "GB",
    "ts": params["ts"],
    "iid": params["iid"],
    "device_id": params["device_id"],
    "openudid": params["openudid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5"
}
payload = {
    'mix_mode': "0",
    'pseudo_id': pseudo_id,
    'challenge_type': "2",
    'action': "3",
    'passport_ticket': passport_ticket2,
    'skip_handler': "error_handler",
    'fixed_mix_mode': "0"
}
m = SignerPy.sign(params=params, cookie=cookies, payload=payload)
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; G011A; Build/PI;tt-ok/3.12.13.16)",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-ss-stub': m['x-ss-stub'],
    'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/idv_core/verification",
    'x-tt-pba-enable': "1",
    'x-tt-dm-status': "login=0;ct=1;rt=7",
    'x-ss-req-ticket': m['x-ss-req-ticket'],
    'x-tt-passport-csrf-token': cog,
    'tt-ticket-guard-public-key': "BCQmhkrziSw7zwWT4qKP1EhHohIqE38GlPThtUdY1mPsQRAi1YDMDTP7fBXkWQrDuGmunIjPvcyLvyvFBAC7KIk=",
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'passport-sdk-version': "6031990",
    'oec-vc-sdk-version': "3.0.5.i18n",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-request-tag': "n=0;nr=011;bg=0",
    'x-tt-pba-enable': "1",
    'x-ladon': m['x-ladon'],
    'x-khronos': m['x-khronos'],
    'x-argus': m['x-argus'],
    'x-gorgon': m['x-gorgon'],
}

response = client.post(url, data=payload, headers=headers, params=params)
print(" [!] Code sent to you'r email !")
time.sleep(2)
code = input(" [+] Enter OTP Code: ")
url = "https://api16-normal-c-alisg.tiktokv.com/passport/aaas/authenticate/"
params = {
    "request_tag_from": "h5",
    "challenge_type": "2",
    "fixed_mix_mode": "1",
    "code": xor(code),
    "skip_handler": "error_handler",
    "pseudo_id": pseudo_id,
    "mix_mode": "1",
    "passport_ticket": passport_ticket2,
    "action": "4",
    "iid": params["iid"],
    "device_id": params["device_id"],
    "ac": "WIFI",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "device_platform": "android",
    "os": "android",
    "ab_version": "37.8.5",
    "ssmix": "a",
    "device_type": params["device_type"],
    "device_brand": params["device_brand"],
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "openudid": params["openudid"],
    "manifest_version_code": "2023708050",
    "resolution": "1600*900",
    "dpi": "240",
    "update_version_code": "2023708050",
    "_rticket": params["_rticket"],
    "is_pad": "0",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Kurdistan/Erbil",
    "carrier_region_v2": "466",
    "app_language": "en",
    "carrier_region": params["carrier_region"],
    "ac2": "wifi",
    "uoo": "0",
    "op_region": params["carrier_region"],
    "timezone_offset": "10800",
    "build_number": "37.8.5",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "region": "GB",
    "ts": params["ts"],
    "cdid": params["cdid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5"
}
payload = {
    'mix_mode': "1",
    'code': xor(code),
    'pseudo_id': pseudo_id,
    'challenge_type': "2",
    'action': "4",
    'passport_ticket': passport_ticket2,
    'skip_handler': "error_handler",
    'fixed_mix_mode': "1"
}
m = SignerPy.sign(params=params, cookie=cookies, payload=payload)
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_US; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-ss-stub': m['x-ss-stub'],
    'x-tt-pba-enable': "1",
    'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
    'tt-ticket-guard-iteration-version': "0",
    'x-ss-req-ticket': m['x-ss-req-ticket'],
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'sdk-version': "2",
    'x-tt-dm-status': "login=0;ct=1;rt=6",
    'x-tt-passport-csrf-token': cog,
    'passport-sdk-version': "6031990",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-pba-enable': "1",
    'x-ladon': m['x-ladon'],
    'x-khronos': m['x-khronos'],
    'x-argus': m['x-argus'],
    'x-gorgon': m['x-gorgon'],
}
response = client.post(url, data=payload, headers=headers, params=params)
url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
params = {
    "request_tag_from": "h5",
    "passport_ticket": passport_ticket,
    "iid": params["iid"],
    "device_id": params["device_id"],
    "ac": "WIFI",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "device_platform": "android",
    "os": "android",
    "ab_version": "37.8.5",
    "ssmix": "a",
    "device_type": params["device_type"],
    "device_brand": params["device_brand"],
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "openudid": params["openudid"],
    "manifest_version_code": "2023708050",
    "resolution": "1600*900",
    "dpi": "240",
    "update_version_code": "2023708050",
    "_rticket": params["_rticket"],
    "is_pad": "0",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1752871588",
    "mcc_mnc": "46692",
    "timezone_name": "Kurdistan/Erbil",
    "carrier_region_v2": "466",
    "app_language": "en",
    "carrier_region": "TW",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "TW",
    "timezone_offset": "10800",
    "build_number": "37.8.5",
    "host_abi": "arm64-v8a",
    "locale": "en-GB",
    "region": "GB",
    "ts": params["ts"],
    "cdid": params["cdid"],
    "support_webview": "1",
    "okhttp_version": "4.2.210.6-tiktok",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5",
}
m = SignerPy.sign(params=params, cookie=cookies)
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_US; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
    'Accept': "application/json, text/plain, */*",
    'Accept-Encoding': "gzip",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-ss-stub': m['x-ss-stub'],
    'x-tt-pba-enable': "1",
    'tt-ticket-guard-public-key': "BHxT6qq83FTRAnJYjUgFDzwxX14GDgGVWmXnZftx8oJntWW03KYyAqdengSdAMgufFURdqiqF23x6RFV+F4593I=",
    'tt-ticket-guard-iteration-version': "0",
    'x-ss-req-ticket': m['x-ss-req-ticket'],
    'tt-ticket-guard-version': "3",
    'passport-sdk-settings': "x-tt-token",
    'passport-sdk-sign': "x-tt-token",
    'sdk-version': "2",
    'x-tt-dm-status': "login=0;ct=1;rt=6",
    'x-tt-passport-csrf-token': cog,
    'passport-sdk-version': "6031990",
    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
    'x-tt-pba-enable': "1",
    'x-ladon': m['x-ladon'],
    'x-khronos': m['x-khronos'],
    'x-argus': m['x-argus'],
    'x-gorgon': m['x-gorgon'],
    'content-type': "application/x-www-form-urlencoded",
    'content-length': m['content-length'],
}
response = client.post(url, headers=headers, params=params)
try:
    response_data = response.json()
    sessionid = response_data["data"]["session_key"]
    username = response_data["data"]["username"]
    followers, likes = anasxzer00(username)
    coins = coincap(sessionid)
    print("—"*60)
    print(" −−− Profile −−−")
    print(f" [×] Followers: {followers}")
    print(f" [×] Likes: {likes}")
    print(f" [×] Coins: {coins}")
    print(f" [×] SID: {sessionid}")
except Exception as e:
    print(f"[-] An unexpected error occurred: {e}")
    exit()
