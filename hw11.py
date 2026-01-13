
import json
from datetime import datetime
from tracker import get_record

records = [
    get_record("Paris", "15-05-2023", "Amazing food and culture"),
    get_record("Rome", "20-08-2024", "Historic and beautiful"),
    get_record("Tokyo", "10-12-2024", "Technology meets tradition")
]

for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON Output:")
print(json_data)

parsed_records = json.loads(json_data)

print("\nParsed Records:")
for record in parsed_records:
    print(f"{record['city']} | {record['date']} | {record['comment']}")
