#tuple in python
# t1=tuple()#empty tuple
# print(type(t1),t1)
# tup2=("","")
# print(type(tup2),tup2)

tup1=(1,23,54,78,67,890,98)
# print(tup1)
# print(tup1[1])
# print(tup1[-1])

# i=int(input("Enter number here for tuple operation ::"))
# if i in tup1:
#     print("Yes it is present in tuple")
# else:
#     print("NO it is not present in tuple")
#tup[a:b]
#a=python by defalult place zero in the position
#b=python will return the length of the tuple by default


#**********************************************************************************************

#methods in tuple
#tuples are immutable 
#If I want to change the tuple items then I must convert the tuple items into list

# tup=(1,"Hello",2,"hi",3,"three")
# print(tup)
# temp=list(tup)
# print(type(temp))
# temp.append("buddy")
# print(temp)
# temp.pop(2)
# print(temp)
# tup=tuple(temp)
# print(tup)

#slicing of the tuple

tupl=(1,2,21,32,43,43,35,36,68,20,3)
print(tupl)
# cnt=tupl.index(43,2,7)#first is the number and 1 is the starting index and 8 is the last index
# print("The count of the 43 in tuple is ::",cnt)

print(tupl.index(21))#this will return the index of the given element in the tuple