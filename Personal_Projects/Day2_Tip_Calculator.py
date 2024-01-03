# Display a welcome message
print("Welcome to the tip calculator!")

# Ask the user for the total bill
total_bill = float(input("What was the total bill?\n$"))

# Ask the user for the percentage tip they would like to give
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

# Ask the user for the number of people to split the bill
number_of_people = int(input("How many people to split the bill?\n"))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the new total bill
new_total_bill = total_bill + tip_amount

# Calculate the individual bill (the bill per person)
bill_per_person = new_total_bill / number_of_people

# Display the bill per person
print(f"Each person should pay: ${bill_per_person:.2f}")

# Conclusion
individual_bill = total_bill/number_of_people
individual_tip = tip_amount/number_of_people
print(f"Thus, everyone's share of the total bill is ${individual_bill:.2f} plus a ${individual_tip:.2f} tip.")

# Display a goodby message
print("Goodbye and Thank you!")