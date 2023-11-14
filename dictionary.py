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

#dictionary is a structure in python used to store the key-value pair.
#for instance, in the code below subject is the key while marks is its value.

marks = {"english": 97, "maths": 56, "chemistry": 89}
print(marks)
print(marks["maths"])

#updation
marks["physics"] = 78
print(marks)

#modification
marks["maths"] = 96
print(marks)