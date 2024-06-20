
# function to find average mark of student
def find_average_marks(marks):
    sum_of_marks= sum(marks)
    number_of_subject =len(marks)
    average_mark = sum_of_marks / number_of_subject
    return average_mark

# finding grade of student
def student_grade(average_mark):
    if average_mark >= 90:
        grade = "A"
    elif average_mark >= 80:
        grade = "B"
    elif average_mark >= 70:
        grade = "C"
    elif average_mark >= 60:
        grade = "D"
    elif average_mark >= 50:
        grade = "E"
    else:
        grade = "F"
    return grade

# printing student's grade from average
marks =[87,71,71,77,75,88,90,77,78,65]
average_mark = find_average_marks(marks)
print("Your average mark is", average_mark)

grade = average_mark
st_grade = student_grade(grade)
print("Your grade is:", st_grade)