# Exercise 3: Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from each email
# address, and print the dictionary.

fname = input("Enter a file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fhand = open(fname)

email_address = dict()
for line in fhand :
    if line.startswith("From "):
        # print(line)
        lines = line.rstrip()
        email = lines.split()[1]
        email_address[email] = email_address.get(email, 0) + 1

print(email_address)
