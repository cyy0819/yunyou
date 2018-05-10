import requests
import json
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time


bus_id = "5af16bb9711f5e60edd74586"
url_1 = "http://api3.yunyouquan.top/"

def tt():
    t_ime = time.time()
    timestamp = int(t_ime)
    timestamp = str(timestamp)
    return timestamp

#login
def login():
    url = "http://api2.yunyouquan.top/login"
    d = {"mobile":"13671074279", "zone":"+86", "pass_word":"19930819"}
    r = requests.post(url, data=d)
    s = r.text
    d = json.loads(s)
    uid = d['data']['uid']
    token = d['data']['token']
    return uid, token


#maimaimai
def transaction(uid, token):
    uid = str(uid)
    url = url_1 + "transaction"
    # print(d['data']['bill']['count'])
    headers = {"uid":uid, "token":token}
    d1 = {'to_uid':uid, 'count': '1000000',
          'pay_type':'cib', 'gold_type':'gmot', 'bill_id':''}
    r = requests.get(url, data=d1, headers=headers)
    s = r.text
    d = json.loads(s)
    print(d)

#mai
def cash(uid, token):
    uid = str(uid)
    url = url_1 + "cash"
    headers = {"uid":uid, "token":token}
    d = {"count":1000000, "pay_pwd":"930819", "pay_type":"cib", "gold_type":"gmot"}
    r = requests.post(url, data=d, headers=headers)
    s = r.text
    d = json.loads(s)
    print(d)


def add_to_16(value):
    tmp_val = value.encode('utf-8')
    m = 16 - (len(tmp_val) % 16)
    if m != 0:
        for i in range(m):
            value += '\0'
    return str.encode(value)

def secret(value):
    # print(value)
    key = '054eda8889ea6240'
    text = {"time":1000000000,
            "title":"银行","fromWay":"招商",
            "billNum":tt(),
            "money":value['data']['bill']['need_money'],
            "status":"1"}
    text = json.dumps(text)
    print(text)
    aes = AES.new(key.encode("utf-8"), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_16(text))
    text = b2a_hex(encrypt_aes)
    text = str(text, encoding=('utf-8'))
    return text

def decrypt(text):
    key = '054eda8889ea6240'
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    plain_text = aes.decrypt(a2b_hex(text))
    ss = str(plain_text, encoding='utf-8')
    ss = ss.rstrip('\0')
    return ss

def simulator_g():
    ur_l = url_1 + "simulator?device_id=6a9fb40480f966e9&business_id=" + bus_id
    url = ur_l
    r = requests.get(url)
    s = r.text
    d = json.loads(s)
    return d

def simulator_p(d, t):
    url = url_1 + "simulator"
    d = {'bill_id':str(d['data']['bill']['_id']),
         'bill_type':str(d['data']['bill']['bill_type']),
         'pay_result':t, 'device_id':'6a9fb40480f966e9',
         'business_id':bus_id}
    # print(d)
    r = requests.post(url, data=d)
    s = r.text
    d = json.loads(s)
    print(d)

def secret_out():
    key = '054eda8889ea6240'
    text_out = {"BizNo":tt()}
    text_out = json.dumps(text_out)
    print(text_out)
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_16(text_out))
    text_out = b2a_hex(encrypt_aes)
    text_out = str(text_out, encoding=('utf-8'))
    return text_out

def decrypt_out(text):
    key = '054eda8889ea6240'
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    plain_text = aes.decrypt(a2b_hex(text))
    ss = str(plain_text, encoding='utf-8')
    ss = ss.rstrip('\0')
    return ss


def fac(num):
    for i in range(1, num+1):
        print(i)
        uid, token = login()
        cash(uid, token)
        d = simulator_g()
        if d['data']['bill']['bill_type'] == 1:
            text = secret(d)
            print(text)
            ss = decrypt(text)
            print(ss)
            simulator_p(d, text)
        else:
            text_out = secret_out()
            print(text_out)
            ds = decrypt_out(text_out)
            print(ds)
            simulator_p(d, text_out)
        print("-----------------------------")



def fn(num):
    for i in range(1, num+1):
        print(i)
        uid, token = login()
        transaction(uid, token)
        d = simulator_g()
        if d['data']['bill']['bill_type'] == 1:
            text = secret(d)
            print(text)
            ss = decrypt(text)
            print(ss)
            simulator_p(d, text)
        else:
            text_out = secret_out()
            print(text_out)
            ds = decrypt_out(text_out)
            print(ds)
            simulator_p(d, text_out)
        print("-----------------------------")


# num = int(input("num:"))
# value = input("value:")
#
# if value == 'b':
#     fn(num)
# else:
#

# fn(1)
fac(1)


