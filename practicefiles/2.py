### string ###

s="hello there"

# print(s)
# l=len(s)
# print(len(s))
# print(type(s))

###iteration of string

##using while loop

# i=0
# s1=''
# while i<len(s):
#     s1= s1+s[i]
#     i=i+1
# print(s1)

##using for loop
# for i in s:
#     print(i)

# p='JKLMNOP'
# S='ack'
# P='Q'
# s='uack'
# for i in p:
#     if i not in p:
#      print(P+s)
#     else:
#      print(i+S)

###string slicing

# s1=s[:]
# print(s1)
t="Example"
# print(t[0:5])
# print(len(t))
# print(t[:7])#will exclude the last letter
# print(t[:len(t)-1])
# print(t[4:])#4th letter to the last letter

# print(t[-1])#-1 will return last character of the string
# print(t[-4:-1])
# print(t[:])

#Strings are immutable constants

#searching in the string

#string methods

# s="HELLO THERE THERE" 
# # print(s)

# a=s.capitalize()#capitalize first letter
# print(a)

# b=s.casefold()#convert into lowercase
# print(b)

# c=s.center(20)#takes an argument
# print(c)

# d=s.count("THERE")#returns how many time given argument occur in the string
# print(d)

# e=s.encode()
# print(e)

# print("The {banana} is gonna sell at Rs.{rs}/- only".format(banana="banana",rs=60))

# hi="this is indexing"#we give the range for the searching
# a=hi.index("in",10,15)
# print(a)

# #isalnum(): checking the all the characters of the string are alphanumaric
# str="hello112"
# s=str.isalnum()
# print(s)

# t=str.isalpha()#check string contains only alphabet not numbers
# print(t)


#replace
# hi="I like cricket"
# print(hi)
# s=hi.replace("cricket", "football")
# print(s)

#split concept
# h1="hello there This is Split concept"
# t=h1.split()
# print(t)

#multiline string
# m='''Hello this is 
# multiline 
# string 
# in which 
# I'm gonna use
# splitline concept'''
# mod1=m.splitlines()
# print(mod1)


#swapcase method
# s="ThiS Is SWapCAse MeThOd"
# s1=s.swapcase()#convert lowercase to uppercase and viceversa
# print(s1)

#title method
# t="this is our match and we goona make it"
# mt=t.title()
# print(mt)

#translate method

# txt="Hi hello !"
# x="hello"
# y="harry"
# mytable=str.maketrans(x,y)
# print(txt.translate(mytable))

#zphill
t="sd"
x=t.zfill()#filling the zero with given size before the printing the string
print(x)