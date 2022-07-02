# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user enters
# "done". Write the program to store the numbers the user enters in a list and use
# the max() and min() functions to compute the maximum and minimum numbers after
# the loop completes.

num_list = []

while True :
    user_input = input("Enter a number: ")
    if user_input.lower() == "done" :
        break
    try :
        number = float(user_input)
    except :
        print("Please input numbers only!")
        continue
    num_list.append(number)

print(f"Maximum: {max(num_list)}")
print(f"Maximum: {min(num_list)}")
