# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

num_list = []

while True :
    user_input = input("Enter a number: ")
    if user_input.lower() == "done" :
        break
    try :
        number = float(user_input)
    except :
        print("Please enter numeric input or type 'done' to exit.")
        continue
    num_list.append(number)

try :
    max_num = num_list[0]
    for i in num_list :
        if i > max_num :
            max_num = i

    min_num = num_list[0]
    for j in num_list :
        if j < min_num :
            min_num = j
    
    print(f"the max number is {max_num} and the min number is {min_num}")

except :
    pass
