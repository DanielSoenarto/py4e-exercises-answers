# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.

# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F

def computegrade(score) :
    if score > 0.9:
        return "A"
    elif score > 0.8 :
        return "B"
    elif score > 0.7 :
        return "C"
    elif score > 0.6 :
        return "D"
    elif score <= 0.6 :
        return "F"
try :
    score = float(input("Enter a score between 0.0 - 1.0: "))
    
    if score < 0.0 or score > 1.0 :
        raise
except :
    print("Bad score")
    quit()

grade = computegrade(score)
print(f"the grade is {grade}")

