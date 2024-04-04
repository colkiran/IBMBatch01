
FL = open("data.txt", "r")

# st = FL.read()      # reads the entire contents of the file
#st = FL.read(500)     # reads depending on the number of bytes specified

#st = FL.readline()      # can read one line at a time
#st = FL.readline(450)     # can read the data depending on the no of bytes specified (bytes should be less than the size of the line)

# st = FL.readlines()          # will read all the lines and store it in the form of a list
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines(855)

print(st)

FL.close()