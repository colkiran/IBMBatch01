import json

import requests

BASE = "http://127.0.0.1:5000/"

print("get".center(60,"-"))
response = requests.get(BASE + "getproduct/coke")
res = response.json()
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))

print("put".center(60, "-"))

response = requests.put(BASE + 'getproduct/coke', data = {'cat': 'baverage'})
res = response.json()
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))


print("post".center(60, "-"))
fanta = {'type': '500 ml bottle', 'price':70, 'qty': 200}

response = requests.post(BASE + 'getproduct/fanta',
        json = json.dumps(fanta))

res = response.json()
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for ky, vl in info.items():
        print(ky, "=>", vl)

print("patch".center(60,"-"))
# coke price to be changed
# data = {'price': 5000, 'qty': 50000}
data = {'price': 5000}

response = requests.patch(BASE + 'getproduct/coke', json= json.dumps(data))
print(response.json())

print("Delete Method".center(60, "-"))

response = requests.delete(BASE + 'getproduct/pepsi')
res = response.json()
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for ky, vl in info.items():
        print(ky, "=>", vl)
    print("-" * 60)

