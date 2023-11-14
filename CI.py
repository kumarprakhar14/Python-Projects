#program to find CI when interest is compounded anually

P = float(input("enter the principal amount"))
r = float(input("enter the rate of interest"))
t = float(input("enter the time period"))
A = (P*((1 + r)/100))**t
CI = A-P
print("the CI is: ", CI)
