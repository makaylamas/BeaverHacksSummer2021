def axe(health, reputation):
    # battle choices for weapon 1: axe
    print("You charge into the village with your fellow warriors, taking no prisoners. \n Then you come upon a wounded enemy; they weakly swing their weapon in an attempt to fight.")
    battle_choice1 = ("Do you: \n 1. Laugh and continue on your way. \n 2. Take pity and end his life.")
    if battle_choice1 == 1:
        reputation = reputation + 2
        print(reputation)
        print(health)
        print("You continue past them, heading towards the Great Hall. You are intercepted by an enemy.")
        print("One raises his weapon to slash you across the torso.")
        battle_choice2 = input("What do you do?: \n 1. Move away \n 2. Attempt to counter his attack")
        if battle_choice2 == 1:
            print("The edge of his blade grazes your side. But another enemy comes from behind and slashes you across the back. [You lose 7 health]")
            health = health - 7
            print(health)
            battle_choice3 = input("You are now bleeding. What do you do? \n 1. Kill them both. \n 2. Kill one and hope for aid. \n 3. Run")
            if battle_choice3 == 1:
                print("You swing your axe in one swift motion, ending the first man's life. You turn your attention to the other and land the final blow just as the horn of battle sounds.")
                print("The raid has ended. You have survived. Good work Viking.")
            elif battle_choice3 == 2:
                print("You make quick work of the first enemy. Just as you turn to deal with the second man, he attacks stabbing you in the stomach.")

                print("You hear the horn of battle sound as you drop to your knees.")
                health = health - health
                print(health)
                print("You fought well Viking. May the Valkyries carry you home to Valhalla.")
            else:
                print("You ran away. You have been labeled a traitor and a coward.")
    else:
        print("You ")

def sword(health, reputation):
    # battle choices for weapon 2: sword
    health = health
    reputation = reputation
   pass

def longbow(health, reputation):
    health = health
    reputation = reputation
    
    # battle choices for weapon 3: longbow
    pass


def game():
        health = 20
        reputation = 
        position = None

        print("Welcome Warrior")
        name = input("What is your name?")
        print(name + ", you have been chosen by your Earl to join the raid of a neighboring territory.")

        # the beginning
        
        weapon_choice = input("Please choose your weapon: \n 1. Axe \n 2. Sword \n 3. Longbow ")
        if weapon_choice == 1:
            position = "Forward Assault"
            print("Good choice Warrior" + name + ". Because you chose the sword, your earl has positioned you in " + position + ".")
        elif weapon_choice == 2:
            position = "Second Wave"
            print("Good choice Warrior" + name + ". Because you chose the sword, your earl has positioned you in " + position + ".")
        else:
            position = "Hilltop"
            print("Good choice Warrior" + name + ". Because you chose the sword, your earl has positioned you in " + position + ".")


        input("Press enter to continue")

        # Choice one - great hall/drunken warrior
        print("You are called to the Great Hall for a feast")

        print("A drunken warrior approaches you with another horn of ale just as you are ready to retire.")
        party_choice = input("Do you: \n 1. Decline and retire to your lodging. \n 2. Take him up on his offer. ")
        if party_choice == 1:
            print("You decline the warrior's offer and stumble home.")
            reputation = reputation - 10
            print("Your reputation among your fellow warriors to decrease.")
            print("Your reputation is now, ", reputation)
        else:
            print("Skol!")
            reputation = reputation + 10
            print("Your reputation among your fellow warriors to increase.")
            print("Your reputation is now, " , reputation)

        input("Press enter to continue")
        print("       ~~ Day of Raid ~~   ")

        if party_choice == 2:
            print("You awake the next morning refreshed and ready for battle.")
            print(health)
            print(reputation)
        else:
            print("You are startled awake by your friend, who angrily tosses you your armour.")
            health = health - 5
            print(health)
            reputation = reputation - 5
            print(reputation)

        print("You don your armour, take up your weapon and shield.")
        print("You meet the party at the edge of town, ready for battle.")
        input("Press enter to continue")

        print("The raiding party reaches their destination as the sun is at its highest peak.") 

        # the raid

        if weapon_choice == 1:
            print("The tension of anticipation builds with the clank of weapons against metal. You twist your axe in your hand, awaiting the battle horn")    
        elif weapon_choice == 2:
           print("The tension of anticipation builds with the clank of weapons against metal. You unsheath your sword as you step quietly through trees, awaiting the battle horn.")
        else:
           print("The tension of anticipation builds with the clank of weapons against metal echoing through the valley. You nock an arrow, awaiting the battle horn")

        print("The battle horn sounds, the voices of war erupting in unison as the party pushes onwards.")
         

        if weapon_choice == 1:
            axe(health, reputation)
        elif weapon_choice == 2:
            sword(health, reputation)
        else:
            longbow(health, reputation)


        # play again
        play_again = input("Would you like to play again? [yes/no]")
        if play_again == "yes" or "y":
            game()
        else:
            exit()

if __name__ == "__main__":
    game()

