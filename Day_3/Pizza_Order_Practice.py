print("Thank you for choosing Zoovie Pizza Deliveries!")
# Ask the user to enter the desired pizza size
size = input("Enter pizza size: s for small, m for medium, l for large\n").lower()

# Ask the user if they want pepporoni
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()

# Ask the user if they want extra cheese
extra_cheese = input("Do you want extra cheese? Y or N\n").lower()

bill = 0

if size == 'S'.lower():
    bill = 15
elif size == 'M'.lower():
    bill = 20
else:
    bill = 25

if add_pepperoni == 'Y'.lower():
    if size == 'S'.lower():
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y'.lower():
    bill += 1

print(f"Your final bill is: ${bill}.")