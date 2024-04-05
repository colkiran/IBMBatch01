
import pymysql
from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb", port=3306)

cursor =conn.cursor()

query = "update player set achievement = '7 ballandors, World Cup Winner' where plyid = 'PL003'"

cursor.execute(query)

conn.commit()

conn.close()
