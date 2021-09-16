####James Burns
####CS101L Assignment 2
####09-16-2021


print("**** Welcome to the LAB grade calculator! ****\n\n")

student_name = input("Who are we calculating grades for? ==>")  #get student name

lab_grade = float(input("\nEnter the LABS grade? ==>")) #get lab grade

#ensure grade is within bounds [0,100]
if lab_grade < 0:
    lab_grade = 0
    print("The lab value should have been zero or greater.  It has been changed to zero.")
if lab_grade > 100:
    lab_grade = 100
    print("The lab value should have been 100 or less.  It has been changed to 100.")

exam_grade =float(input("\nEnter the EXAMS grade? ==>"))    #get exam grade

#ensure grade is within bounds [0,100]
if exam_grade < 0:
    exam_grade = 0
    print("The exam value should have been zero or greater.  It has been changed to zero.")
if exam_grade > 100:
    exam_grade = 100
    print("The exam value should have been 100 or less.  It has been changed to 100.")

attendance_grade = float(input("\nEnter the ATTENDANCE grade? ==>"))    #get attendance grade

#ensure grade is within bounds[0,100]
if attendance_grade < 0:
    attendance_grade = 0
    print("The attendance value should have been zero or greater.  It has been changed to zero.")
if attendance_grade > 100:
    attendance_grade = 100
    print("The attendance value should have been 100 or less.  It has been changed to 100.")

total_grade = (0.7 * lab_grade) + (0.2 * exam_grade) + (0.1 * attendance_grade) #calculate total grade according to weight

#assign value range to letter grades
if 0 <= total_grade < 60:
    letter_grade = 'F'
if 60 <= total_grade < 70:
    letter_grade = 'D'
if 70 <= total_grade < 80:
    letter_grade = 'C'
if 80 <= total_grade < 90:
    letter_grade = 'B'
if 90 <= total_grade <= 100:
    letter_grade = 'A'
                         
print("\n\nThe weighted grade for" , student_name , "is" , total_grade) #print weighted grade as float value
print(student_name , "has a letter grade of" , letter_grade)    #print letter grade according to range

print("\n\n****Thanks for using the Lab grade calculator****")
