import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
number = random.randint(0,2)
comp_choice = list[number]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("Try Again. You typed an invalid number.")
    

print("Computer chose:")
print(comp_choice)

if user_choice == "0" and comp_choice == rock:
        print("It's a draw.")
elif user_choice == "0" and comp_choice == paper:
        print("You lose.")
elif user_choice == "0" and comp_choice == scissors:
        print("You Win!")

elif user_choice == "1" and comp_choice == rock:
        print("You Win!")
elif user_choice == "1" and comp_choice == paper:
        print("It's a draw.")
elif user_choice == "1" and comp_choice == scissors:
        print("You lose.")

elif user_choice == "2" and comp_choice == rock:
        print("You lose.")
elif user_choice == "2" and comp_choice == paper:
        print("You Win!")
elif user_choice == "2" and comp_choice == scissors:
        print("It's a draw.")
else:
    input()

    input()