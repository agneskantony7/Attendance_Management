import pandas as pd
import random
import datetime
import csv
import json



employee_data = {
    1001: 'John Smith',
    1002: 'Jane Doe',
    1003: 'Bob Johnson',
    1004: 'Sarah Lee',
    1005: 'Tom Williams'
}
employee_ids = [1001, 1002, 1003, 1004, 1005]


start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)
attendance_data = pd.DataFrame(columns=['company_id','employee_id','employee_name', 'in_time', 'out_time'])
for employee_id in employee_ids:
    for single_date in pd.date_range(start_date, end_date):
        in_time = datetime.datetime.combine(single_date, datetime.time(random.randint(8, 9), random.randint(0, 59)))
        out_time = datetime.datetime.combine(single_date, datetime.time(random.randint(17, 18), random.randint(0, 59)))
        temp_df = pd.DataFrame({'company_id': [1],'employee_id': [employee_id],'employee_name': [employee_data[employee_id]], 'in_time': [in_time], 'out_time': [out_time]})
        attendance_data = pd.concat([attendance_data, temp_df], ignore_index=True)


attendance_data.to_csv('employee_attendance.csv', index=False)
attendance_data = "employee_attendance.csv"
with open(attendance_data, "r", newline="") as f:
    reader = csv.reader(f)
  #  for row in reader:
   #     print(row)
with open('employee_attendance.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]
with open('attendance_data.json', 'w') as file:
    json.dump(rows, file)


import pandas as pd
import random
import datetime
import csv
import json

public_holidays = [
    datetime.date(2022, 1, 26),  # Republic Day
    datetime.date(2022, 3, 11),  # Mahashivratri
    datetime.date(2022, 3, 29),  # Holi
    datetime.date(2022, 4, 15),  # Good Friday
    datetime.date(2022, 5, 3),   # Buddha Purnima
    datetime.date(2022, 8, 15),  # Independence Day
    datetime.date(2022, 10, 2),  # Gandhi Jayanti
    datetime.date(2022, 10, 15), # Dussehra
    datetime.date(2022, 11, 4),  # Diwali
    datetime.date(2022, 12, 25), # Christmas Day
]

attendance_data = pd.read_csv('employee_attendance.csv')

attendance_data['in_time'] = pd.to_datetime(attendance_data['in_time'])
attendance_data['out_time'] = pd.to_datetime(attendance_data['out_time'])

attendance_data = attendance_data[~(attendance_data['in_time'].dt.weekday.isin([5, 6]) | attendance_data['in_time'].dt.date.isin(public_holidays))]

attendance_data.to_csv('filtered_employee_attendance.csv', index=False)

with open('filtered_employee_attendance.csv', 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]
    for row in rows:
         print(row)

with open('filtered_attendance_data.json', 'w') as file:
    json.dump(rows, file)



