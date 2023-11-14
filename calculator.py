#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pratiksha kiran
#
# Created:     01/10/2023
# Copyright:   (c) pratiksha kiran 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("enter first no.")
operator = input("enter the operator- +, -, *, /, %")
second = input("enter second no.")

first = int(first)
second = int(second)

if operator=='+':
    print("the sum is: ",first + second)
elif operator=='-':
    print("the differnce is: ",first - second)
elif operator=='*':
    print("the product is: ",first * second)
elif operator=='/':
    print("the quotient is: ",first / second)
elif operator=='%':
    print("the remainder is: ",first % second)
else :
    print("Invalid Operation")