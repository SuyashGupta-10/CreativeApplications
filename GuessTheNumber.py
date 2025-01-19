import random

logo = '''   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       '''

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guesses = 0

if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    guesses += 10
elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    guesses += 5
def guess():
    global guesses
    while guesses > 0:
        guessed_number = int(input("Make a guess: "))
        if guessed_number > number:
            guesses -= 1
            print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number.")
            guess()
        elif guessed_number < number:
            guesses -= 1
            print(f"Too low.\nGuess again.\nYou have {guesses} attempts remaining to guess the number.")
            guess()
        else:
            print(f"You got it! The answer was {number}")
            guesses = -1
            input()
    
    if guesses == 0:
        print(f"You've run out of guesses. You lose. The number was {number}")
        input()

guess()


    
