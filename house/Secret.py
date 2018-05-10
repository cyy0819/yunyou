from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time
import requests
import json


bus_id = "5af16bb9711f5e60edd74586"
url_1 = "http://api3.yunyouquan.top/"

def tt():
    t_ime = time.time()
    timestamp = int(t_ime)
    timestamp = str(timestamp)
    return timestamp


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

def simulator_g():
    url = url_1 + "simulator" \
          "?device_id=6a9fb40480f966e9&business_id=" + bus_id
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

# mairu
# d = simulator_g()
# print(d)
# text = secret(d)
# print(text)
# ss = decrypt(text)
# print(ss)
# simulator_p(d, text)


#maichu
d = simulator_g()
text = secret_out()
print(decrypt_out(text))
simulator_p(d, text)






