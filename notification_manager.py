# -*- encoding: utf-8 -*-

from twilio.rest import Client
from password import *
import smtplib

class NotificationManager:
    def __init__(self, data_json):

        self.data_json = data_json
        self.price = self.data_json['data'][0]['price']
        self.departure_airport_code = self.data_json['data'][0]['flyFrom']
        self.departure_city = self.data_json['data'][0]['cityFrom']
        self.departure_country = self.data_json['data'][0]['countryFrom']['name']
        departure_date = self.data_json['data'][0]['route'][0]['local_departure']
        self.departure_date = departure_date.split("T")[0]

        self.arrival_airport_code = self.data_json['data'][0]['flyTo']
        self.arrival_city = self.data_json['data'][0]['cityTo']
        self.arrival_country = self.data_json['data'][0]['countryTo']['name']
        back_date = self.data_json['data'][0]['route'][1]['local_arrival']
        self.back_date = back_date.split("T")[0]

        self.text = (f"Low price alert! Only £{self.price} to fly from "
        f"{self.departure_city}-{self.departure_airport_code} to "
        f"{self.arrival_city}-{self.arrival_airport_code}, from {self.departure_date} to "
        f"{self.back_date}").encode('utf-8')

    def send_message(self):

        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        from_phone = FROM_PHONE
        to_phone = TO_PHONE
        client = Client(account_sid, auth_token)

        client.messages.create(
            body=self.text,
            from_=from_phone,
            to=to_phone
        )

    def send_emails(self, to_email):

        my_email = MY_EMAIL
        password = PASSWORD

        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Fly Notification\n\n{self.text}"
            )
        pass
