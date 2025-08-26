# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#
# empty_dictionary = {}
# empty_dictionary["Key"] = "Value"
#
# #Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
        print(student_grades)
