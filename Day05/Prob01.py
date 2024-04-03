st = """
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/mypics.gif
HTTP/1.0" 200 6248 "http://www.abcxyz.com/asctortf/" "Mozilla/4.05
(Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/mypics.gif
HTTP/1.0" 200 6248 "http://www.abcxyz.com/asctortf/" "Mozilla/4.05
(Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/mypics.gif
HTTP/1.0" 200 6248 "http://www.abcxyz.com/asctortf/" "Mozilla/4.05
(Macintosh; I; PPC)"
"""

# Split string with space
listString = st.split(' ')
print(listString)
print("-" * 60)

# Print IP address
ip = st.split()[0]
print(f"IP : {ip}")
print("-" * 60)

# Print Date
date = st.split()[3]
date = date.strip("[")
date = date.split(" :")[0]
print(f"Date : {date}")
print("-" * 60)

# Print Pic
pic = st. split()[6]
print(f"PIC : {pic}")
print("-" * 60)

# Print URL
url = st. split()[10]
print(f"URL : {url}")
print("=" * 60)

# Creation of list
updatedList = []
updatedList.append(ip)
updatedList.append(date)
updatedList.append(pic)
updatedList.append(url)
print(f"Updated List : {updatedList}")
print("=" * 60)

# The Lists of list
listsOfList = []
for i in range(0, 3, 1):
    listsOfList.append(updatedList)
print(f"The List of lists : {listsOfList}")
print("=" * 60)

# The Lists of Tuple
listsOfTuple = []
for i in range(0, 3, 1) :
    listsOfTuple. append (tuple(updatedList))
print(f"The List of Tuples : {listsOfTuple}")
print("=" * 60)

# Dictionary
dict = { }
dict.setdefault('0', tuple(updatedList))
dict.setdefault('1', tuple(updatedList))
dict.setdefault('2', tuple(updatedList))

print(f"Dictionary : {dict}")
print("=" * 60)