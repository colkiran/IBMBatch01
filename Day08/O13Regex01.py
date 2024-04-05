
import re

st = "b#t"

res = re.match(r'b.t', st)
print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched my regex
else:
    print("Match not found....")