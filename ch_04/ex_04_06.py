# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate) :
    pay = hours * rate
    if hours > 40 :
        pay2 = (40 * rate) + ((hours - 40) * rate * 1.5)
        return pay2
    else :
        return pay

try :
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except :
    print("Error, please enter numeric input")
    quit()

payment = computepay(hours, rate)
print(f"the payment is {payment}")