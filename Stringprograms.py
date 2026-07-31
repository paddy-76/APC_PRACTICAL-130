
#program 1                                                                                    #STRINGS
"""
s=input("enter any string:")
count =0
for i in s:
    count =count+1
print(count)  
"""
#PROGRAM 2
'''
s = input("Enter a string: ")

v = c = d = sp = sc = 0

for ch in s:
    if ch in "AEIOUaeiou":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1
    else:
        sc += 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)

'''

#PROGRAM 3
'''
s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reverse =", rev)
'''

#PROGRAM 4
'''
s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#PROGRAM 5
'''
s = input("Enter a string: ")

u = l = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Uppercase =", u)
print("Lowercase =", l)
'''

#PROGRAM 6
'''
s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

print(s.replace(old, new))
'''
#PROGRAM 7
'''
s = input("Enter a string: ")

new = ""

for i in s:
    if i != " ":
        new += i

print("Result =", new)
'''
#PROGRAM 8
'''
s = input("Enter a string: ")
ch = input("Enter character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency =", count)
'''

#PROGRAM 9
'''
s = input("Enter a string: ")

print("First Character =", s[0])
print("Last Character =", s[-1])
'''
#PROGRAM 10
'''
s = input("Enter a string: ")

for i in s:
    print(i, "=", ord(i))
'''
#PROGRAM 11
'''
s = input("Enter a sentence: ")

words = s.split()

print("Total Words =", len(words))
'''
#PROGRAM 12
'''
s = input("Enter a sentence: ")

words = s.split()
long = words[0]

for i in words:
    if len(i) > len(long):
        long = i

print("Longest Word =", long)
'''
#PROGRAM 13
'''
s = input("Enter a sentence: ")

words = s.split()
short = words[0]

for i in words:
    if len(i) < len(short):
        short = i

print("Shortest Word =", short)
'''
#PROGRAM 14
'''
s = input("Enter a sentence: ")

print(s.title())
'''
#PROGRAM 15
'''
s = input("Enter a string: ")

for i in s:
    if s.count(i) > 1:
        print(i)
'''
#PROGRAM 16
'''
s = input("Enter a string: ")

for i in set(s):
    print(i, "=", s.count(i))
'''
#PROGRAM 17
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
'''
#PROGRAM 18
 '''   
s = input("Enter a string: ")

new = ""

for i in s:
    if i not in new:
        new += i

print("Result =", new)
    ''''
#PROGRAM 19
 '''
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found") 
'''

#PROGRAM 20
'''
s = input("Enter a sentence: ")
word = input("Enter word: ")

words = s.split()

count = 0

for i in words:
    if i == word:
        count += 1

print("Occurrences =", count) 
'''
#PROGRAM 21
'''
p = input("Enter Password: ")

u = l = d = s = 0

for i in p:
    if i.isupper():
        u = 1
    elif i.islower():
        l = 1
    elif i.isdigit():
        d = 1
    else:
        s = 1

if len(p) >= 8 and u and l and d and s:
    print("Valid Password")
else:
    print("Invalid Password")
'''

#PROGRAM 22
'''
s = input("Enter String: ")

count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1

print(s[-1] + str(count))
'''
#PROGRAM 23
'''
s = input("Enter String: ")

result = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

if len(result) < len(s):
    print(result)
else:
    print(s)
'''
#PROGRAM 24
'''
s = input("Enter String: ")

ch = ""
m = 0

for i in s:
    if s.count(i) > m:
        m = s.count(i)
        ch = i

print("Most Frequent Character =", ch)
'''
#PROGRAM 25
'''
s = input("Enter String: ")

freq = {}

for i in s:
    freq[i] = s.count(i)

f = sorted(freq.values(), reverse=True)

second = f[1]

for k in freq:
    if freq[k] == second:
        print("Second Most Frequent =", k)
        break
'''
#PROGRAM 26
'''
text = input("Enter Message: ")
key = 3

result = ""

for i in text:
    result += chr(ord(i) + key)
'''
#PROGRAM 27
'''
email = input("Enter Email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
print("Encrypted =", result)
'''
#PROGRAM 28
'''
s = input("Enter Sentence: ")

words = s.split()

for i in set(words):
    print(i, "=", words.count(i))
'''
#PROGRAM 29
'''
s = input("Enter Sentence: ")

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
'''
#PROGRAM 30
s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")
