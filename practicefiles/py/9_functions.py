# Functions are reusable pieces of programs. They allow you to give a name to a block of
# statements, allowing you to run that block using the specified name anywhere in your
# program and any number of times. This is known as calling the function.

#function to call the hello world (function without parameter)

def helloWorld():
    #block of function
    print("hello world")
#end of the function


# helloWorld() #calling of the function



#function parameters

#function for finding the greater number by providing the parameters

# def paraFun(a,b): #here a and b are parameters
#     if a>b:
#         print(a," is greater")
#     elif a==b:
#         print("Both x = {} and y = {} are equal".format(a,b))
#     else:
#         print(b," is greater")

# paraFun(4,5)

# x=int(input('enter the integer for compare ::'))
# y=int(input('enter the integer for compare ::'))


# paraFun(x,y) #variables are as arguments hance value of argument x assign to the parameter a and value of argument y assign to the parameter b


#Local varibles

# When you declare variables inside a function definition, they are not related in any way to
# other variables with the same names used outside the function - i.e. variable names are
# local to the function. This is called the scope of the variable.
#  All variables have the scope of
# the block they are declared in starting from the point of definition of the name.

x=50 #local to the main block of statement
def locVar(x):
    print("X is the ::",x)
    x=5 #local to the locVar() function
    print("changing x to the :: ",x)
    
locVar(x)

print("value of X is :: ",x)    
   
   
#global statement

# We do this using the global statement. It is impossible to assign
# a value to a variable defined outside a function without the global statement   

# You can specify more than one global variable using the same global statement e.g.
# global x, y, z

g=50

def globalFun():
    global g
    print("The value of the g is :: ",g)
    g=8
    print("The global value of the g is :: ",g)
    
globalFun()

print("The value of the g is :: ",g)    

#default argument values

# You can specify default argument values for parameters by
# appending to the parameter name in the function definition the assignment operator ( = )
# followed by the default value.

def say(massage, times=1): 
    print(massage*times )
    
    
say("hello")
say("hi",times=3)


