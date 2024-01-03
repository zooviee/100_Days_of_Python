# The program checks if the year is a leap year or not
print("Welcome to the leap year checker.")
# Which year do you want to check?
year = int(input("Enter year: "))

# Checking if the year is a leap year or not
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
    print("Not leap year")