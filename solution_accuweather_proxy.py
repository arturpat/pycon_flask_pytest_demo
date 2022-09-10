import requests


class AccuweatherProxy:
    def __init__(self, apikey: str):
        self.apikey = apikey

    # to be written live
    def __str__(self):
        return "I'll be displayed in the debugger variables window"

    def __repr__(self):
        return "I would be displayed in the debugger variables window it it wasn't for the guy above"
    ##############################

    # iter 1: "query" instead of "q" (should be "q")
    # def find_city_key(self, city_name: str) -> str:
    #     url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    #     params = {"apikey": "ADuP1UGtZCSRyLyM2lRcSTalxzBxbaqD",
    #               "query": city_name}
    #     response = requests.request("POST", url, params=params)
    #     return response.text

    # iter 2: response.json() and finding in structure
    # in variables view - can't see response.json() -> add to watches
    # response.json()[0]['Key']
    # def find_city_key(self, city_name: str) -> str:
    #     url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    #     params = {"apikey": "ADuP1UGtZCSRyLyM2lRcSTalxzBxbaqD",
    #               "q": city_name}
    #     response = requests.request("POST", url, params=params)
    #     return response.text

    def find_city_key(self, city_name: str) -> str:
        url = "http://dataservice.accuweather.com/locations/v1/cities/search"
        params = {"apikey": self.apikey,
                  "q": city_name}
        response = requests.request("POST", url, params=params)
        # great time to use watches
        return response.json()[0]['Key']

    # iter 1: put breakpoint and see how the response looks like
    # def get_forecast_for_city_by_key(self, key: str) -> str:
    #     return f"test forcast for city key {key}"

    def get_forecast_for_city_by_key(self, key: str) -> str:
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{key}"
        params = {"apikey": self.apikey}
        response = requests.request("GET", url, params=params)
        return response.json()["Headline"]["Text"] + f"\nMore info at {response.json()['Headline']['Link']}"
