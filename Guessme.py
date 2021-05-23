import random

print("Hi Welcome to my game! Please type in your name")
name = input()
secretnumber = random.randint(1, 20)
print(
    "Hi !"
    + name
    + "..Let's play random number guessing game Pls make a guess from number in range 1-20"
)

for i in range(1, 4):
    print("Take a guess")
    guess = int((input()))
    if guess > secretnumber:
        print("Number too high")

    elif guess < secretnumber:

        print("Number too low")

    else:
        break
if guess == secretnumber:
    print("wholaa You won!")
else:
    print("Nope Sorry You lost try later! My number was" + str(secretnumber))
