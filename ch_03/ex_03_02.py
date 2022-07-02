# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the
# program.

try :
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except :
    print("Error, please enter numeric input")
    quit()

pay = hours * rate
if hours > 40 :
    pay2 = (40 * rate) + ((hours - 40) * rate * 1.5)
    print(pay2)
else :
    print(pay)
