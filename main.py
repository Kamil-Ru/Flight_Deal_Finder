from pprint import pprint
from data_manager import *
# from data_import import data
from flight_search import *
from notification_manager import *

sheet_data_data = DataManager()
get_data = sheet_data_data.get()
data = get_data["prices"]
# pprint(get_data)

for row in data:
    # print(row["city"])
    new_search = FlightSearch()
    city_iata = new_search.search_city_iata(row["city"])
    print(city_iata)

    local_data = new_search.search_connection(city_iata, row["lowestPrice"])
    pprint(local_data)
    notification = NotificationManager(local_data)

    notification.send_message()
