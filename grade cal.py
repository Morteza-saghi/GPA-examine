# # to examine the grade
# def gradeReviewTeller(grade):
#     if grade >= 17:
#         print("Great")
#     elif 12 < grade < 17:
#         print("Normal")
#     elif 12 > grade:
#         print("Fail")


def GPA(A):
    grades = list()
    isfinished = False
    while isfinished == False:
        theinpute = int(
            input("please enter the grade\n"))
        grades.append(theinpute)
        print(grades)


GPA("A")
