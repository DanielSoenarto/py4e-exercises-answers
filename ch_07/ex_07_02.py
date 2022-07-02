# Exercise 2: Write a program to prompt for a file name, and then read through the
# file and look for lines of the form:

# X-DSPAM-Confidence:0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the
# line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fname = input("Enter the file name: ")
fhand = open(fname)

count = 0
total = 0
for line in fhand :
    if line.startswith("X-DSPAM-Confidence:") :
        num_start = line.find("0.")
        num_end = line.find(" ", num_start)
        num = float(line[num_start:num_end])
        count = count + 1
        total = total + num

average = total / count
print(f"the average spam confidence is: {average}")