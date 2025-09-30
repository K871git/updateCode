#conditionals

# num=40
# guess=int(input('Enter the Integer no :: '))#convert input string into the integer

# if guess==num:
#     print("congratulations, You get it")
    
# elif guess<num:
#     print("number is little heigher then that")
    
# else :
#     print("It is little lower then that");

    
# print("thank you")

# We supply a string to the built-in input function which prints it to the screen and waits for
# input from the user. Once we enter something and press kbd:[enter] key, the input()
# function returns what we entered, as a string. We then convert this string to an integer using
# int and then store it in the variable guess . Actually, the int is a class but all you need to
# know right now is that you can use it to convert a string to an integer (assuming the string
# contains a valid integer in the text).

# Remember that the elif and else parts are optional. A minimal valid if statement is:

# if True:
#  print('Yes, it is true')

# There is no switch statement in Python. You can use an if..elif..else statement to
# do the same thing (and in some cases, use a dictionary to do it quickly

#While Statement :

# The while statement allows you to repeatedly execute a block of statements as long as a
# condition is true. A while statement is an example of what is called a looping statement. A
# while statement can have an optional else clause.

# num=34
# run=True

# while run:
#     guess=int(input('Enter the Integer :: '))
    
#     if guess == num:
#         print("Wow, You get it...!")
#         run=False
#     elif guess<num:
#         print("It is little heigher then that")
#     else :
#         print("it is little lower then that")
         
# else:
#     print("while loop is over")
    
# print("done")

#for loop statement

# The for..in statement is another looping statement which iterates over a sequence of
# objects i.e. go through each item in a sequence

# for i in range(0,5):
#     print(i)
    
# else:
    # print("for loop is over")
    
#     What we do here is supply it two numbers and range returns a sequence of numbers
# starting from the first number and up to the second number

#  By default, range takes a step count of 1. If we supply a third
# number to range , then that becomes the step count

# for i in range(1,8,2):
#     print(i)

# for i in range ( {starting step}, {end step(don't count)}, {no. of steps})

# print(list(range(5)))

#Break Statement

# The break statement is used to break out of a loop statement i.e. stop the execution of a
# looping statement, even if the loop condition has not become False or the sequence of
# items has not been completely iterated over.


# while True:
#     s=input("Enter something ::")
#     if s=="quit":
#         break
#     print("The length of the string is :: ",len(s))
# print(56+'hello')

#continue statement

# The continue statement is used to tell Python to skip the rest of the statements in the
# current loop block and to continue to the next iteration of the loop.
while True:
    s=input("Enter here :: ")
    if s=="quit":
        break
    if len(s)<3:
        print("too small")
        continue
    print("input having sufficient length")
        
        
    