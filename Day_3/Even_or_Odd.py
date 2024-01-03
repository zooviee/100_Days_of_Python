# The program tells the user if a given number is an odd or even number

# Which number do you want to check
number = int(input("Enter your desired number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"This is an even number.")
else:
    print(f"This is an odd number.")