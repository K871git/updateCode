# Strings Are Immutable
# This means that once you have created a string, you cannot change it. Although this might
# seem like a bad thing, it really isn't. We will see why this is not a limitation in the various
# programs that we see later on.

#writing the multiline 
"""this 
is the 
multiline 
string
"what is your name" or
'what is your name'
hance I can use double or single quote in multiline string

"""

#formating the string

#using the format()

age=20
name="harry"

# print("the boy name {0} is at age {1}".format(name,age))
# print("why is {0} playing with python".format(name))


# Python starts counting from 0 which means that first position is at index 0, second position is at index 1, and so on.


# Notice that we could have achieved the same using string concatenation:

 # name + ' is ' + str(age) + ' years old'


# but that is much uglier and error-prone. 
# Second, the conversion to string would be done automatically by the format method instead of the explicit conversion to strings needed in this case. 
# Third, when using the format method, we can change the message without having to deal with the variables used and vice-versa.



# Also note that the numbers are optional, so you could have also written as:
age = 20
name = 'harry'
# print('{} was {} years old when he wrote this book'.format(name, age))
# print('Why is {} playing with that python?'.format(name))
# which will give the same exact output as the previous program.


#formating in different way

# print('{1:.3f}'.format(1.0/3,3/5))
# print('{1:.3f}'.format(2/3,3))
x="hello"
# print("there is %s and %s number of %s program"%('45','56',x))
#formatting the string using mode character

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
# print('{0:_^11}'.format('hello'))

#declare the variables inside the format
#hance it is keyword basedz
# print('My name is {name} and I am a {proff}'.format(name="harry",proff="programmer"))

a="34"
b=56

# letter="hello{1} this{0} is kishor"
# print(f"hello{a} there is {b}")#adding the f at the start of the string (using the variable name to populate)
#if I want to preserve the curly braces then I have to use nested format for this like {{hi}}

print('{0:} to | {1:<3}'.format("hello","sdflaf"))


a='''
this is the comment
this is the comment
this is the comment
this is the comment
'''
print(a)

b=  """hello this is another docstring
    """