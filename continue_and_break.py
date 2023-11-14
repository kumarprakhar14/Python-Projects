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

students = ["ram", "shyam", "kishan", "radha", "radhika"]
for students in students:
    if students == "radha":
        break;
    print(students)

for students in students:
    if students == "kishan":
        continue;
    print(students)