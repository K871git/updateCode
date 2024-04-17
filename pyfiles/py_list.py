# import print(object(s), separator=separator, end=end, file=file, flush=flush)
# Python Lists
# mylist = ["apple", "banana", "cherry"]

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist1[2:5])

# list2=["hello",23,"this",45,"mix list"]

# for val in list2:
#     print(val)
    
    
# This example returns the items from the beginning to, but NOT including, "kiwi":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# print(thislist[-1:-4])#this will return an empty list

# # Check if "apple" is present in the list:

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
  
#remove in list
  
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
# #in case of more than one occurance that time it only remove the first occurance

# # Remove Specified Index
# # The pop() method removes the specified index.

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)#this will remove the item from last

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist) #you can add any iterable object (tuples, sets, dictionaries etc.).

list1=[22,33,44]
list1.insert(5,"hello")
print(list1)#no matter what index we given, if index number exceded that time it will apend number in the list

list2=[222,333,444,555,666,777,888]
# i=0
# while i < len(list2):
#   print(list2[i])
#   i+=1

# for val in range(len(list2)):
#   print(list2[val])

# thislist = ["apple", "banana", "cherry"]
# thislist.extend(list2)
# [print(x) for x in thislist]

#I can achive comprehansion using apend keyword
l1=["apple", "banana", "alis","alita"]
# l2=[]
l2=list()
print(type(l2))
for val in l1:
  if 'a' in val:
    l2.append(val)
print(l2)

#this can be done in one line 
# ruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)