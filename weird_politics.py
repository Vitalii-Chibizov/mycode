#!/usr/bin/env python3
import os
import random

COLORS = {
    "pure": "\033[97m",  # white
    "sky": "\033[94m",  # blue
    "pink": "\033[95m",  # pink
    "gold": "\033[93m",  # yellow
    "fire": "\033[33m",  # orange
    "rage": "\033[91m",  # red

    "Reset": "\033[0m",  # reset
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to determine the winner of a round
def determine_winner(player, ai):
    if player == ai:
        return "Draw"
    elif (
            (player == "A" and (ai == "M" or ai == "B")) or
            (player == "P" and (ai == "A" or ai == "M")) or
            (player == "I" and (ai == "P" or ai == "A")) or
            (player == "B" and (ai == "I" or ai == "P")) or
            (player == "M" and (ai == "B" or ai == "I"))
    ):
        return "Player"
    else:
        return "AI"


def print_hands(ai_hand, player_hand):
    clear_console()

    ai_hand.sort()
    player_hand.sort()
    print("\033[97mAI's hand:    \033[0m", end="")
    better_print(ai_hand, COLORS)
    print("\n")
    print(f"\033[97mPlayer's hand: \033[0m", end="")
    better_print(player_hand, COLORS)
    print("\n")


def better_print(elements, colors):
    for element in elements:
        if element == "A":
            print("\033[94m Aristocrat \033[0m", end="")
        elif element == "P":
            print("\033[95m Prostitute \033[0m", end="")
        elif element == "I":
            print("\033[33m Inquisitor \033[0m", end="")
        elif element == "B":
            print("\033[93m Bishop \033[0m", end="")
        else:
            print("\033[91m Mercenary \033[0m", end="")


def player_choice(citizens, player_hand):
    choice = input("\nWho would you send? (A/P/I/B/M): ").strip().capitalize()
    while True:
        if choice in citizens and choice in player_hand:
            break
        elif choice == "exit":
            break
        else:
            print("Invalid option. Please choose a valid option.")
    return choice


def ai_choice(ai_hand):
    # AI brain
    choice = random.choice(ai_hand)
    print(f"AI have called for: {choice}\n")
    return choice


def trash_talk(champion):
    print()
    # Some dialogs based on champion occupation
    if champion == "A":
        print("Aristocrat hires the Mercenary and corrupts the Bishop.")
    elif champion == "P":
        print("Prostitute captivates the Aristocrat's heart and lures the Mercenary.")
    elif champion == "I":
        print("Inquisition extorts the Aristocrat and issues a fiery threat to the Prostitute")
    elif champion == "B":
        print("Bishop initiates an Inquisition and controls the Prostitutes.")
    elif champion == "M":
        print("Mercenary falls for the Prostitute's charm and intimidates the Bishop.")
    else:
        print("Draw: Both citizens simply smile at each other")
    print()


def politics_check(player_score, ai_score, politics_threshold):
    if (player_score == politics_threshold) or (ai_score == politics_threshold):
        print("Game is over. City has voted for it's ruler.\nFinal scores: ")
        print(f"\033[97mInfluence points: \033[0m")
        print(f"Player: {player_score} | AI: {ai_score}")
        if player_score > ai_score:
            print("Congratulations! Your manipulations and ambitions served you well.")
            return True
        elif player_score < ai_score:
            print("AI, your opponent, obliterated you, as expected! Better luck next time!")
            return True
        else:
            print("It's a draw!")
            return True
    else:
        return False


def population_check(city):
    if len(city) <= 1:  # odd number or no citizens left
        print("In politics dog fight you are the only one to rule and only one to serve. City is dead")
        return True
    else:
        return False


# if you pull it out - you are actually cool guy
def special_win(player, elements):
    special_number = 3
    for element in elements:
        count = elements.count(element)
        if count >= special_number:
            print(f"Magnificent! {player} managed to win by overpopulating city with 4 similar profession citizens! "
                  f"You won the game on a spot!")
            return True
        else:
            return False


def main():
    # Initialize the main lists
    citizens = ["A", "P", "I", "B", "M"]
    population = 4
    city = []
    for element in citizens:
        city.extend([element] * population)

    # Initialize player's and AI's hands
    # To make game fair, each will have same base hand
    player_hand = citizens[:]
    ai_hand = citizens[:]

    # TODO: random from deck
    # player_hand = random.city(citizens, k=5)
    # ai_hand = random.city(citizens, k=5)

    # One of the win conditions - get politics score up to 4
    politics_threshold = 5
    player_score = 0
    ai_score = 0

    # Main game loop (infinite))
    while True:
        print(f"\n")
        # Phase 0 - Rules

        # Phase 1 - field
        print_hands(ai_hand, player_hand)
        player = player_choice(citizens, player_hand)
        if player == "exit":
            break
        ai = ai_choice(ai_hand)

        # Phase 2 - brawl and champion occupation (if not a draw)
        champion_lord = determine_winner(player, ai)
        if champion_lord == "Player":
            player_score += 1
            print(f"AI lost his follower {ai}")
            print(f"Player: {player_score} | AI: {ai_score}")
            champion = player
            ai_hand.remove(ai)
        elif champion_lord == "AI":
            ai_score += 1
            print(f"You lost your follower {player}")
            print(f"Player: {player_score} | AI: {ai_score}")
            champion = ai
            player_hand.remove(player)
        else:
            champion = "Draw"

        # Phase 3 - trash talk for flavor!!!
        trash_talk(champion)

        # Phase 4 - game over conditions check

        # - Empty city
        endgame = politics_check(player_score, ai_score, politics_threshold)
        if endgame:
            input("Press the Enter key to continue: ")
            break

        # - Victory due to politics threshold breached
        endgame = population_check(city)
        if endgame:
            input("Press the Enter key to continue: ")
            break

        # - Special victory conditions:
        if (special_win("Player", player_hand) and special_win("AI", ai_hand)):
            print(f"Such a coincident! Both of players got special win. Draw then...")
            endgame = True
        elif special_win("Player", player_hand):
            print(f"True victory! Special win condition achievement unlocked")
            endgame = True
        elif special_win("AI", ai_hand):
            print(f"True failure! Yes, you are special, kinda")
            endgame = True
        if endgame:
            input("Press the Enter key to continue: ")
            break

        # Phase 5 - Shuffle the elements of city and draw a card
        # Since game is not over at this point - we will draw and start over
        random.shuffle(city)
        player_hand.append(city[0])
        city.remove(city[0])

        random.shuffle(city)
        ai_hand.append(city[0])
        city.remove(city[0])

        input("Press the Enter key to continue: ")


if __name__ == "__main__":
    main()

