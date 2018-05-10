import requests
import json

def login():
    url = "http://api2.yunyouquan.top/login"
    d = {"mobile":"13671074279", "zone":"+86", "pass_word":"19930819"}
    r = requests.post(url, data=d)
    s = r.text
    d = json.loads(s)
    uid = d['data']['uid']
    token = d['data']['token']
    return uid, token



def cash(uid, token):
    uid = str(uid)
    url = "http://api2.yunyouquan.top/cash"
    headers = {"uid":uid, "token":token}
    d = {"count":9000, "pay_pwd":"930819", "pay_type":"cib", "gold_type":"gmot"}
    r = requests.post(url, data=d, headers=headers)
    s = r.text
    d = json.loads(s)
    print(d)


uid, token = login()
# d = simulator_g()
# print(d)
cash(uid, token)