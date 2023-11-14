#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pratiksha kiran
#
# Created:     02/10/2023
# Copyright:   (c) pratiksha kiran 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#tuple is immutable which means that we can't modify, append, delete elements
#as we did in list

marks = (95, 98, 97, 97, 97)

print("97 apears " +str(marks.count(97)) + " times")
print("the index of 98 is " + str(marks.index(98)))