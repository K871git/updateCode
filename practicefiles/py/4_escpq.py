# Since we are discussing formatting, note that print always ends with an invisible "new
# line" character ( \n ) so that repeated calls to print will all print on a separate line each. To
# prevent this newline character from being printed, you can specify that it should end with a
# blank:

print('a', end='')
print('b')

str='what\'s your name ??'#using the escape sequence for resolving the confusion
print(str)

#new line

print("This is the first line.\
    and this is the second line")
print("new line \n hello")