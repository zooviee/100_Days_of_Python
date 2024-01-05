# import the random module
import random

random_side = random.randint(0, 1)
print(f"The computer generated {random_side} as the random number.")
if random_side == 1:
    print("Heads")
else:
    print("Tails")