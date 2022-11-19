import time, sys

backpack = {}
tower = {}

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0)

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.0)
  value = input()  
  return value 

#Adventure Game
def welcome():
    print("""..••°°°°••....••°°°°••...••°°°°••....••°°°°••...ELROND'S TOWER..••°°°°••....••°°°°••....••°°°°••....••°°°°••..
                            Welcome to Elrond's Tower! A text-based adventure game.
 
            There are different options you can choose from. These choices will affect your gameplay.
                    Experience a fantasy world through your imagination! Be a hero.

..••°°°°••....••°°°°••...••°°°°••....••°°°°••....••°°°°••....••°°°°••....••°°°°••....••°°°°••....••°°°°••..
    """)
    while True:
        startGame = input("Are your ready to start your game? Type Y if yes or N if no: ")
        if startGame.upper() == "Y":
            intro()
            break

        elif startGame.upper() == "N":
            print("Come by some other time!")
            break

        else:
            print("Input not recognized.")
            continue

#Player Customization
def intro():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    typingPrint("""

        It was dark....
        You hear faint voices in the distance.

        \033[1m MUMBLE MUMBLE \033[0;0m

        As you slowly opened your eyes, you see different kinds of people in medieval clothing.
        You hear footsteps behind you.

        \033[1m PAT PAT \033[0;0m

        You looked behind you and saw three old men.

        Old Man #1: "Greetings adventurer! We are the wise men, protectors of this realm." 
        Old Man #2: "We summoned you in this world to become our hero who will defeat the evil Lord Elrond."
        Old Man #3: "What is your name adventurer?"
    """)
    playerName = typingInput("You: ")
    typingPrint(f"""
        Old Man #3: What a fit name for a hero, {playerName}!
        Old Man #1: Pick your magical weapon that will aid you in your battle.

                 \033[1mSWORD         WAND        BOW\033[0;0m

    """)
    playerWeapon = typingInput("You: I'll pick the ")
    
    while True:
        if playerWeapon.upper() == "SWORD":
            typingPrint("\n\033[1;32m SWORD ACQUIRED \033[0;0m\n")
            typingPrint(f"""
        Old Man #2: Wonderful choice! You are now a swordsman.
        Old Man #1: The evil Lord Elron is on the top of his Spike Tower.
        Old Man #3: We will now teleport you into the first floor of the tower.
        Old Men in Unison: Good luck {playerName} the Adventurer!

    """)
            backpack.update({"Weapon" : "Sword"})
            towerEntrance()
            break

        elif playerWeapon.upper() == "WAND":
            typingPrint("\n\033[1;32m WAND ACQUIRED \033[0;0m\n")
            typingPrint(f"""
        Old Man #2: Wonderful choice! You are now a mage.
        Old Man #1: The evil Lord Elron is on the top of his Spike Tower.
        Old Man #3: We will now teleport you into the first floor of the tower.
        Old Men in Unison: Good luck {playerName} the Adventurer!

    """)
            backpack.update({"Weapon" : "Wand"})
            towerEntrance()
            break

        elif playerWeapon.upper() == "BOW":
            typingPrint("\n\033[1;32m BOW ACQUIRED \033[0;0m\n")
            typingPrint(f"""
        Old Man #2: Wonderful choice! You are now an archer.
        Old Man #1: The evil Lord Elron is on the top of his Spike Tower.
        Old Man #3: We will now teleport you into the first floor of the tower.
        Old Men in Unison: Good luck {playerName} the Adventurer!

    """)
            backpack.update({"Weapon" : "Bow"})
            towerEntrance()
            break
        else:
            print("Input not recognized.")
            continue

