# Prompt the user to enter a number between 0 and 100

target = int(input("Enter a number between 0 and 100:\n"))

total = 0
for num in range(1, (target + 1)):
    if num % 2 == 0:
        total += num
print(f"The sum of even numbers in {target} is = {total}.")