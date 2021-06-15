# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) #needed int
exam_three = int(input("Input exam grade three: ")) #change str to int, change to three instead of 3
grades = [exam_one, exam_two,exam_three] #add comma
sum = 0
#grades2 = str(grades)
for grade in grades: #change second to grades
  sum = sum + grade
avg = sum/len(grades) #grades mispelled
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 69 and avg < 80:
    letter_grade = "C" #change type of quotation missing equals
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif avg <= 65: #define grade and remove :
    letter_grade = "F"
for grade in grades:   
    print("Exams: " + str(grades))
    print("Average: " + str(avg))
    print("Grade: " + letter_grade)
    break
if letter_grade == "F" : #change n dash to underscore, remove is
    print ("Student is failing.") #add parenthesis
else:
    print ("Student is passing.") #add parenthesis
