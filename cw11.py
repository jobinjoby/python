import tripdata
from datetime import datetime
import json

trips = [
    tripdata.get_trip("Paris", "15-05-2023", "Amazing food and culture"),
    tripdata.get_trip("Rome", "20-08-2024", "Historic and beautiful"),
    tripdata.get_trip("Tokyo", "10-12-2024", "Technology meets tradition")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)
print(json_data)

