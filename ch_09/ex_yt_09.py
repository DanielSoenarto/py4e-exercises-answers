# Count the frequency of each word in a file & store it in a dictionary.
# Then, find the most common word.
# Note: This is the exercise from Freecodecamp youtube Channel and not the book

file = input("Enter the file name: ")
if len(file) < 1:
    file = 'clown.txt'
else:
    file = 'intro.txt'
handle = open(file)

counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    print(words)
    print(type(words))
    for word in words:
        # idiom: retrieve/create/update counter
        counts[word] = counts.get(word, 0) + 1

print(counts)
largest = -1
bigword = None
for word, count in counts.items():
    if count > largest:
        bigword = word
        largest = count

print(bigword, largest)
