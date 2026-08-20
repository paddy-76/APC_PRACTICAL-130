#program 1

s={45,4,6,8,0}
print(s)

#program 2
l=[12,13,11,12,13,10]
set(l)
print(set(l))

#program 3

s={"banana","apple","guava","mango"}
print(s)
s.add("grapes")
print(s)

#program 4
'''
s={"harsh","prathmesh","nikhil","pruthvi"}
a=input("enter a name:")
if a in s:
    print("name found")
'''
#program 5

s={"kolhapur","pune","satara","mumbai"}
print(len(s))

#program 6

s={'pyhton','c++','c#','swift','php'}
for i in s:
    print(i)


#program 7
    
s={45,4,6,8,0}
s.remove(0)
print(s)

#program 8
l=[12,13,11,12,13,10]
set(l)
print(set(l))

#program 9
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.union(set2)

print("Union:", result)

#program 10
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.intersection(set2)

print("Common elements:", result)

#program 11
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

first = set1.difference(set2)
second = set2.difference(set1)

print("First set but not second:", first)
print("Second set but not first:", second)

#program 12
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)

#program 13
set1 = {10, 20}
set2 = {10, 20, 30, 40}

result = set1.issubset(set2)

print("First set is subset of second:", result)

#program 14

set1 = {10, 20, 30, 40}
set2 = {10, 20}

result = set1.issuperset(set2)

print("First set is superset of second:", result)

#program 15
set1 = {10, 20, 30}
set2 = {40, 50, 60}

result = set1.isdisjoint(set2)

print("Sets have no common elements:", result)

#program 16

set1 = {10, 20, 30}
set2 = {40, 50, 60}

if set1==set2:
    print("both are equal set")
else:
    print("unequal")

#program 17

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

common = set1.intersection(set2)

print("Common elements:", common)

#program 18
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

first_only = set1.difference(set2)
second_only = set2.difference(set1)

print("First set but not second:", first_only)
print("Second set but not first:", second_only)

#program 19
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)

#program 20
set1 = {10, 20, 30, 40}
set2 = {10, 20}

if set1.issuperset(set2):
    print("First set is a superset of second set")
else:
    print("First set is not a superset of second set")

#program 21
student1 = {"Python", "Java", "Maths", "English"}
student2 = {"Python", "Java", "Science", "English"}

common = student1.intersection(student2)

print("Subjects studied by both students:", common)

#program 22
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}


common = employee1.intersection(employee2)

unique_employee1 = employee1.difference(employee2)

unique_employee2 = employee2.difference(employee1)

all_skills = employee1.union(employee2)

print("Common skills:", common)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)

#program 23
available_books = {"Python", "Java", "C++", "SQL", "HTML"}
requested_books = {"Python", "SQL", "JavaScript", "Java"}

available_requested = requested_books.intersection(available_books)

print("Requested books that are available:", available_requested)

#program 24
 first_day = {101, 102, 103, 104, 105}
second_day = {103, 104, 105, 106, 107}


unique_visitors = first_day.union(second_day)

returning_visitors = first_day.intersection(second_day)


first_day_only = first_day.difference(second_day)


second_day_only = second_day.difference(first_day)

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("First day only:", first_day_only)
print("Second day only:", second_day_only)

#program 25
user1_friends = {"Amit", "Rahul", "Priya", "Sneha"}
user2_friends = {"Priya", "Sneha", "Rohan", "Kiran"}
mutual_friends = user1_friends.intersection(user2_friends)

user1_unique = user1_friends.difference(user2_friends)

user2_unique = user2_friends.difference(user1_friends)

total_friends = user1_friends.union(user2_friends)

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", user1_unique)
print("Friends unique to User 2:", user2_unique)
print("Total unique friends:", total_friends)
