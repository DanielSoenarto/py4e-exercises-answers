# Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence: 0.8475 '

# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into
# a floating point number.

num_start = str.find("0.")
print("starts at", num_start)
num_end = str.find(" ", num_start)
print("ends at", num_end)

num = float(str[num_start:num_end])
print(num)
print(f"the type is {type(num)}")