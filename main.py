# Name: Chase Prasad
# Title: Blackjack

from random import Random
rng = Random()

game = 1
playerWins = 0
dealerWins = 0
tieWins = 0

while True:
    playing = True
    card = rng.next_int(13) + 1

    if card == 11 or card == 12 or card == 13:
        hand = 10
    else:
        hand = card

    print(f"\nSTART GAME #{game}\n")
    match card:
        case 1:
            print(f"Your card is a ACE!")
        case 11:
            print(f"Your card is a JACK!")
        case 12:
            print(f"Your card is a QUEEN!")
        case 13:
            print(f"Your card is a KING!")
        case _:
            print(f"Your card is a {card}!")
    print(f"Your hand is: {hand}\n")

    while playing:
        choice = int(input("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: "))
        match choice:
            case 1:
                card = rng.next_int(13) + 1
                match card:
                    case 1:
                        print(f"\nYour card is a ACE!")
                        hand += 1
                    case 11:
                        print(f"\nYour card is a JACK!")
                        hand += 10
                    case 12:
                        print(f"\nYour card is a QUEEN!")
                        hand += 10
                    case 13:
                        print(f"\nYour card is a KING!")
                        hand += 10
                    case _:
                        print(f"\nYour card is a {card}!")
                        hand += card
                print(f"Your hand is: {hand}\n")

                if hand == 21:
                    print("BLACKJACK! You win!")
                    playerWins += 1
                    game += 1
                    playing = False
                elif hand > 21:
                    print("You exceeded 21! You lose.")
                    dealerWins += 1
                    game += 1
                    playing = False

            case 2:
                dealer = rng.next_int(11) + 16
                print(f"\nDealer's hand: {dealer}")
                print(f"Your hand is: {hand}\n")

                if dealer > 21:
                    print("You win!")
                    playerWins += 1
                    game += 1
                    playing = False
                elif dealer > hand:
                    print("Dealer wins!")
                    dealerWins += 1
                    game += 1
                    playing = False
                elif dealer == hand:
                    print("It's a tie! No one wins!")
                    tieWins += 1
                    game += 1
                    playing = False
                else:
                    print("You win!")
                    playerWins += 1
                    game += 1
                    playing = False

            case 3:
                print(f"\nNumber of Player wins: {playerWins}")
                print(f"Number of Dealer wins: {dealerWins}")
                print(f"Number of tie games: {tieWins}")
                print(f"Total # of games played is: {game - 1}")
                print(f"Percentage of Player wins: {round(((playerWins / (game - 1)) * 100), 1)}%\n")

            case 4:
                exit()
                
            case _:
                print("\nInvalid input!\nPlease enter an integer value between 1 and 4.\n")