# Program to calculate the area of a triangle
"""
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print("Area of Triangle =", area)
"""

# Program to calculate the area of a square
"""
side = float(input("Enter the side of the square: "))

area = side ** 2

print("Area of Square =", area)
"""

# Program to calculate the volume of a sphere

pi = 3.14159

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * pi * radius ** 3

print("Volume of Sphere =", volume)

# Program to calculate the total surface area of a cylinder

pi = 3.14159

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

tsa = 2 * pi * radius * (radius + height)

print("Total Surface Area of Cylinder =", tsa)


#write a pgm to convert pounds into kgs , km into miles
"""
pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.453592
print("Weight in kg =", kg)

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print("Distance in miles =", miles)
"""
#FActorial program
"""
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact*i

print("Factorial =", fact)
"""
#wap to check number is pallindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#wap to convert decimal to binary,decimal to octal,to hexadecimal
num = int(input("Enter a decimal number: "))

print("Binary =", bin(num))
print("Octal =", oct(num))
print("Hexadecimal =", hex(num))

## Factors of a Number
num = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        
# Program to check whether a number is Prime or Not Prime

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
# Program to find the ASCII value of a character

ch = input("Enter a character: ")

ascii_value = ord(ch)

print("ASCII value of", ch, "is", ascii_value)        
