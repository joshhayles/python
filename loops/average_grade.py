
# using for loop:
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade 

print(total / amount) # => 80.0

# not using a for loop:
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount) # => 80.0