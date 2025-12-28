import numpy as np
import pandas as pd
students = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun",
    "Sai", "Krishna", "Ishaan", "Rohan", "Ananya"
]

Total_days = 26

Present_days = np.array([22, 25, 20, 24, 18, 23, 21, 26, 19, 24])

Absent_days = Total_days - Present_days

attendance_df = pd.DataFrame({
    "Student Name": students,
    "Days Present": Present_days,
    "Days Absent": Absent_days})

# Calculate attendance percentage
attendance_df["Attendance %"] = (attendance_df["Days Present"] / Total_days) * 100

print("ATTENDANCE MANAGEMENT SYSTEM\n - mrinal.py:22")
print(attendance_df)

low_attendance = attendance_df[attendance_df["Attendance %"] < 75]

print("\nStudents with Attendance Below 75%:\n - mrinal.py:27")
print(low_attendance)