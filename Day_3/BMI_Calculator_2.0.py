# Prompt the user to enter their height data
height = float(input("Enter you height (m): \n"))

# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight (kg): \n"))

# Calculate the body mass index
bmi = weight / height ** 2
BMI = round(bmi, 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} kg/m², you are  underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI} kg/m², you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI} kg/m², you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI} kg/m², you are obese.")
else:
    print(f"You BMI is {BMI} kg/m², you are clinically obese.")