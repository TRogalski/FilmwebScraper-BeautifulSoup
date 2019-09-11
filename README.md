# FilmwebSrapper
web scrapping project in Python

Web scrapper takes data from top series url:
https://www.filmweb.pl/serials/search?orderBy=popularity&descending=true&page=%1

Saves 'raw' page code to the archive for the given day and creates a list of maps:
['title': "", 'rating': 0.0, 'rating_count': 0]

TODO
-There should be a log of success/fail fetches depending on the html response code,
-More detailed data,
-MySQL database for cleaned up data,
-Code refactor & packaging
