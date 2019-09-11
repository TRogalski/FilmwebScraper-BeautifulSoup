import requests
import os
import datetime
from fileUtils import FileUtils
from formatUtils import FormatUtils
from bs4 import BeautifulSoup

class WebScrapper():
    
    serials = []
    page_url_template = "https://www.filmweb.pl/serials/search?orderBy=popularity&descending=true&page=%d" 
    
    def __init__(self):
        self.fileUtils = FileUtils(datetime.datetime.today().strftime("%d-%m-%Y")) 
        
    def scrapp_serials(self):  
        self.fileUtils.create_archive_dir()
        
        for page_index in range(1, 21):
            
            response = requests.get(self.page_url_template % page_index)
            self.notify(page_index, response.status_code)

            html_soup = BeautifulSoup(response.content, 'html.parser')
            self.put_in_archive(page_index, html_soup)
            
            hits = html_soup.find_all(class_="hits__item")

            for hit in hits:
                self.serials.append(self.get_formatted_data(hit))
                
    
    
    def get_formatted_data(self, serial_section):
        serial = {}
        serial['title'] = serial_section.find(class_ = "filmPreview__title").get_text()
        serial['rating'] = FormatUtils.to_float(serial_section.find(class_ = "rateBox__rate"))
        serial['rate_count'] = FormatUtils.to_int(serial_section.find(class_ = "rateBox__votes--count"))
        serial['year'] = serial_section.find(class_ = "filmPreview__year").get_text()
        return serial
    
    
    def notify(self, page, status):
        print("Get page = %d, response status = %s" % (page, status))
    
    
    def put_in_archive(self, page, soup):      
        self.fileUtils.create_subdir()
        self.fileUtils.save_raw(page, soup)
    
    
    def display_serials(self):
        for serial in self.serials:
            print("Movie: %s (%s),  Rating: %r" % (serial.get('title'), serial.get('year'), serial.get('rating')))



