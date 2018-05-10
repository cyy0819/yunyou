import requests
import json


bus_id = "5af16bb9711f5e60edd74586"
url_1 = "http://api3.yunyouquan.top/"

def login():
    url = "http://api2.yunyouquan.top/login"
    d = {"mobile":"13671074279", "zone":"+86", "pass_word":"19930819"}
    r = requests.post(url, data=d)
    s = r.text
    d = json.loads(s)
    uid = d['data']['uid']
    token = d['data']['token']
    return uid, token


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




uid, token = login()
transaction(uid, token)





