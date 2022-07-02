# Exercise 1: Write a program which repeatedly reads numbers until the user enters 
# "done". Once "done" is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

count = 0
total = 0
print("CALCULATOR. Type 'done' to quit.")
while True : 
    user_input = input("Enter a number: ")
    if user_input.lower() == "done" :
        break
    try :
        number = float(user_input)
    except :
        print("bad data. Please enter numeric input. If you would like to exit, type 'done'.")
        continue
    count = count + 1
    total = total + number

try :
    average = float(total/count)
    print(f"total: {total}, count: {count}, average: {average}")
except :
    pass