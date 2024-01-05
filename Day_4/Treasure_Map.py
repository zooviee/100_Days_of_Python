# This program marks a spot on a map with an X where a user can hide their treasure.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
mapping = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

# Prompt the user to enter a letter-number combination
position = input("Where do you want to put the treasure? e.g. A1, B2, C3 \n")

letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

mapping[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")