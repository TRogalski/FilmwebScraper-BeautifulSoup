# FilmwebSrapper
Web scrapping project in Python

Web scrapper takes data from top TV series, url:

https://www.filmweb.pl/serials/search?orderBy=popularity&descending=true&page=%1

Saves 'raw' page code to the archive for the given day and creates a list of maps:

['title': "", 'rating': 0.0, 'rating_count': 0]

There is also a success log for each page scrapp attempt.

TODO:
- More detailed data.
- There should be option to rerun of the failed fetches (if they appear in the log).
- Add more descriptive error handling.
