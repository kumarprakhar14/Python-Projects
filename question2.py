""" Write a python program that accepts a sequence of lines as input(blankline
 to terminate) and prints all the lines in upper case."""

p = ""
print("Enter some text. Enter a blank line to terminate input.")
while(True):
    string = input()
    p = p + string
    if(len(string) == 0):
        break

print(p.upper())
