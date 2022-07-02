# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop (see Section
# [maximumloop]) to find who has the most messages and print how many messages
# the person has.

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

# print(email_address)

max_key = None
max_value = 0
for key,value in email_address.items() :
    if value > max_value :
        max_value = value
        max_key = key

print(max_key, max_value)