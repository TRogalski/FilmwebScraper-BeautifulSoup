import os

class FileUtils():

    archive_dir = "../../archive"
    
    def __init__(self, date):
        self.date = date        
    
    
    def create_archive_dir(self):  
        if not os.path.exists(self.archive_dir):
            os.mkdir(self.archive_dir)
            print("Archive directory created.")
        else:
            print("Archive directory exists.")
    
    
    def create_subdir(self):
        if not os.path.exists(self.archive_dir + "/" + self.date):
            os.mkdir(self.archive_dir + "/" + self.date)
            print("Archive subdirectory for %s created." % self.date)
            
            
    def save_raw(self, page, soup):
        with open(self.archive_dir+"/"+self.date+"/"+'page %d.txt' % page, 'w') as file:
            file.write(str(soup))
    
    def clear_day_log(self):
        open(self.archive_dir + "/log/" + self.date + ".txt", 'w').close()
            
    def day_log(self, page, response_status):
        self.create_log_dir()
        with open(self.archive_dir + "/log/" + self.date + ".txt", 'a') as file:
            file.writelines("%d, %d\n" % (page, response_status))
    
    
    def create_log_dir(self):
        if not os.path.exists(self.archive_dir + "/log"):
            os.mkdir(self.archive_dir + "/log")
            print("Log folder created.")
