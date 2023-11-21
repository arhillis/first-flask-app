import os
from xata.client import XataClient
 
client = XataClient(api_key=os.environ["XATA_API_KEY"], db_url="https://Andrielle-Hillis-s-workspace-ksvpaa.us-east-1.xata.sh/db/students")

data = client.data().query("students", {
    "columns": [
        "id",
        "first_name",
        "last_name",
        "grade_level"
    ]
})
print(data)