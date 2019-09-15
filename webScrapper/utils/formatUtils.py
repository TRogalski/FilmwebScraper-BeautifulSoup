class FormatUtils():

    def to_float(rating):
        if rating is not None:
            return float(rating.get_text().replace(",", "."))
        else:
            return "N/A"
        
    def to_int(rate_count):
        if rate_count is not None:
            return int(rate_count.get_text().replace(" ", ""))
        else:
            return "N/A"
