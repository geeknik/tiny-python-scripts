
import os
import json
import datetime

def analyze_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    log_data = []
    for log in logs:
        log_json = json.loads(log)
        log_data.append(log_json)

    return log_data

def filter_logs(log_data, start_date, end_date):
    filtered_logs = []
    for log in log_data:
        log_date = datetime.datetime.strptime(log['timestamp'], '%Y-%m-%d %H:%M:%S')
        if start_date <= log_date <= end_date:
            filtered_logs.append(log)

    return filtered_logs

def main():
    log_file = 'logs.json'
    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2022, 12, 31)

    log_data = analyze_logs(log_file)
    filtered_logs = filter_logs(log_data, start_date, end_date)

    for log in filtered_logs:
        print(log)

if __name__ == "__main__":
    main()
