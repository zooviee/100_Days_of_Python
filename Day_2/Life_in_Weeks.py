# The code below calculates a user's life span in weeks if they live for up to 90 years.
# It will take your current age as the input and output a message with our time left

# Prompt the user for their age
age = int(input("Enter your age: "))
years = 90 - age

# Convert the years to weeks
life_in_weeks = years * 52

# Display the time left in weeks
print(f"You have {life_in_weeks} weeks left." )