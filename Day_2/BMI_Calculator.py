# Prompt the user to enter their height data
height = float(input("Enter your height (m): "))
weight = int(input("Enter your weight (kg): "))

# Calculate the body to mass index of the user
bmi = weight / height ** 2

# Convert the bmi to integer type data
bmi = int(bmi)

# Display the bmi data
print(f"Your body mass index is: {bmi} kg/m².")