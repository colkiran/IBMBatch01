
import pymysql
from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb", port=3306)

cursor =conn.cursor()

query = "select * from player"

cursor.execute(query)

prtTbl = from_db_cursor(cursor)
prtTbl.align['plyname'] = "l"
prtTbl.align['sport'] = "r"


print(prtTbl)

conn.close()
