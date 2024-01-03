print("The Love Calculator is calculating your score...")
# Ask for the user's name
name1 = input("What is your name?\n")

# Ask for their partner's name
name2 = input("What is your partner's name?\n")

# Combine the name of the user and their partner
combined_names = name1 + name2
lower_case = combined_names.lower()

# Count the occurrence of both names in the string 'TRUE'
t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
count_name1 = t + r + u + e

# Count the occurrence of both names in the string 'LOVE
l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
count_name2 = l + o + v + e


# Calculate the love score by concatenating the count of each name
love_score = int(str(count_name1) + str(count_name2))

# Create a conditional criteria based on the love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you slightly compatible.")
else:
    print(f"Your score is {love_score}, you are alright together.")