import csv
import json
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['UST']
with open('attendance.csv', 'r') as f:
    reader = csv.DictReader(f)
    attendance_data = [row for row in reader]
attendance_collection = db['DEPARTMENTS']
attendance_collection.insert_many(attendance_data)

with open('employee_attendance.json', 'r') as f:
    attendance_data1 = json.load(f)
attendance_collection.insert_many(attendance_data1)
for record in attendance_collection.find():
    print(record)

