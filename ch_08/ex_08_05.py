# Exercise 5: Write a program to read through the mail box data and when you find
# line that starts with "From", you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.

text = open("mbox-short.txt")

for line in text:
    words = line.rstrip().split()
	# guardian in a compound statement (guardian comes before!)
    if len(words) < 3 or words[0] != "From" :
        continue
    print(words[2])
