#Name: Sebastian Murga
#period: PM
#Student Performance Analyzer

#Program introduction
print("===================================")
print("  STUDENT PERFFORMANCE ANALYZER.   ")
print("===================================")

#Student Information
student_name = input("What is your name?")
student_grade_level = int(input("What grade are you in?"))
student_assignment_average = float(input("what is your assignment average"))
student_quiz_average = float(input("What is your quiz average"))
test_avg = float(input("What is your test average?"))
attendance_percent = float(input("What isnyou attendance percent?"))
missing_count = int(input("what is your missing assignment count?"))

#calculate students grade
def calculate_grade(student_assignment_average, student_quiz_average, test_avg):
    overall_grade = (student_assignment_average * 0.30) + (student_quiz_average * 0.30) + (test_avg * 0.40)
    print("overall grade:", round(overall_grade, 2))
    return overall_grade

#determine letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        print("Letter Grade: A")
    elif overall_grade >= 80:
        print("Letter Grade: B")
    elif overall_grade >= 70:
        print("Letter Grade: C")
    elif overall_grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")

#determine attendence
def attendance_status(attendance_percent):
    if attendance_percent >= 95:
        print("Attendance status: Excellent attendance")
    if attendance_percent >= 90:
        print("Attendance status: Good attendance")
    if attendance_percent >= 80:
        print("Attendance status: Needs work")
    else:
        print("Attendance status: Poor attendance")

#check missing assignments
def assignment_status(missing_count):
    if missing_count == 0:
        print("missing assignnment status: Excellent")
    elif missing_count <= 2:
        print("missing assignnment status: Good")
    elif missing_count <= 4:
        print("missing assignnment status: Warning")
    else:
        print("missing assignnment status: Critical")

#eligibility check nested mode
def check_eligibility(overall_grade, attendance_percent, missing_count):
    if overall_grade >= 70:
        if attendance_percent >= 90:
            if missing_count <= 2:
                print("Academic Eligibility: Eligible")
                print("Student passed all three requirements.")   
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Elibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low")
    else:
        print("Academic Elgibility: NOT ELIGIBLE")
        print("Reason: overall grade is too low")

# high honors check nested mode
def check_high_honors(overall_grade, attendance_percent, missing_assignments):
    if overall_grade >= 90:
        if attendance_percent >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

# good standing check
def check_good_standing(overall_grade, attendance_percent):
    if overall_grade >= 70 and attendance_percent >= 90:
        print("Good standing: YES")
    else:
        print("Good standing: NO")

#Support check
def check_support(overall_grade, attendance_percent):
    if overall_grade < 70 or attendance_percent < 80:
        print("Additional support: RECOMMENDED")
    else:
        print("Additional support: NOT NEEDED")

#Messages based on grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your first year Freshman!!")
    elif grade_level == 10:
        print("One year down, 3 more to go!!!")
    elif grade_level == 11:
        print("3 out of 4?, you can do this!!!")
    elif grade_level == 12:
        print("Home Stretch, YOU CAN DO THIS!!!")
    else:
        print("Invalid grade level.")

# finds highest score
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average and assignment_average >= test_average:
        print("Strongest Category: Assignments")
    elif quiz_average >= assignment_average and quiz_average >= test_average:
        print("Strongest Category: Quizzes")
    else:
        print("Strongest Category: Tests")

# printing  student summary
print()
print("========================================")
print("            STUDENT SUMMARY")
print("========================================")
print()
print("Student name: ", student_name)
print("Grade Level: ", student_grade_level)
grade_level_message(student_grade_level)
print()
print("Assignment Average:", student_assignment_average)
print("Quiz Average:", student_quiz_average)
print("Test average:", test_avg)
print("Attendance:", attendance_percent)
print("Missing assignments", missing_count)
print()