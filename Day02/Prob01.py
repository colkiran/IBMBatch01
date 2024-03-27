
st = """123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/mypics.gif
HTTP/1.0" 200 6248 "http://www.abcxyz.com/asctortf/" "Mozilla/4.05
(Macintosh; I; PPC)"
"""

print(f"st :{st}")

ip = st.split()
print(f"ip :{ip}")
print("-" * 60)

ip = st.split()[0]
print(f"ip :{ip}")

date = st.split()[3]
date = date.lstrip("[")
date = date.split(":")[0]
print(f"date :{date}")
print("-" * 60)

pics = st.split()[6]
pics = pics.split("/")[2]
print(f"pics :{pics}")
print("-" * 60)

url = st.split()[10]
print(f"url :{url}")
