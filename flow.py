def game():
        health = 20
        reputation = 50 

        print("Welcome Warrior")
        name = input("What is your name?")
        print(name + ", you have been chosen by your Earl to join the raid of a neighboring territory.")

        # the beginning
        
        weapon_choice = int(input("Please choose your weapon: \n 1. Axe \n 2. Sword \n 3. Longbow "))
        if weapon_choice == 1:
            print("Good choice Warrior " + name + ". Because you chose the axe, your earl has positioned you in the forward assault.")
        elif weapon_choice == 2:
            print("Good choice Warrior " + name + ". Because you chose the sword, your earl has positioned you in the second wave.")
        elif weapon_choice == 3:
            print("Good choice Warrior " + name + ". Because you chose the longbow, your earl has positioned you on the hilltop.")

        # Choice one - great hall/drunken warrior
        print("You are called to the Great Hall for a feast")

        print("A drunken warrior approaches you with another horn of ale just as you are ready to retire.")
        party_choice = int(input("Do you: \n 1. Decline and retire to your lodging. \n 2. Take him up on his offer. "))
        if party_choice == 1:
            print("You decline the warrior's offer and stumble home.")
            reputation = reputation - 10
            print("Your reputation among your fellow warriors to decrease.")
            print("Your reputation is now, ", reputation)
        elif party_choice == 2:
            print("Skol!")
            reputation = reputation + 10
            print("Your reputation among your fellow warriors to increase.")
            print("Your reputation is now, " , reputation)

        input("Press enter to continue")
        print("       ~~ Day of Raid ~~   ")

        if party_choice == 1:
            print("You awake the next morning refreshed and ready for battle.")
            
        elif party_choice == 2:
            print("You are startled awake by your friend, who angrily tosses you your armour.")
            health = health - 5
            reputation = reputation - 5

        print("You don your armour, take up your weapon and shield.")
        print("You meet the party at the edge of town, ready for battle.")
        input("Press enter to continue")

        print("The raiding party reaches their destination as the sun is at its highest peak.") 

        # the raid

        if weapon_choice == 1:  # axe
            print("The tension of anticipation builds with the clank of weapons against metal. You twist your axe in your hand, awaiting the battle horn")    
        elif weapon_choice == 2:  # sword
           print("The tension of anticipation builds with the clank of weapons against metal. You unsheath your sword as you step quietly through trees, awaiting the battle horn.")
        elif weapon_choice == 3:  # longbow
           print("The tension of anticipation builds with the clank of weapons against metal echoing through the valley. You nock an arrow, awaiting the battle horn")

        print("The battle horn sounds, the voices of war erupting in unison as the party pushes onwards.")
        print("Your current health is:", health)
        print("Your current reputaiton is:", reputation)

        if weapon_choice == 1:       # axe
            print("You charge into the village with your fellow warriors, taking no prisoners. \n Then you come upon a wounded enemy; they weakly swing their weapon in an attempt to fight.")
            battle_choice1 = int(input("Do you: \n 1. Laugh and continue on your way. \n 2. Take pity and end his life."))
            if battle_choice1 == 1:
                reputation = reputation + 2
                print("Your current health is:", health)
                print("Your current reputaiton is:", reputation)
                print("You continue past them, heading towards the Great Hall. You are intercepted by an enemy.")
                print("One raises his weapon to slash you across the torso.")

                battle_choice2 = int(input("What do you do?: \n 1. Move away \n 2. Attempt to counter his attack"))
                if battle_choice2 == 1:
                    print("The edge of his blade grazes your side. But another enemy comes from behind and slashes you across the back. [You lose 7 health]")
                    health = health - 7
                    print(health)
                    battle_choice3 = int(input("You are now bleeding. What do you do? \n 1. Kill them both. \n 2. Kill one and hope for aid. \n 3. Run"))
                    if battle_choice3 == 1:
                        print("You swing your axe in one swift motion, ending the first man's life. You turn your attention to the other and land the final blow just as the horn of battle sounds.")
                        print("The raid has ended. You have survived. Good work Viking.")
                    elif battle_choice3 == 2:
                        print("You make quick work of the first enemy. Just as you turn to deal with the second man, he attacks stabbing you in the stomach.")

                        print("You hear the horn of battle sound as you drop to your knees.")
                        health -= health
                        reputation += 15
                        print("Your current health is:", health)
                        print("Your current reputaiton is:", reputation)
                        print("You fought well Viking. May the Valkyries carry you home to Valhalla.")
                    
                    elif battle_choice3 == 3:
                        print("You ran away. You have been labeled a traitor and a coward.")
            elif battle_choice1 == 2:
                print("You take his life in one swift motion. Wishing him well on his way to Valhalla.")
                reputation += 5
                print("Your current health is:", health)
                print("Your current reputaiton is:", reputation)
                print("You continue onward towards the great hall. You see a few of your fellow warriors working to take down an enemy.")
                battle_choice4 = int(input("What do you do?: \n 1. Join them in the fight. \n 2. Decide they can handle it and go off in search of gold."))
                if battle_choice4 == 1:
                    print("You join your fellow warriors in battle against the enemy.")
                    print("Together you charge at him, drawing blood with each swing.")
                    print("The enemy makes contact, slashing you across the chest with is axe.")
                    health -= health
                    print("You fall to your knees as the horn of battle sounds.")
                    print("You fought well Viking. May the Valkyries carry you home to Valhalla.")
                elif battle_choice4 == 2:
                    print("You know your fellow warriors well and turn your attention to the spoils of the village.")
                    print("You enter an empty home. You rummage through the rooms.")
                    print("You have found gold. You pocket it as the horn of battle sounds.")
                    print("The raid has ended. You have survived. Good work Viking.")

        elif weapon_choice == 2:
            # sword
            print("You continue quietly through the woods surrounding the village. You come upon a house.")
            print("You are behind it. In the distance you hear the cries of the other villagers intermixed with the sounds of victory.")
            print("You enter the home in search of treasure and find a villager hiding in the corner.")
            battle_choice5 = int(input("Do you: \n 1. Let him live, but take his gold.  \n 2. Kill him and take his gold."))
            if battle_choice5 == 1:
                print("You place a finger to your lips to tell the villager to stay silent as you rummage throug his home, pocketing any treaure you find.")
                reputation -= 8
                print("Your current reputaiton is:", reputation)
                print("The horn of battle sounds throughout the village as the battle ends.")
                print("The raid has ended. You have survived. Good work Viking.")
            elif battle_choice5 == 2:
                print("You make quick work of him and go around the home pocketing any treasure you find.")
                reputation +=8
                print("You step out of the home. However, you have let your guard down.")
                print("An enemy runs his sword through you. You collapse to the ground as the horn of battle sounds.")
                health -= health
                print("Your current health is:", health)
                print("Your current reputaiton is:", reputation)
                print("Your greed has caused your death.")


        elif weapon_choice == 3: 
            # longbow
            print("You draw your arrow back, awaiting the command from your leader.")
            print("The battle rages on below. You see the mass of bodies, hear the clang of metal against metal.")
            print("You are command to shot your arrow. But you have no clear shot and cannot kill an enemy without sacrificing one of your friends.")
            battle_choice_6 = int(input("What do you do? \n 1. Take the shot \n 2. Wait for a clearer shot."))
            if battle_choice_6 == 1:
                print("You take the shot. Praying to Odin to send the Valkyries to guide your friend to Valhalla.")
                reputation += 8
                print("Your current health is:", health)
                print("Your current reputaiton is:", reputation)
                print("The horn of batttle echoes through the valley as the battle ends.")
                print("The raid has ended. You have survived. Good work Viking.")
            elif battle_choice_6 == 2:
                print("You refuse, lowering your bow.")
                print("Your commander is furious.")
                reputation -= 8 
                print("Your current repuation is: ", reputation)
                print("The horn of batttle echoes through the valley as the battle ends.")
                print("Despite your greivous error, your commander has let you live.")
                print("You live to fight another day, Viking.")



        # play again
        play_again = input("Would you like to play again? [yes/no]")
        if play_again == "yes" or "y":
            game()
        else:
            exit()

if __name__ == "__main__":
    game()

