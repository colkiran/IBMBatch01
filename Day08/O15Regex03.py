


import re

st = "baaaaaaaaaaaaaaaaaaaaaaaat"

res = re.search(r'ba*t', st)

print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched my regex
else:
    print("Match not found....")
