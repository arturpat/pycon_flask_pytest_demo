import requests


class AccuweatherProxy:
    def __init__(self, apikey: str):
        self.apikey = apikey

    def find_city_key(self, city_name: str) -> str:
        url = "http://dataservice.accuweather.com/locations/v1/cities/search"
        params = {"apikey": self.apikey,
                  "query": city_name}  # something's wrong here
        response = requests.request("POST", url, params=params)
        return response.text

    # iter 1: put breakpoint and see how the response looks like
    def get_forecast_for_city_by_key(self, key: str) -> str:
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{key}"
        params = {"apikey": self.apikey}
        response = requests.request("GET", url, params=params)
        # what a great place to put a breakpoint at
        return f"test forcast for city key {key}"
