import random

print("Roll the dice against the computer")

roll = input("Press R to roll the die: ").upper()

if (roll == "R"):
    yourRoll = random.randint(1,6)
    print("\n" + "Your roll is " + str(yourRoll))
    computerRoll = random.randint(1,6)
    print("\n" + "Computer's roll is " + str(computerRoll))

if (computerRoll == yourRoll):
    print("\n" + "Tie")
elif (computerRoll > yourRoll):
    print("\n" + "Computer Wins")
elif (computerRoll< yourRoll):
    print("\n" + "You Win")
else:
    print("\n" + "You should not see this")
