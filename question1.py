# Write a python code to solve the Quadratic Equation ax^2 + by + c
# by getting input of coeffients from the user.

a = float(input("Enter the coeffient of x^2."))
b = float(input("Enter the coeffient of x."))
c = float(input("enter the constant term."))
D = (pow(b,2)) - 4*a*c
root_1 = (-b + pow(D, 0.5))/(2*a)
root_2 = (-b - pow(D, 0.5))/(2*a)
print("the root of the given quadratic eqaution is: ", root_1, root_2)
