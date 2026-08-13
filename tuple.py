#program 1
'''
i=(1,25,54,78)
print(i)
'''
#program 2
'''
i=("kolhapur","Pune","Sangli","Mumbai")
print(i[0])
print(i[3])
print(i[2])
'''
#program 3
'''
i=(1,25,54,78)
print(len(i))
'''
#program 4
'''
t=("orange","red","White","pink")
ch =input("enter a color")

if ch in t:
    print("color found in tuple")
else:
    print("color not found")
'''
#program 5
'''
t=("mango","apple","banana","guava")
for i in t:
    print(i)
'''

#program 6
'''
i=(1,25,54,78,25)
print(i.count(25))
'''

#program 7
'''
e=(121,222,341,555)
n=int(input("enter id to find index:"))
print(e.index(n))
'''
#program 8
'''
t=("mango","apple","banana","guava")
i=(1,25,54,78,25)

print(t+i)
'''

#program 9
'''
i=(1,25,54,78,25)*3
print(i)
'''

#program 10
'''
t=(10,20,30,40,50,60,70,80,90,100)
print(t[0:6])
print(t[4:9])
print(t[3:7])
print(t[0:10:2])
print(t[::-1])
'''
#program 11
'''
t=(10,20,30,40,50,60,70,80,90,100)
l=list(t)
l.append(110)
t=tuple(l)
print(t)
'''
#program 12
'''
lst = []

for i in range(5):
    n = int(input("Enter number: "))
    lst.append(n)

t = tuple(lst)

print("List:", lst)
print("Tuple:", t)
'''
#program 13
'''
t=(10,20,30,40,50,60,70,80,90,100)
l=list(t)
t=tuple(l)
print(t)
'''

#program 14
'''
t=(10,20,30,40,50,60,70,80,90,100)
del t
'''
#program 15
'''
students=(
    (1,"paddy",130),
    (2,"game",127)
    )
for i in students:
    print("id",i[0])
    print('name:',i[1])
    print('roll:',i[2])
'''
#program 16
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

sum = 0

for n in t:
    sum = sum + n

print("Sum =", sum)
'''

#PROGRAM 17
'''
t = (25, 10, 45, 5, 30, 60)

largest = t[0]
smallest = t[0]

for n in t:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n


print("Largest =", largest)
print("Smallest =", smallest)
'''
#program 18
'''
t = (25, 10, 45, 5, 30, 60)
sum =0
for  i in t:
    sum= sum+i
    av=sum//len(t)
print(av)   
'''
#program 19
'''
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for n in t:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)
'''
#program 20
'''
t=(5,4,6,7,8)
n=int(input("enter a number:"))
if n in t:
    print("element exist in tuple")
else:
    print("element not found")
'''

#program 21
'''
roll_no=int(input("enter roll no:"))
marks=int(input("enter marks:"))
name=input("enter name:")

t=(roll_no,marks,name)
for i in t:
    print(i)
    
'''
#program 22
'''
prices = (100, 250, 150, 500, 300)

total = 0

for price in prices:
    total = total + price

average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total Bill =", total)
print("Average Price =", average)
print("Highest Price =", highest)
print("Lowest Price =", lowest)
'''
#program 23
'''
temperatures = (32, 35, 31, 30, 36, 34, 33)

total = 0

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    total = total + temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperatures)

print("Maximum Temperature =", maximum)
print("Minimum Temperature =", minimum)
print("Average Temperature =", average)
'''
#program 24
'''
runs = (45, 72, 30, 100, 56, 80, 25, 67, 90, 40)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total Runs =", total)
print("Highest Score =", highest)
print("Lowest Score =", lowest)
print("Average Score =", average)
'''
#program 25
'''
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for n in tuple1:
    if n in tuple2:
        common = common + (n,)

print("Common Elements =", common)
'''
#program 26
'''
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = ()

for n in merged:
    if n not in result:
        result = result + (n,)

print("Merged Tuple =", result)
'''
#program 27
'''
t = (10, 20, 10, 30, 20, 10, 40, 30)

checked = ()

for n in t:
    if n not in checked:
        count = 0

        for x in t:
            if x == n:
                count = count + 1

        print(n, "=", count)

        checked = checked + (n,)

'''
#program 28
'''
t = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Original Tuple =", t)
print("Ascending Order =", ascending)
print("Descending Order =", descending)
      '''
#program 29
'''
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Priya", 28, "A+")
)


print("Patient Records:")

for patient in patients:
    print(patient)


patient_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found:")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if found == False:
    print("Patient not found")


print("\nTotal Number of Patients =", len(patients))


blood_group = input("\nEnter Blood Group: ")

print("Patients with Blood Group", blood_group)

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
        '''
#program 30
'''
employees = (
    (101, "Rahul", 25000),
    (102, "Amit", 30000),
    (103, "Sneha", 28000),
    (104, "Priya", 35000)
)

print("Employee Information:")

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
    '''
