

import re

st = "bct"

# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)

res = re.search(r'b[^aeiou]t', st)

print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched my regex
else:
    print("Match not found....")
