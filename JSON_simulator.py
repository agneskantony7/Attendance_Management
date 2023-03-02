from faker import Faker
import random
import datetime
import json
fake = Faker()
attendance_data = []
for i in range(10):
        employee_id = f'E{i + 1:04d}'
        name = fake.name()
        date = datetime.date(2023, 3, i+1)
        time_in = datetime.time(random.randint(8, 10), random.randint(0, 59))
        time_out = datetime.time(random.randint(17, 19), random.randint(0, 59))
        status = random.choice(['present', 'absent'])
        attendance_record = {'employee_id': employee_id, 'name': name, 'date': date.isoformat(), 'time_in': time_in.isoformat(), 'time_out': time_out.isoformat(), 'status': status}
        attendance_data.append(attendance_record)
for attendance_record in attendance_data:
    print(attendance_record)
with open('employee_attendance.json', 'w') as f:
    json.dump(attendance_data, f)

with open("employee_attendance.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)

