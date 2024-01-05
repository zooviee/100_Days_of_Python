# The program will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
import random

# Prompt the user to enter the list of names e.g: david, daniel, jessica
names_string = input("Enter the names of your friends: ")
names = names_string.split(",")

# Get the total number of items in the list
num_items = len(names)

# Generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items - 1)

# Choose and print a random name
print(f"{names[random_choice]} is going to buy the meal today.")
