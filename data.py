import os
from xata.client import XataClient
 
client = XataClient(api_key="xau_d8vjReqyvQgAh2JBThuyme6fbcjKV8IO5", db_url="https://Andrielle-Hillis-s-workspace-ksvpaa.us-east-1.xata.sh/db/students")

def main():
    students = get_students()
    for student in students:
        print(student)

def get_students():
    data = client.data().query("students", {
        "columns": [
            "id",
            "first_name",
            "last_name",
            "grade_level"
        ]
    })
    return [{'first_name': record['first_name'], 'last_name': record['last_name'], 'grade_level': record['grade_level']} for record in data['records']]


if __name__ == "__main__":
    main()