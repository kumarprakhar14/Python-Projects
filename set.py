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

#set stores unique values only unlike list and tuple.
#there is no indexing of elements in the case of sets thus sets are known as
#unordered  structures.

marks = {98, 97, 43, 34, 34}  # 34 would be printed only once. Why?
print(marks)

for score in marks:
    print(score)