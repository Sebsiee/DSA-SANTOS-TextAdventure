import time, sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  value = input()  
  return value 

#Adventure Game
def welcome():
    print("""..••°°°°••....••°°°°••...••°°°°••....••°°°°••...ELROND'S EMPIRE..••°°°°••....••°°°°••....••°°°°••....••°°°°••..
                            Welcome to Elrond's Empire! A text-based adventure game.
 
            There are different options you can choose from. These choices will affect your gameplay.
                    Experience a fantasy world through your imagination! Be an Elrond hero.

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
        You hear faint voices in the distance....

        \033[1m MUMBLE MUMBLE \033[0;0m

        As you slowly opened your eyes, you see different kinds of people in medieval clothing.

        \033[1m PAT PAT \033[0;0m, said the footsteps behind you

        It was from the three old men with long hair and beards.

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
            print("You are now a swordsman.")
            break
        elif playerWeapon.upper() == "WAND":
            print("You are now a mage.")
            break
        elif playerWeapon.upper() == "SWORD":
            print("You are now an archer.")
            break
        else:
            print("Input not recognized.")
            continue


welcome()

    
#Swordsman Option
#Mage Option
#Archer Option





