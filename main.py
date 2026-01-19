import json
from datetime import datetime
from tripdata import get_trip

trips = []

trips.append(get_trip("Paris", "15-05-2023", "Beautiful architecture"))
trips.append(get_trip("Rome", "02-08-2022", "Amazing food"))
trips.append(get_trip("Tokyo", "21-12-2024", "Great culture"))

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)
print(json_data)
