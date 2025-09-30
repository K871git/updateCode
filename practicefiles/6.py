#list in python
#we can done indexing
#l1=[23,"hello",45.56,(2,3)]

#count total number of elements which has first and last digit same 
# list1=['AnA','LOL','456','919',"hi"]
# c=0
# for a in list1:
#     if len(a)>=2 and a[0]==a[-1]:
#         c+=1
# print(f"total strings ={c}")

num=[2,6,78,5,4,17,87,65,34,100,45,1000]
print(num)
# num.sort()

# print(num)
# num.reverse()
# print(num)
# print(num[11])
# print(len( num))

# print(num[-5:-1])
# print(num[:])
#in slicing when I give positive number then last number get excluded and then I give negetive number that time the first number get excluded

# print(num[::])
# print(num[::2]) #this third parameter will skip the numbers position of given number
#in negetive slicing -1 is recomanded not go for -2 and more

# print(max(num))
# print(min(num))

# num.append(333)
# print(num)#add in the end

# print(num)
# num.insert(1,23)
# print(num)
# num.remove(1000)

num.pop(1)#taking index but default is -1 or remove the last element
print(num)
