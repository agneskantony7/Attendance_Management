import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

def calculate_working_days(employee_data):
    employee_id, data = employee_data
    attendance_data = pd.DataFrame(data, columns=['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time'])
    attendance_data['in_time'] = pd.to_datetime(attendance_data['in_time'])
    attendance_data['out_time'] = pd.to_datetime(attendance_data['out_time'])
    daily_working_hours = (attendance_data['out_time'] - attendance_data['in_time']).dt.total_seconds() / 3600
    attendance_data = attendance_data[daily_working_hours >= 8]
    #print(attendance_data)

    monthly_working_days = attendance_data.groupby([
        pd.Grouper(key='in_time', freq='M'),
        'company_id',
        'employee_id',
        'employee_name'
    ]).apply(lambda x: len(x))

    # Initialize a dictionary to store the working days for each employee and month
    results = {}

    for index, row in monthly_working_days.items():
        company_id, employee_id, employee_name = index[1], index[2], index[3]
        month = index[0].strftime('%B')
        year = index[0].year
        working_days = row

        # Add the working days to the results dictionary
        key = (company_id, employee_id, employee_name, year)
        if key not in results:
            results[key] = {'january': 0, 'february': 0, 'march': 0, 'april': 0, 'may': 0, 'june': 0, 'july': 0, 'august': 0, 'september': 0, 'october': 0, 'november': 0, 'december': 0}
        results[key][month.lower()] = working_days
    print(results)
    # Convert the results dictionary to a DataFrame and print it
    df = pd.DataFrame.from_dict(results, orient='index').reset_index()
    print(df)
    df = df.rename(columns={'index': 'company_id_employee_id_employee_name_year'})
    df[['company_id', 'employee_id', 'employee_name', 'year']] = df['company_id_employee_id_employee_name_year'].apply(pd.Series)
    df = df.drop('company_id_employee_id_employee_name_year', axis=1)
    print(df)
    print(df.to_string(index=False))
    print(df)
# Create a connection to the Postgres database
    conn = psycopg2.connect(
        host="localhost",
        database="*****",
        user="*****",
        password="******"
    )

    # Create a table in the database
    engine = create_engine('postgresql+psycopg2://postgres:******@localhost:5432/********')
    df.to_sql(name='working_days', con=engine, if_exists='replace', index=False)

    # Close the database connection
    conn.close()


if __name__ == '__main__':
    attendance_data = pd.read_csv('filtered_employee_attendance.csv')
    employee_attendance = attendance_data.groupby(['company_id', 'employee_id']).apply(
        lambda x: x[['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time']].values.tolist())
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(calculate_working_days, employee_attendance.items())
