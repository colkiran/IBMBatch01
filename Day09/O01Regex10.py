
"""
.   -  single character
^   -   begning of the string
$   -   end of the string

*   -   zero or more occurances
?   -   zero or one occurances
+   -   one or more occurances
{n}
{n,}
{n,m}
[]
"""



import re

st = "boat"

res = re.search(r'b(ai|oa)t', st)

print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched my regex
else:
    print("Match not found....")
