import json
from datetime import datetime
from tripdata import create_trip
trips=[
      create_trip("Kochi", "2023-05-10", "Business trip"),
      create_trip("Trivandrum", "2022-11-15", "Vacation"),
      create_trip("Calicut", "2024-03-20", "Good food")
      ]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%Y-%m-%d")
    trip["date"] = date_obj.strftime("%B %d, %Y")

    
    
trips=json.dumps(trips,indent=4)

print(trips)
