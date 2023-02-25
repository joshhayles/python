# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)

# Ex: height: 1.70 > weight: 76kg => 26 bmi