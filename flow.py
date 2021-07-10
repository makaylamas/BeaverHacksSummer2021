print("Welcome Warrior")
name = input("What is your name?")
print(name + ", you have been chosen by your Earl to raid a neighboring territory.")


health = 100
reputation = 50

weapon_choice = input("Please choose your weapon: \n 1. Axe \n 2. Sword \n 3. Longbow")
if weapon_choice == 1:
    position = "Forward Assault"
elif weapon_choice == 2:
    position == "Second Wave"
else:
    position = "Hilltop"

input("Press enter to continue")

print("You are called to the Great Hall for a feast")

input("Press enter to continue")

print("A drunken warrior approaches you with another horn of ale just as you are ready to retire.")
choice = input("Do you: \n 1. Decline and retire to your lodging. \n 2. Take him up on his offer.")
if choice = 1:
    print("You decline the warrior's offer and stumble home.")
    reputation - 10
    print("Your choice has cause your reputation among your fellow warriors to decrease.")
    print(reputation)
elif choice = 2:
    print("Skol!")
    reputation + 10
    print(reputation)
    print("Your choice has caused your reputation among your fellow warriors to increase.")

input("Press enter to continue")
print("       ~~ Day of Raid ~~   ")