def towerEntrance():
    tower.update({"Tower" : "Entrance"})
    typingPrint("\n\033[1;32m Player customization is now finished. \033[0;0m\n")
    typingPrint("\033[1;32m Teleported into Spike Tower's Entrance. \033[0;0m\n")
    typingPrint("\033[1;32m Type B to check backpack. Type L for location. \033[0;0m")
    typingPrint("""
        
        As you were summoned in the tower, you see three passages:
        On the left is a large door.
        On the middle is a hallway.
        On the right is a staircase

        Where do you want to go?

                 \033[1mLEFT         MIDDLE        RIGHT\033[0;0m

    """)

    while True:
        playerChoice = typingInput("\nYou: ")
        if playerChoice.upper() == "B":
            typingPrint("\nYour backpack contains: \n")
            typingPrint (backpack["Weapon"])
            continue
        elif playerChoice.upper() == "L":
            typingPrint("\nYour location is: \n")
            typingPrint(tower["Tower"])
            continue
        elif playerChoice.upper() == "LEFT":
            typingPrint("""
        
        You entered the big door.
        There is a skeleton holding a sword.
        IT'S COMING TOWARDS YOU!

        What do you want to do?

                 \033[1mFIGHT        FLEE\033[0;0m

    """)
            while True:
                playerSkeleton = typingInput("You: I will ")
                if playerSkeleton.upper() == "FIGHT":
                    typingPrint("\n\033[1;32mYou defeated the skeleton!\033[0;0m")
                    typingPrint("""
        
        You searched the room and saw an iron armor.
\033[1;32m IRON ARMOR ACQUIRED \033[0;0m
        You went outside the room and proceeded to the top tower.

    """)
                    backpack.update({"Armor" : "Iron Armor"})
                    topTower()
                    break
                

                elif playerSkeleton.upper() == "FLEE":
                    typingPrint("\n\033[0;31mThe skeleton caught you.\033[0;0m\n")
                    typingPrint("\033[0;31mYou lost. Try again!\033[0;0m\n")
                    continue

                else:
                    print("Input not recognized.")
                    continue


            break




        elif playerChoice.upper() == "MIDDLE":
            typingPrint("""
        
        You entered the hallway.
        There is a bandit holding a knife.
        IT'S COMING TOWARDS YOU!

        What do you want to do?

                 \033[1mFIGHT        FLEE\033[0;0m

    """)
            while True:
                playerSkeleton = typingInput("You: I will ")
                if playerSkeleton.upper() == "FIGHT":
                    typingPrint("\n\033[1;32mYou defeated the bandit!\033[0;0m")
                    typingPrint("""
        
        You searched the hallway and saw a leather armor.
\033[1;32m LEATHER ARMOR ACQUIRED \033[0;0m
        You went outside the hallway and proceeded to the top tower.

    """)
                    backpack.update({"Armor" : "Leather Armor"})
                    topTower()
                    break
                

                elif playerSkeleton.upper() == "FLEE":
                    typingPrint("\n\033[0;31mThe bandit caught you.\033[0;0m\n")
                    typingPrint("\033[0;31mYou lost. Try again!\033[0;0m\n")
                    continue

                else:
                    print("Input not recognized.")
                    continue

            break


        elif playerChoice.upper() == "RIGHT":
            topTower()
            break

        else:
            print("Input not recognized.")
            continue


def topTower():
    tower.update({"Tower" : "Elrond's Throne"})
    typingPrint("""
        
        \033[0;37mELROND'S FLOOR\033[0;0m

        You saw Elrond sitting on his throne.
        He's using a flaming sword.
        He's slowly approaching you,
        What do you do?


                 \033[1mFIGHT         BARGAIN        FLEE\033[0;0m

    """)

    while True:
        playerChoice = typingInput("\nYou: ")
        if playerChoice.upper() == "B":
            typingPrint("\nYour backpack contains: \n")
            typingPrint (backpack["Weapon"])
            continue
        elif playerChoice.upper() == "L":
            typingPrint("\nYour location is: \n")
            typingPrint(tower["Tower"])
            continue
        elif playerChoice.upper() == "FIGHT":
            typingPrint("""
        
        You attacked him once but he's still standing
        He stricked back.
    """)

            if "Iron Armor" in backpack.values():
                finalAttack = typingInput("""

        His sword didn't do anything
        What will you do you now?


                 \033[1mFIGHT        FLEE\033[0;0m

    """)
                while True:
                    if finalAttack.upper == ("FIGHT"):
                        ("You defeated him!")
                    break

            elif "Leather Armor" in backpack.values():
                typingPrint("      His flaming sword burned your armor")

            else:
                typingPrint("You have no Armor.")

            break


welcome()


    
#Swordsman Option
#Mage Option
#Archer Option





