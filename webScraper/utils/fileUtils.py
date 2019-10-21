import os
import csv
import datetime

class FileUtils():

    def __init__(self, date = datetime.datetime.today().strftime("%d-%m-%Y"), archive_dir = "../../archive"):
        self.archive_dir = archive_dir
        self.date = date        


    def create_archive_dir(self):  
        if not os.path.exists(self.archive_dir):
            os.mkdir(self.archive_dir)
            print("Archive directory created.")
        else:
            print("Archive directory exists.")


    def create_raw_subdir(self):
        if not os.path.exists(self.archive_dir + "/" + self.date):
            os.mkdir(self.archive_dir + "/" + self.date)
            print("Archive subdirectory for %s created." % self.date)
    
    
    def save_raw(self, page, soup):
        with open(self.archive_dir + "/" + self.date + "/" + 'page %d.txt' % page, 'w') as file:
            file.write(str(soup))


    def save_csv(self, serials):
        csv_file = open(self.archive_dir + "/csv/" + self.date + ".csv", 'wt')
        try:
            writer = csv.writer(csv_file)
            writer.writerow(('title', 'rating', 'rate_count', 'year'))
            for serial in serials:
                writer.writerow((serial['title'], serial['rating'], serial['rate_count'], serial['year']))
        finally:
            csv_file.close()
    
    
    def create_csv_subdir(self):
        if not os.path.exists(self.archive_dir + "/csv"):
            os.mkdir(self.archive_dir + "/csv")
            print("csv folder created.")


    def clear_day_log(self):
        self.create_log_subdir()
        open(self.archive_dir + "/log/" + self.date + ".txt", 'w').close()
    

    def day_log(self, page, response_status):
        self.create_log_subdir()
        with open(self.archive_dir + "/log/" + self.date + ".txt", 'a') as file:
            file.writelines("%d, %d\n" % (page, response_status))


    def create_log_subdir(self):
        if not os.path.exists(self.archive_dir + "/log"):
            os.mkdir(self.archive_dir + "/log")
            print("Log folder created.")
