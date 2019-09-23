class FormatUtils():

    def to_float(rating):
        if rating is not None:
            try:
                return float(rating.get_text().replace(",", "."))
            except ValueError:
                return "error"
        else:
            return "N/A"


    def to_int(rate_count):
        if rate_count is not None:
            try:
                return int(rate_count.get_text().replace(" ", ""))
            except ValueError:
                return "error"
        else:
            return "N/A"
