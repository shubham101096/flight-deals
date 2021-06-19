from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
user_data = data_manager.get_users()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight and flight.price < destination["lowestPrice"]:
        message = f"Subject: Low price alert! \n\nOnly £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        if flight.max_stopover > 0:
            message += f"\nFlight has {flight.max_stopover} stop over, via {flight.via_city}."

        notification_manager.send_sms(
            message=message
        )

        link = f"\nhttps://www.google.co.uk/flights?hl=en#flt=" \
               f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*" \
               f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        for id in user_data:
            notification_manager.send_email(id, message+link)



