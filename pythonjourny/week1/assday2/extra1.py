weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")

weight = float(weight)
height = float(height)

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
else:
    print("Overweight")