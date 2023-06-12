# to examine the grade
def gradeReviewTeller(grade):
    if grade >= 17:
        print("Great")
    elif 12 < grade < 17:
        print("Normal")
    elif 12 > grade:
        print("Fail")


sumOfGrades = 0
howmanygrades = int(input("how many grades do you want to enter"))
for i in range(howmanygrades):
    a = int(input("plz enter your grade "))
    sumOfGrades += a

gradeReviewTeller(sumOfGrades / howmanygrades)
