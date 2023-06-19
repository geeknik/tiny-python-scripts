
import re
import requests

def is_sql_injection(payload):
    # SQL Injection patterns
    patterns = [
        r"(\b(AND|OR)\b\s+\w+\s*=\s*\w+\s*\b(AND|OR)\b|\b(AND|OR)\b\s+\w+\s*=\s*\w+\s*\b(AND|OR)\b)",
        r"(\b(AND|OR)\b\s+\w+\s*=\s*\w+\s*\b(AND|OR)\b|\b(AND|OR)\b\s+\w+\s*=\s*\w+\s*\b(AND|OR)\b)",
        r"(SELECT\s+[\w\*\)\(\,\s]+\s+FROM\s+\w+)",
        r"(INSERT\s+INTO\s+\w+\s+VALUES\s+\(\s*[\w\'\,\)]+)",
        r"(UPDATE\s+\w+\s+SET\s+\w+\s*=\s*\w+)",
        r"(DELETE\s+FROM\s+\w+)"
    ]

    for pattern in patterns:
        if re.search(pattern, payload, re.I):
            return True

    return False

def main():
    url = input("Enter URL to test for SQL Injection: ")
    payload = input("Enter the payload: ")

    if is_sql_injection(payload):
        print("Possible SQL Injection detected!")
    else:
        print("No SQL Injection detected.")

if __name__ == "__main__":
    main()
