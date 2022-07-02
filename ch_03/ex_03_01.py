# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate

if hours > 40 :
    pay2 = (40 * rate) + ((hours - 40) * rate * 1.5)
    print(pay2)
else :
    print(pay)
