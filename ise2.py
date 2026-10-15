"""
n= int(input("enter no of students:"))
marks=[]
for i in range (n):
    marks.append(int(input("enter marks:")))


maximum=max(marks)
minimum=min(marks)

average=sum(marks)/n
count =0

for mark in marks:
    if mark>average:
        count +=1


print("maximmum:",maximum)
print("minimum:",minimum)
print("avg",average)
print("students above avg:",count)

"""
        
import numpy as np


marks = np.array([
    [[70, 80, 90],
     
     [60, 75, 85]],

    [[80, 90, 85],
     
     [70, 80, 90]],

    [[60, 70, 80],
     
     [75, 85, 95]]
])

print("Marks:")

print(marks)

print("Subject-wise average:")

print(np.mean(marks, axis=(0, 1)))  
