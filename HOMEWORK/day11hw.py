import json
from datetime import datetime
from tracker import create_trip
trips=[
      create_trip("Kochi","Business trip","2023-05-10"),
        create_trip("Trivandrum","Vacation","2022-11-15"),
        create_trip("Calicut","Good food","2024-03-20")
        ]   
for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%Y-%m-%d")
    trip["date"] = date_obj.strftime("%M %d, %Y")

trips=json.dumps(trips,indent=4)
print(trips)

tripobj=json.loads(trips)
for trip in tripobj:
    print(f"City: {trip['city']}, Date: {trip['date']}, Comment: {trip['comment']}")