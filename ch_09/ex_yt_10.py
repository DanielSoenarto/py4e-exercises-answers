# Find the top 5 words in a file
# Note: this is the exercise from Freecodecamp youtube Channel and not the book

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
    for word in words:
        # idiom: retrieve/create/update counter
        counts[word] = counts.get(word, 0) + 1

# making the tuple
tmp = []
for k,v in counts.items():
    newtup = (v, k)
    tmp.append(newtup)

# print(f"unsorted: {tmp}")

# sort and reverse
tmp_sorted = sorted(tmp, reverse = True)
# print(f"sorted {tmp_sorted}")

# choose top 5 words
for k,v in tmp_sorted[:5]:
    print(v,k)
