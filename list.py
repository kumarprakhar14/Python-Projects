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

marks = [98, 96, 34, "maths"]
print(marks)
print(marks[0])
print(marks[-1])

#negative indexing  means that the indexing begins from
#the back

print(marks[0:2])
for score in marks:
    print(score)

marks.append(99)
marks.insert(0, 43)
print(marks)
print(99 in marks)
print(len(marks))
marks.clear() #clears all list of items
print(marks)