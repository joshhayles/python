
# return the keys in dictionary:
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(student) # => Rolf Bob Anne (keys are returned)


# cleaner way to access items:
my_student_attendance = {"Rolfy": 96, "Bobby": 80, "Anny": 100}

# creating two variables and using items():
for student, attendance in my_student_attendance.items():
    print(f"{student}: {attendance}") # => Rolfy: 96 Bobby: 80 Anny: 100