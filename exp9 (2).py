
"""
pgm1
import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Python": [85, 72, 90, 65, 80],
    "DBMS": [78, 75, 88, 70, 82],
    "Mathematics": [90, 68, 85, 72, 79]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])
"""
"""
PGM 2

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [55000, 48000, 65000, 72000, 45000],
    "Experience": [3, 5, 7, 10, 2]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
"""

"""
pgm 3

import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 800, 1500, 12000, 9000],
    "Quantity": [5, 20, 15, 8, 6]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
"""
"""
pgm 4

import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Patient_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Fever", "Diabetes"],
    "Medical_Charges": [60000, 25000, 80000, 15000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
"""
"""
pgm 5

import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [60000, 25000, 15000, 12000, 18000],
    "Discount": [2000, 1000, 500, 500, 1000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())
"""
"""

pgm 6
import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE"],
    "Total_Classes": [100, 100, 90, 100, 80],
    "Classes_Attended": [90, 70, 80, 60, 75]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])
"""
"""


pgm 7

import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "TV", "Printer", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Price": [50000, 20000, 40000, 10000, 15000],
    "Quantity": [5, 10, 3, 8, 6]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())
"""
"""


pgm 8

import pandas as pd

marks = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 90,
    "Priya": 65,
    "Neha": 80
}

s = pd.Series(marks)

print("Series:")
print(s)

print("\nMarks of Amit:")
print(s["Amit"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAverage Marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])
"""
"""

pgm 9

import pandas as pd

salary = {
    "Amit": 55000,
    "Rahul": 48000,
    "Sneha": 65000,
    "Priya": 45000,
    "Neha": 72000
}

s = pd.Series(salary)

print("Series:")
print(s)

print("\nHighest Salary:")
print(s.max())

print("\nLowest Salary:")
print(s.min())

print("\nAverage Salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])
"""
"""

pgm 10

import pandas as pd

products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 9000
}

s = pd.Series(products)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost expensive product:")
print(s.idxmax(), s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])
"""
"""

pgm 11

import pandas as pd

patients = {
    "P101": 65,
    "P102": 45,
    "P103": 72,
    "P104": 30,
    "P105": 68
}

s = pd.Series(patients)

print("Patient Ages:")
print(s)

print("\nAverage Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), s.max())

print("\nYoungest Patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60:")
print(s[s > 60])
"""
"""
#pgm 12
import pandas as pd

attendance = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 95,
    "Priya": 68,
    "Neha": 91
}

s = pd.Series(attendance)

print("Attendance:")
print(s)

print("\nAverage Attendance:")
print(s.mean())

print("\nAttendance below 75:")
print(s[s < 75])

print("\nAttendance above 90:")
print(s[s > 90])

print("\nHighest Attendance:")
print(s.max())

"""
"""
#pgm 13

import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks of each subject:")
print("Python:", df["Python"].mean())
print("DBMS:", df["DBMS"].mean())
print("Maths:", df["Maths"].mean())
"""

"""
pgm14
import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
"""
"""
pgm 15
import pandas as pd

df = pd.read_csv("employees.csv")

print("CSE Employees:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
"""


