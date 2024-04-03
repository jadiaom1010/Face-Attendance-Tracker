import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred ,
{
    'databaseURL' : "https://faceattendancerealtime-8c84f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "41":
        {
            "name": "Om ",
            "Branch": "IT",
            "starting_year": 2021,
            "total_attendance": 7,
            "Grade": "A",
            "year": 3,
            "last_attendance_time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        },

    "63":
        {
            "name": "Harsh ",
            "Branch": "IT",
            "starting_year": 2021,
            "total_attendance": 10,
            "Grade": "B",
            "year": 3,
            "last_attendance_time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        },
    "16":
        {
            "name": "Sheen ",
            "Branch": "IT",
            "starting_year": 2021,
            "total_attendance": 1,
            "Grade": "C",
            "year": 3,
            "last_attendance_time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        },
    "15":
        {
            "name": "Sairaj ",
            "Branch": "IT",
            "starting_year": 2021,
            "total_attendance": 5,
            "Grade": "D",
            "year": 3,
            "last_attendance_time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }

}

for key, value in data.items():
    ref.child(key).set(value)