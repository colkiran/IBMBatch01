
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/coke")
res = response.json()
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))

print("-" * 60)

response = requests.put(BASE + 'getproduct/coke', data = {'cat': 'baverage'})
res = response.json()
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))

print("-" * 60)

response = requests.post(BASE + 'getproduct/fanta', data = {'fanta' :{'type': '500 ml bottle', 'price':70, 'qty': 200}})
print(response.json())

print("-" * 60)

response = requests.delete(BASE + 'getproduct/pepsi')
print(response.json())


"""
# response = requests.patch(BASE + 'getproduct/coke', data = {'type': '1 ltr bottle'})
# print(response.json())


for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))

"""