#factorial
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i

    return fact
n = int(input("entr a number:"))
print("factorial:",factorial(n))
'''
'''

#even or odd

def check_even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
n= int(input("enter a number:"))
print("number is :",check_even_odd(n))

'''
'''
#greater of two nummbers

def greater(a,b):
    if a>b:
        return a
    else:
        return b



a=int(input("enter first number:"))
b=int(input("second number:"))
print(greater(a,b))
'''
'''
#simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))
'''
'''
#prime number

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False

    return True 
n=int(input("enter a nnumber:"))
print("number is:",is_prime(n))
'''
'''
#area of circle

def circle_area(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area =", circle_area(r))

#sum of first n natural number
def natural_sum(n):
    return n * (n + 1) // 2

n = int(input("Enter n: "))
print("Sum =", natural_sum(n))
'''
'''
#power
def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Answer =", power(base, exponent))

#Largest Element Without max()
def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

numbers = [10, 25, 5, 40, 15]

print("Largest =", largest(numbers))
'''
'''

#count vowels
def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count

s = input("Enter a string: ")
print("Vowels =", count_vowels(s))
'''
'''
#Reverse String
def reverse_string(s):
    return s[::-1]

s = input("Enter string: ")
print("Reverse =", reverse_string(s))
'''
'''
#palindrome
def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter string or number: ")
print(palindrome(value))
'''
'''
#Average of List
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]

print("Average =", average(numbers))
'''
'''
#Count Occurrences
def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count += 1

    return count

numbers = [1, 2, 2, 3, 2, 4]
element = int(input("Enter element: "))

print("Occurrences =", count_element(numbers, element))
'''
'''
#Unique Elements
def unique_elements(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5]

print("Unique elements =", unique_elements(numbers))
'''
'''
#second largest

ef second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    return unique[-2]

numbers = [10, 25, 5, 40, 30]

print("Second largest =", second_largest(numbers))
'''
'''
#First n Fibonacci Numbers
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))

print(fibonacci(n))
'''
'''

#Percentage and Grade
def result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = result(*marks)

print("Percentage =", percentage)
print("Grade =", grade)
'''
'''
#Electricity Bill Using Slabs
def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    return bill

units = int(input("Enter units: "))
print("Electricity Bill =", electricity_bill(units))
'''
'''
#Gross Salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

basic = float(input("Enter basic salary: "))

print("Gross Salary =", gross_salary(basic))
#Minimum, Maximum, Sum and Average
def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for n in numbers:
        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = [10, 20, 5, 40, 30]

result = calculate(numbers)

print("Minimum =", result[0])
print("Maximum =", result[1])
print("Sum =", result[2])
print("Average =", result[3])
'''
'''
#Student Records
def calculate_student(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


students = [
    ("Rahul", 101, [80, 75, 90, 85, 88]),
    ("Amit", 102, [70, 65, 75, 80, 72]),
    ("Priya", 103, [90, 92, 88, 95, 91])
]

percentages = []

for student in students:
    name = student[0]
    roll = student[1]
    marks = student[2]

    total, percentage, grade = calculate_student(marks)
    percentages.append(percentage)

    print("\nName:", name)
    print("Roll No:", roll)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

print("\nClass Average =", sum(percentages) / len(percentages))

highest = max(students, key=lambda x: sum(x[2]))
lowest = min(students, key=lambda x: sum(x[2]))

print("Highest Scorer =", highest[0])
print("Lowest Scorer =", lowest[0])
'''
'''
#Banking System
balance = 0
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Balance =", balance)


def transaction_history():
    print("\nTransaction History:")

    for transaction in transactions:
        print(transaction)


deposit(5000)
withdrawal(1000)
withdrawal(5000)
balance_enquiry()
transaction_history()
'''
'''
#library management
books = {
    "Python": True,
    "Java": True,
    "C Programming": True,
    "Database": True
}


def add_book(name):
    books[name] = True
    print("Book added")


def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(name):
    if name in books:
        books[name] = True
        print("Book returned")


def search_book(name):
    if name in books:
        print("Book found")
    else:
        print("Book not found")


def display_books():
    print("\nAvailable Books:")

    for name, available in books.items():
        if available:
            print(name)


display_books()
issue_book("Python")
display_books()
return_book("Python")
search_book("Java")
#Hospital Bill
def consultation_charge():
    return 500


def laboratory_charge():
    return 1000


def medicine_charge():
    return 1500


def room_charge(days):
    return days * 1000


def discount(category, amount):
    if category == "senior":
        return amount * 0.20
    elif category == "student":
        return amount * 0.10
    else:
        return 0


def final_bill(category, days):
    total = (consultation_charge() +
             laboratory_charge() +
             medicine_charge() +
             room_charge(days))

    discount_amount = discount(category, total)

    return total - discount_amount


category = input("Enter category (senior/student/general): ")
days = int(input("Enter room days: "))

print("Final Bill =", final_bill(category, days))
'''
'''
#Shopping Invoice
products = {}


def add_product(name, price, quantity):
    products[name] = [price, quantity]


def remove_product(name):
    if name in products:
        del products[name]


def subtotal():
    total = 0

    for price, quantity in products.values():
        total += price * quantity

    return total


def coupon_discount(amount):
    return amount * 0.10


def gst(amount):
    return amount * 0.18


def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)

    final = taxable + tax

    print("Subtotal =", sub)
    print("Discount =", discount)
    print("GST =", tax)
    print("Final Amount =", final)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

invoice()
'''
'''
#Recursive Binary Search
def binary_search(numbers, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid

    elif target < numbers[mid]:
        return binary_search(numbers, low, mid - 1, target)

    else:
        return binary_search(numbers, mid + 1, high, target)


numbers = [10, 20, 30, 40, 50, 60]

target = int(input("Enter element: "))

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")s

'''
