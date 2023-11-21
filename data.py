import os
from xata.client import XataClient
 
client = XataClient(api_key=os.getenv("XATA_API_KEY"), db_url="https://Andrielle-Hillis-s-workspace-ksvpaa.us-east-1.xata.sh/db/students")

def main():
    students = get_students()
    print(students)

def get_students():
    data = client.data().query("students", {
        "columns": [
            "id",
            "first_name",
            "last_name",
            "grade_level"
        ]
    })
    return data['records']


if __name__ == "__main__":
    main()