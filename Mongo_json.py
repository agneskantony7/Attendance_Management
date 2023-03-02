import json
from pymongo import MongoClient
client = MongoClient()
db = client.UST
attendance_collection = db.JSON_FILE
with open('employee_attendance.json', 'r') as f:
    attendance_data1 = json.load(f)
attendance_collection.insert_many(attendance_data1)
for record in attendance_collection.find():
    print(record)
