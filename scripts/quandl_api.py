import quandl
from pprint import pprint

API_KEY = "XL_c6FZRjuz6WYRTJB_a"

def get_quandl_code(area_category, area_code, indicator_code):
    return f"ZILLOW/{area_category}{area_code}_{indicator_code}"



# set api key

zip_code = "78739"
area_category = "Z"
area_code = zip_code
indicator_code = "ZHVIAH"

quandl.ApiConfig.api_key = API_KEY
quandl_code = get_quandl_code(area_category, area_code, indicator_code)

data = quandl.get(quandl_code, start_date="1800-01-01", end_date="2018-04-30")
pprint(data)
