import requests
from password import *
from datetime import date
import dateutil.relativedelta

def today():
    today_day = date.today()
    data_now = today_day.strftime("%d/%m/%Y")
    return data_now

def six_months_later():
    today_day = date.today()
    delta = dateutil.relativedelta.relativedelta(months=6)
    six_months_later = today_day + delta
    six_months_later = six_months_later.strftime("%d/%m/%Y")

    return six_months_later
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.apikey = API_key
        self.url = URL_TEQUILA
        self.headers = {
        "accept": "application / json",
        "apikey": self.apikey
    }

    def search_city_iata(self, city):
        self.url = URL_TEQUILA + "locations/query"
        body = {
        "term": city,
        "location_types": "airport",
        "limit" : "1"
        }

        response = requests.get(url=self.url, params=body, headers=self.headers)
        data = response.json()
        iata = data["locations"][0]["city"]["code"]
        return iata

    def search_connection(self, code_IATA_destination_city, price_to):
        url = URL_TEQUILA + "v2/search"
        body = {
        "fly_from": "KRK",
        "fly_to": code_IATA_destination_city,
        "date_from" : today(),
        "date_to" : six_months_later(),
        "nights_in_dst_from": "7",
        "nights_in_dst_to" : "28",
        "flight_type" : "round",
        "curr" : "GBP",
        "price_to" : price_to,
        "limit" : "1"
        }

        response = requests.get(url=url, headers=self.headers, params=body)

        response.raise_for_status()
        data_json = response.json()
        return data_json
