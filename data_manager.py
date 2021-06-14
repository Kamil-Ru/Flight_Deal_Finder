from password import *
import requests

class DataManager:
    def __init__(self):
        self.url_sheety = URL_SHEETY
        self.headersAuth = {
        'Authorization': f'Bearer {BEARER_AUTHENTICATION}'
    }

    def get(self):
        response = requests.get(url=self.url_sheety, headers=self.headersAuth)
        return response.json()

    def put(self, id, city_iata):
        self.url_sheety = URL_SHEETY + f"/{str(id)}"
        self.body = {
            "price": {
                "iataCode": city_iata,
            }}
        response = requests.put(url=self.url_sheety, json=self.body, headers=self.headersAuth)
        return print(response.text)