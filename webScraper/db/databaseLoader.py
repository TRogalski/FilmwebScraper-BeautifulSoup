import pymysql
import csv
import datetime

class DatabaseLoader():
    
    def __init__(self, host, user, port, passwd, db):
            self.host = host
            self.user = user
            self.port = port
            self.passwd = passwd
            self.db = db


    def load_day_into_db(self, archive_path, day):
        
        day_csv_path = archive_path + day + ".csv"
        db_conn = self.get_connection()
        cur = db_conn.cursor()
        
        self.create_db_if_not_exists(cur)
        
        try:
            cur.execute("USE filmweb")
            self.create_serials_table(cur)
            self.clear_previous_load_for_date(day, cur)
            with open(day_csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter = ',')
                next(reader, None)  # skip the headers
                for row in reader:
                    row_cleaned = list(map(self.replace_na_with_none, row))
                    print(row_cleaned)
                    query = "INSERT INTO serials(scrap_date, title, rating, rate_count, year) VALUES(STR_TO_DATE(%s, %s), %s, %s, %s, %s)"
                    cur.execute(query, (day, "%d-%m-%Y", row_cleaned[0], row_cleaned[1], row_cleaned[2], row_cleaned[3]))
                cur.connection.commit()
        finally:
            db_conn.close()
            cur.close()
    
    def clear_previous_load_for_date(self, date, db_cursor):
        db_cursor.execute("DELETE FROM serials WHERE scrap_date = STR_TO_DATE(%s, %s)", (date, '%d-%m-%Y'))
        db_cursor.connection.commit()
        print("Old data removed.")
    
    
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
                                                                scrap_date VARCHAR(10),
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
db.load_day_into_db("../../../archive/csv/", "26-10-2019")

    
    
    
