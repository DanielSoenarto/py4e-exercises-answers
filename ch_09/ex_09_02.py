# Exercise 2: Write a program that categorizes each mail message by which day of 
# the week the commit was done. To do this look for lines that start with "From",
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).

fname = input("Enter a file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhand = open(fname)

days = dict()
for line in fhand :
    if line.startswith("From ") :
        lines = line.rstrip()
        # print(lines)
        words = lines.split()[2]        # Getting the days only
        print("printing the words...")
        print(words)
        print(type(words))
        days[words] = days.get(words, 0) + 1

print("-----dictionary-----")
print(days)
