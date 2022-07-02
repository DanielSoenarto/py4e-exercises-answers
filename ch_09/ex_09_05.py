# Exercise 5: This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

fname = input("Enter a file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhand = open(fname)

domains = dict()

for line in fhand :
    if line.startswith("From ") :
        lines = line.rstrip()
        email = lines.split()[1]
        print("printing email")
        print(email)
        domain = email.split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)