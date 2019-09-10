import requests
import os
from bs4 import BeautifulSoup


def formatRating(rating):
    if rating is not None:
        return float(rating.get_text().replace(",", "."))
    else:
        return "N/A"
        
def formatRateCount(rate_count):
    if rate_count is not None:
        return int(rate_count.get_text().replace(" ", ""))
    else:
        return "N/A"

movies = []

for page_index in range(1, 21):
    
    response = requests.get("https://www.filmweb.pl/serials/search?orderBy=popularity&descending=true&page=%d" % page_index)
    
    print("Get page = %d, response status = %s" % (page_index, response.status_code))
    
    html_soup = BeautifulSoup(response.content, 'html.parser')
    series_divs = html_soup.find_all(class_="hits__item")

    for section in series_divs:
        details_map = {}
        details_map['title'] = section.find(class_ = "filmPreview__title").get_text()
        details_map['rating'] = formatRating(section.find(class_ = "rateBox__rate"))
        details_map['rate_count'] = formatRateCount(section.find(class_ = "rateBox__votes--count"))
        details_map['year'] = section.find(class_ = "filmPreview__year").get_text()
        movies.append(details_map)


for item in movies:
    print("Movie: %s (%s),  Rating: %r" % (item.get('title'), item.get('year'), item.get('rating')))





