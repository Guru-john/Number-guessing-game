import random
import math

lower = int(input("enter lower bound : "))
upper = int(input("enter upper bound : "))

x = random.randint(lower, upper)

print(f"you have only {round(math.log(upper - lower + 1, 2))} chances to guess the integer")

count = 0
while count < math.log(upper - lower +1, 2):
    count += 1
    guess = int(input(" guess a number :"))
    if x == guess:
        print("congrates you did it in", count, "try")
        break
    elif x < guess:
        print(" you have guessed too high")
    elif x > guess:
        print("you have guessed too low")
if count >= math.log(upper - lower + 1, 2):
    print("the number is", x)
    print("better luck next time")

