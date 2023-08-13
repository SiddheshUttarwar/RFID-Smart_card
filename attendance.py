from datetime import datetime,timedelta
import time

def get_attendance():
    students = []
    start = datetime.now()
    end = start +timedelta(minutes=1)
    while datetime.now()<end:
        b = input()
        if b not in students:
            students.append(b)
        time.sleep(1)
    #ser.close()
    return students
