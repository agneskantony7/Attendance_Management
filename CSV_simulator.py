import csv
import random
from datetime import datetime, timedelta
def generate_attendance_data(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)

    employees = ["Alice", "Bob", "Charlie", "David", "Eve", "Amy", "Jane", "Andria"]
    employee_id = ["E012", "E013", "E014", "E015", "E016","E017","E018","E019"]
    data = [["Employee", "Employee_id", "Date", "In Time", "Out Time"]]

    for date in dates:
        for employee in employees:
            for id in employee_id:
                attendance = random.choice(["Present", "Absent"])
                if attendance == "Present":
                    # generate random in-time between 8:00 AM and 10:00 AM
                    in_time = date.replace(hour=random.randint(8, 10), minute=random.randint(0, 59))
                    # generate random out-time between 4:00 PM and 6:00 PM
                    out_time = date.replace(hour=random.randint(16, 18), minute=random.randint(0, 59))

                    row = [employee, id, date.strftime("%Y-%m-%d"), in_time.strftime("%H:%M:%S"),
                           out_time.strftime("%H:%M:%S")]
                else:
                    row = [employee, id, date.strftime("%Y-%m-%d"), "", ""]
                data.append(row)

    return data
def save_attendance_data(data, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 31)
data = generate_attendance_data(start_date, end_date)
filename = "attendance.csv"
save_attendance_data(data, filename)
with open(filename, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)