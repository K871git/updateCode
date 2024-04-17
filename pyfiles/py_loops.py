#iteration statements in python
# Loop Control Statements
# Statements used to control loops and change the course of iteration are called control statements. All the objects produced within the local scope of the loop are deleted when execution is completed.

# Python programming language provides two types of loops – For loop and While loop to handle looping requirements. Python provides three ways for executing the loops.

# Loops in Python – For, While and Nested Loops

#  While Loop 
# while expression:
#     statement(s)
    
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
    
# Using else statement with While Loop in Python

# while condition:
#      # execute these statements
# else:
#      # execute these statements

count = 0
while (count < 3):
	count = count + 1
	print("Hello Geek")
else:
	print("In Else Block")


# For Loop in Python

# For Loop Syntax:

# for iterator_var in sequence:
#     statements(s)

# n = 4
# for i in range(0, n):
#     print(i)


print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)
print("\nString Iteration")
s = "Geeks"
for i in s:
	print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),

# Iterating by the Index of Sequences

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
    
# Using else Statement with for Loop in Python

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")
    
# Nested Loops

# for iterator_var in sequence:
#    for iterator_var in sequence:
#        statements(s)
#    statements(s)

# while expression:
#    while expression: 
#        statement(s)
#    statement(s)

# from __future__ import print_function
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.

# Example: This Python code iterates through the characters of the string ‘geeksforgeeks’ using a ‘for' loop. However, it doesn’t perform any specific action within the loop, and the ‘pass' statement is used. After the loop, it prints “Last Letter :” followed by the last character in the string, which is ‘s’

# for letter in 'geeksforgeeks':
#     pass
# print('Last Letter :', letter)


