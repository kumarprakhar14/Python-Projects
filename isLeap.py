year = int(input("Enter the year to check if it is Leap year or not."))
isLeap = False

if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    isLeap = True
print(isLeap)