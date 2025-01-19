print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

dir_1 = str(input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')).lower()
if dir_1 == "left":
          dir_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
          if dir_2 == "wait":
                    dir_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
                    if dir_3 == "red":
                              print("It is a room full of fire. Game Over.")
                    elif dir_3 == "yellow":
                              prompt = input("You found the treasure! Type 'yes' to claim it or 'no' to leave it.\n").lower()
                              if prompt == "yes":
                                        answer = input("You've found $1,000,000! Do you wish to claim it?\n").lower()
                                        if answer == "yes":
                                                  print("YOU WIN!")
                                        else:
                                                  print("You have lost your senses after this gruesome adventure. Go Home. Game Over")
                              elif prompt == "no":
                                        print("You are a coward. Game Over.")
                              else:
                                        print("You have lost your senses after this gruesome adventure. Go Home. Game over.")
                                        
                    elif dir_3 == "blue":
                              print("You enter a room full of beasts. Game Over.")
                    else:
                              print("You chose a door that doesn't exist. You have lost your senses after this gruesome adventure. Go Home. Game over.")
          elif dir_2 == "swim":
                    print("You get attacked by an angry piranha. Game Over.")
          else:          
                    print("You have lost your senses after this gruesome adventure. Go Home. Game over.")
elif dir_1 == "right":
          print("You got caught in a bear trap. Game over.")
else:
          print("It seems you chose the direction to the mental asylum. Game Over.")
hack = input()