                                                                                    #FOR LOOP

#PROGRAM 1
'''
n=int(input("enter value of n:"))
for i in range(0,n):
    print(i)

'''

#PROGRAM 2
'''
n=int(input("enter value of n:"))
for i in range(0,n):
    if(i%2==0):
        print("even numbers:",i)
'''

#PROGRAM 3
'''
n=int(input("enter value of n:"))
for i in range(0,n):
    if(i%2!=0):
        print("ODD numbers:",i)
'''

#PROGRAM 4
'''
n=int(input("enter number:"))
z=1
for i in range(1,n):
    print(z)
    z*=2
'''
#PROGRAM 5
'''
n = int(input("Enter the value of n: "))

sum = 1   
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    sum = sum + (1 / factorial)

print("Sum of the series =", sum)
'''
#PROGRAM 6
'''
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + sign * (x ** i) / fact
    sign = -sign

print("cos(", x, ") =", sum)
'''

#PROGRAM 7
'''
import math

n = int(input("Enter a number: "))
r = int(math.sqrt(n))

c = 0
for i in range(1, r + 1):
    if r % i == 0:
        c += 1

if c == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
'''
#PROGRAM 8
'''
for i in range(3):
    print("A B C")
'''

#PROGRAM 9
'''
n = int(input("Enter n: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

'''
#PROGRAM 10
'''
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
'''

#PROGRAM 11
'''
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
#PROGRAM 12
'''
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
'''    
                                                                                            #WHILE LOOP
#PROGRAM 1
'''
n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i)
    i = i + 1
'''
#PROGRAM 2
'''
n = int(input("Enter n: "))

i = 2
while i <= n:
    print(i)
    i = i + 2
'''

#PROGRAM 3
'''
n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i)
    i = i + 2
'''
#PROGRAM 4
'''
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1
'''    
#PROGRAM 5
'''
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum= sum +i
    i = i + 2    
print("Sum =", sum)
    
'''
#PROGRAM 6

'''
n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n = n - 1
'''
#PROGRAM 7
'''
n = int(input("Enter n: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1
    '''
#PROGRAM 8
'''
n = int(input("Enter a number: "))

fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial =", fact)
'''
#PROGRAM 10
'''
n = int(input("Enter a number: "))

i = 2
prime = True

while i < n:
    if n % i == 0:
        prime = False
        break
    i = i + 1

if prime and n > 1:
    print("Prime Number")
else:
    print("Not Prime Number")
'''
#PROGRAM 11
'''
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    d = n % 10
    sum = sum + d
    n = n // 10

print("Sum of digits =", sum)
'''
#PROGRAM 12
'''
n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
#PROGRAM 13
'''
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

print("Reverse =", rev)
'''
#PROGRAM 14
'''
n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1
'''
#PROGRAM 15
'''
n = int(input("Enter how many numbers: "))

i = 1
largest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest =", largest)
'''
#PROGRAM 16
'''
n = int(input("Enter how many numbers: "))

i = 1
smallest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest =", smallest)
'''
