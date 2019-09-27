import pymysql
import csv

class DatabaseLoader():
    
    def __init__(self, host, user, port, passwd, db):
            self.host = host
            self.user = user
            self.port = port
            self.passwd = passwd
            self.db = db


    def load_day_into_db(self, day_csv_path):
        db_conn = self.get_connection()
        cur = db_conn.cursor()
        
        self.create_db_if_not_exists(cur)
        
        try:
            cur.execute("USE filmweb")
            self.create_serials_table(cur)
            with open(day_csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter = ',')
                next(reader, None)  # skip the headers
                for row in reader:
                    row_cleaned = list(map(self.replace_na_with_none, row))
                    print(row_cleaned)
                    cur.execute("""INSERT INTO serials(title, rating, rate_count, year)
                                                VALUES(%s, %s, %s, %s)""", (row_cleaned[0], row_cleaned[1], row_cleaned[2], row_cleaned[3]))
                cur.connection.commit()
        finally:
            db_conn.close()
            cur.close()
    
    
    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            port = self.port,
            passwd = self.passwd,
            db = self.db)
    
    
    def create_db_if_not_exists(self, db_cursor):
        db_cursor.execute("""CREATE DATABASE IF NOT EXISTS filmweb 
                             CHARACTER SET = utf8mb4 
                             COLLATE  = utf8mb4_unicode_ci""")


    def create_serials_table(self, db_cursor):
        db_cursor.execute("""CREATE TABLE IF NOT EXISTS serials(id BIGINT(7) NOT NULL AUTO_INCREMENT,
                                                                title VARCHAR(200),
                                                                rating FLOAT,
                                                                rate_count INT,
                                                                year INT,
                                                                PRIMARY KEY (id))""")


    def replace_na_with_none(self, item):
        # Missing values replaced with -1
        if item == "N/A":
            return -1
        else:
            return item

db = DatabaseLoader("localhost", "root", 3306, "root", "mysql")
db.load_day_into_db("../../../archive/csv/24-09-2019.csv")

    
    
    
