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

age = input("enter your age")

if int(age) >= 18:
    print("you can vote")

elif int(age) < 18 and int(age) > 3:
    print("you are in school")

else:
    print("you are a kid")

print("Thank You")