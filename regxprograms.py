#1.Write a Python program using regular expressions to extract all digits from a given string.
'''
import re

s = input("Enter string: ")
print(re.findall(r'\d', s))
'''

#2.Accept a sentence and display all words beginning with the letter A or a.
'''
import re

s = input("Enter sentence: ")
print(re.findall(r'\b[Aa]\w*', s))
'''

#3.Write a program to count the occurrences of vowels in a given string using regular expressions.
'''
import re

s = input("Enter string: ")
print(len(re.findall(r'[aeiouAEIOU]', s)))
'''

#4.Write a program to extract all uppercase letters from a given string.
"""
import re

s = input("Enter string: ")
print(re.findall(r'[A-Z]', s))
"""
#5.Write a program to identify all spaces, tabs, and newline characters in a text.
'''
import re

s = input("Enter text: ")
print(re.findall(r'[ \t\n]', s))
'''

#6.Write a program to replace multiple consecutive spaces with a single space.
'''
import re

s = input("Enter string: ")
print(re.sub(r' +', ' ', s))
'''
#7.Accept a sentence and display all words containing exactly five characters.
'''
import re

s = input("Enter sentence: ")
print(re.findall(r'\b\w{5}\b', s))
'''
#8.Write a program to identify all words ending with the letter s.
'''
import re

s = input("Enter sentence: ")
print(re.findall(r'\b\w+s\b', s, re.I))
'''
#9.Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.
'''
import re

s = input("Enter string: ")
print(re.sub(r'[^a-zA-Z0-9 ]', '', s))
'''
#10.Write a program to count the number of words in a sentence using regular expressions.
'''
import re

s = input("Enter sentence: ")
print(len(re.findall(r'\b\w+\b', s)))
'''
#11.Write a program to validate a 10-digit Indian mobile number using a regular expression.
'''
import re

n = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', n):
    print("Valid")
    
else:
    print("Invalid")
'''
#12.Accept an email address and check whether it follows a reasonable email format.
'''
import re

e = input("Enter email: ")

if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w{2,}', e):
    print("Valid Email")
else:
    print("Invalid Email")
'''


#13.Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
'''
    import re

s = input("Enter paragraph: ")
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s))
'''

#14.Write a program to identify web addresses beginning with http:// or https://.
'''
import re

s = input("Enter text: ")
print(re.findall(r'https?://\S+', s))

'''
#15.write a program to extract all hashtags from a social media post.
'''
import re

s = input("Enter post: ")
print(re.findall(r'#[A-Za-z0-9_]+', s))
'''
#16.Write a program to check whether a password contains at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character
'''
import re

p = input("Enter password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'

if re.fullmatch(pattern, p):
    print("Valid Password")
else:

    print("Invalid Password")
    '''
#17.Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
 '''
import re

s = input("Enter sentence: ")
print(re.findall(r'\b(\w+)\s+\1\b', s, re.I))
'''
 #18.Write a program to extract six-digit Indian PIN codes from a paragraph.
'''
 import re

s = input("Enter paragraph: ")
print(re.findall(r'\b[1-9]\d{5}\b', s))
'''
#19.Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.
'''
import re

n = input("Enter vehicle number: ")

if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', n):
    print("Valid Format")
else:
    print("Invalid Format")
'''
#20.Write a program to extract file extensions from filenames in a given string.
'''
    import re

s = input("Enter filenames: ")
print(re.findall(r'\.([A-Za-z0-9]+)\b', s))
'''

#21.Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.
'''
import re

s = input("Enter text: ")

s = re.sub(r'<[^>]+>', '', s)
s = re.sub(r'[^\w\s]', '', s)
s = re.sub(r'\s+', ' ', s)

print(s.strip())
'''
#22.	Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.
'''
import re

s = input("Enter invoice text: ")

print("Invoice:", re.findall(r'INV-\d+', s))
print("Dates:", re.findall(r'\d{2}-\d{2}-\d{4}', s))
print("Amounts:", re.findall(r'₹\s?\d+(?:,\d{3})*(?:\.\d{2})?', s))
'''
#23.	Write a program to identify single-line comments in Python source code. Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
'''
import re

s = input("Enter Python code: ")
print(re.findall(r'#.*', s))
'''
#24.	Validate product codes following the pattern ABC-1234-XY, where letters and digits must appear in the specified positions.
'''
import re

c = input("Enter product code: ")

if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', c):
    print("Valid Code")
else:
    print("Invalid Code")
'''
#25.	Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.
'''
    import re

s = input("Enter student details: ")

name = re.search(r'Name:\s*(\w+)', s)
roll = re.search(r'Roll:\s*(\d+)', s)
marks = re.search(r'Marks:\s*(\d+)', s)

if name and roll and marks:
    print("Name:", name.group(1))
    print("Roll:", roll.group(1))
    print("Marks:", marks.group(1))

'''
#26.	Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.
'''
    import re

s = input("Enter research references: ")

print("DOI:", re.findall(r'\b10\.\d{4,9}/\S+', s))
print("Years:", re.findall(r'\b(?:19|20)\d{2}\b', s))
print("Emails:", re.findall(r'[\w.-]+@[\w.-]+\.\w+', s))
print("URLs:", re.findall(r'https?://\S+', s))
'''
