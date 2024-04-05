


import re

st = "baaaaaaaaaaaaaaaaat"

res = re.search(r'ba{3,}t', st)

print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched my regex
else:
    print("Match not found....")
