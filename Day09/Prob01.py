"""
ln= "LCNO-KAR-05-2005-2315"

LCNO - constant

KAR - KAR, KER, TND, APN, TEL, MAH

05 - 01 - 73    - RTO office number (no 00)

2005 - year     -   2000+

2315 - 0001 to 9999 (no 0000)
"""

import re

ln = "LCNO-MAH-73-2018-0001"

res = re.search(r'LCNO-(KAR|TND|APN|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', ln)

if res:
    print("Match found.......")
    print(res.group(0))
else:
    print("Match not found.....")





