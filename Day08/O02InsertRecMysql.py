
import  pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port = 3306, database="playerdb")

cursor = conn.cursor()

FL = open("query.txt", "r")

for query in FL.readlines():
    print(query)
    cursor.execute(query)

FL.close()
conn.commit()
conn.close()