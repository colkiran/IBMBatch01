

import pymysql
from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb", port=3306)

cursor =conn.cursor()

query = "delete from player where plyid = 'PL021'"

cursor.execute(query)

conn.commit()
conn.close()
