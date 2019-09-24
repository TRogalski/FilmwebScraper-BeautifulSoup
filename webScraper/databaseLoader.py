import pymysql
import csv

def create_db_if_not_exists(db_cursor):
    db_cursor.execute("""CREATE DATABASE IF NOT EXISTS filmweb 
                         CHARACTER SET = utf8mb4 
                         COLLATE  = utf8mb4_unicode_ci""")


def create_serials_table(db_cursor):
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS serials(id BIGINT(7) NOT NULL AUTO_INCREMENT,
                                                            title VARCHAR(200),
                                                            rating FLOAT,
                                                            rate_count INT,
                                                            year INT,
                                                            PRIMARY KEY (id))""")


def replace_na_with_none(item):
    # Missing values replaced with -1
    if item == "N/A":
        return -1
    else:
        return item


db_conn = pymysql.connect(
    host = "localhost",
    user = "root",
    port = 3306,
    passwd = "root",
    db = 'mysql'
)

cur = db_conn.cursor()

create_db_if_not_exists(cur)

try:
    cur.execute("USE filmweb")
    create_serials_table(cur)
    with open('../../archive/csv/24-09-2019.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        next(reader, None)  # skip the headers
        for row in reader:
            row_cleaned = list(map(replace_na_with_none, row))
            print(row_cleaned)
            cur.execute("""INSERT INTO serials(title, rating, rate_count, year)
                                        VALUES(%r, %r, %r, %r)""", (row_cleaned[0], float(row_cleaned[1]), int(row_cleaned[2]), int(row_cleaned[3])))
        cur.connection.commit()
finally:
    db_conn.close()
    cur.close()
    
    

