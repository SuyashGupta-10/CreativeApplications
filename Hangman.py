import random

word_list = [
    "apple", "banana", "grape", "orange", "lemon", "peach", "berry", "melon", "kiwi", "mango",
    "chair", "table", "sofa", "bed", "desk", "lamp", "rug", "couch", "stool", "shelf",
    "water", "juice", "soda", "coffee", "tea", "milk", "beer", "wine", "bread", "butter",
    "shirt", "pants", "shoes", "socks", "coat", "hat", "glove", "scarf", "belt", "tie",
    "dog", "cat", "fish", "bird", "horse", "rat", "wolf", "deer", "duck", "frog",
    "train", "plane", "car", "bike", "boat", "bus", "truck", "ship", "subway", "van",
    "sun", "moon", "star", "sky", "cloud", "rain", "wind", "storm", "snow", "fog",
    "pen", "book", "notebook", "pencil", "marker", "eraser", "ruler", "tape", "glue", "scissors",
    "house", "apartment", "cabin", "mansion", "hut", "villa", "shack", "palace", "tower", "tent",
    "phone", "radio", "tv", "computer", "tablet", "camera", "mouse", "keyboard", "speaker", "printer",
    "apple", "peach", "plum", "date", "fig", "nut", "bean", "corn", "wheat", "barley",
    "pasta", "pizza", "soup", "steak", "chicken", "salad", "sandwich", "taco", "burger", "sushi",
    "moon", "sun", "star", "space", "comet", "galaxy", "planet", "asteroid", "rocket", "alien",
    "forest", "desert", "beach", "mountain", "valley", "river", "lake", "pond", "field", "hill",
    "cake", "cookie", "pie", "muffin", "donut", "croissant", "brownie", "cheesecake", "pancake", "waffle",
    "basket", "box", "bag", "can", "bottle", "jar", "cup", "plate", "spoon", "fork",
    "bath", "shower", "sink", "toilet", "towel", "soap", "shampoo", "brush", "comb", "mirror",
    "fan", "heater", "air", "conditioner", "fridge", "stove", "oven", "microwave", "toaster", "blender",
    "door", "window", "wall", "floor", "ceiling", "roof", "fence", "gate", "path", "yard",
    "train", "submarine", "helicopter", "zeppelin", "sailboat", "kayak", "scooter", "skateboard", "hoverboard", "tricycle",
    "vase", "statue", "painting", "clock", "lamp", "candle", "trophy", "photo", "poster", "mirror",
    "clock", "watch", "calendar", "thermometer", "barometer", "compass", "thermometer", "scale", "radio", "tuner"
]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")
            input()

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        input()

    print(stages[lives])