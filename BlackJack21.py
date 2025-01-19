import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / 
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    print(logo)

    def draw_card():
        return cards[random.randint(0, 13)]

    def adjust_for_aces(deck, current_sum):
        while current_sum > 21 and 11 in deck:
            deck.remove(11)
            deck.append(1)
            current_sum -= 10
        return current_sum

    num1 = draw_card()
    num2 = draw_card()
    num3 = draw_card()
    num4 = draw_card()

    player_deck = [num1, num2]
    computer_deck = [num3, num4]

    sum_player = num1 + num2
    sum_computer = num3 + num4

    sum_player = adjust_for_aces(player_deck, sum_player)
    sum_computer = adjust_for_aces(computer_deck, sum_computer)

    print(f"Your cards: {player_deck}, current score: {sum_player}")
    print(f"Computer's first card: {computer_deck[0]}")

    game_is_on = True

    while game_is_on:
        if sum_player > 21:
            print(f"\nYour final hand: {player_deck}, final score: {sum_player}")
            print(f"Computer's final hand: {computer_deck}, final score: {sum_computer}")
            print("You went over. You lose!")
            break

        more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if more_cards == "y":
            new_num_player = draw_card()
            player_deck.append(new_num_player)
            sum_player += new_num_player

            sum_player = adjust_for_aces(player_deck, sum_player)

            print(f"Your cards: {player_deck}, current score: {sum_player}")
            print(f"Computer's first card: {computer_deck[0]}")

        elif more_cards == "n":
            while sum_computer < 17:
                new_num_computer = draw_card()
                computer_deck.append(new_num_computer)
                sum_computer += new_num_computer
                sum_computer = adjust_for_aces(computer_deck, sum_computer)

            print(f"\nYour final hand: {player_deck}, final score: {sum_player}")
            print(f"Computer's final hand: {computer_deck}, final score: {sum_computer}")

            if sum_player > 21:
                print("You went over. You lose!")
            elif sum_computer > 21:
                print("Opponent went over. You win!")
            elif sum_player == sum_computer:
                print("It's a draw!")
            elif sum_player > sum_computer:
                print("You win!")
            else:
                print("You lose!")

            break
        else:
            print("Invalid input, please try again.")

    while True:
        play_again = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_again == "y":
            blackjack()
            break
        elif play_again == "n":
            break
        else:
            print("Invalid input, please enter 'y' or 'n'.")


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == "y":
    blackjack()
else:
    input()
