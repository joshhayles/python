
# this tells Python you want a list with a tuple inside of it:
x = [(5, 12)]

print(x)

# short-hand for defining two variables at the same time:
x, y = 5, 12

print(x, y) # => 5, 12

# you can assign the two variables to another tuple:
t = 3, 18
x, y = 3, 18

print(t) # => (3, 18)

# print a formatted response from nested tuples using destructuring:
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Teacher")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Name: Bob, Age: 42, Profession: Mechanic
# Name: James, Age: 24, Profession: Artist
# Name: Harry, Age: 32, Profession: Teacher

# use an underscore in place of the variable you want to ignore in order to avoid errors:
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession) # => Bob Mechanic