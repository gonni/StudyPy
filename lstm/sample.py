import pymysql

conn, cur = None, None
row = ""

conn = pymysql.connect(host='x86d', user='root', password='root', db='users', charset='utf8mb4')
cur = conn.cursor()
cur.execute("SELECT * FROM user_table")

while(True):
    row = cur.fetchone()
    if row==None:
        break
    print('-->' + row[0])

conn.close()

print("DB Connection completed ..")