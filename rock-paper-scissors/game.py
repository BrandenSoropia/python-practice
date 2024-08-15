# use Python 3.12+, StrEnum comes from this version
from enum import StrEnum
import random
import time
import sys


class HandSign(StrEnum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    # Source: https://stackoverflow.com/a/54919285
    @classmethod
    def list(cls):
        """Return all values of an enum in a list"""
        return list(map(lambda c: c.value, cls))

    @classmethod
    # PEP8 convention: "cls" is like "self" but for class methods, where "self" is for instance methods https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes
    def random(cls):
        # list(cls) turns enum into a list with key/value pairs as items
        # when a random index is chosen and since our Enum inherits StrEnum, the printed result is just the value! (instead of the key value pair an Enum would print!)
        return random.choice(list(cls))


def prompt_player_hand_selection():
    """Prompt player to pick a hand sign for rock, paper, scissors and return it in upper case."""
    return input(f'Please choose by typing one of the following and pressing "Enter": {list(map(lambda sign: sign.lower(), HandSign.list()))} \nYour choice: ').upper()


def print_countdown():
    count_down_steps = ['Rock...', 'Paper...', 'Scissors..!']
    for step in count_down_steps:
        print(step)
        time.sleep(1)


def random_hand() -> str:
    """Return a hand sign generated at random."""
    return HandSign.random()


def check_if_player_won(player_hand, cpu_hand):
    isRockBestsScissors = player_hand == HandSign.ROCK and cpu_hand == HandSign.SCISSORS
    isPaperBeatsRock = player_hand == HandSign.PAPER and cpu_hand == HandSign.ROCK
    isScissorsBeatsPaper = player_hand == HandSign.SCISSORS and cpu_hand == HandSign.PAPER

    return isRockBestsScissors or isPaperBeatsRock or isScissorsBeatsPaper


def print_result(player_hand, cpu_hand):
    print(f"It's {player_hand} versus {cpu_hand}")

    didPlayerWin = check_if_player_won(player_hand, cpu_hand)

    if (didPlayerWin):
        print('You win!')
    else:
        print("You lose...")


def ask_to_replay():
    shouldReplay = input(
        "Do you want to play again? Type 'yes' and hit enter if you do. Otherwise hit enter to exit. \n")

    if (shouldReplay):
        play_match()

    else:
        print("Thanks for playing!")
        sys.exit()


def play_match():
    player_hand = prompt_player_hand_selection()
    print_countdown()
    cpu_hand = random_hand()

    print_result(player_hand, cpu_hand)
    ask_to_replay()


if __name__ == "__main__":
    play_match()
