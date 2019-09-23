import pymysql

db_conn = pymysql.connect(
    host = "localhost",
    user = "root",
    port = 3306,
    passwd = "root",
    db = 'mysql'
)

cur = db_conn.cursor()
cur.execute("USE fw_scraping")
cur.execute("SELECT * FROM new")
print(cur.fetchone())
cur.close()
db_conn.close()

