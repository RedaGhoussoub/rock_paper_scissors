import random
from enum import Enum


class GameOutcome(Enum):
    USER = "user"
    COMPUTER = "computer"
    DRAW = "draw"


def greetings(username: str) -> None:
    print(f"Hello, {username}")


def message(choice: str, outcome: GameOutcome) -> str:
    if outcome == GameOutcome.USER:
        result = f"Well done. The computer chose {choice} and failed"
    elif outcome == GameOutcome.COMPUTER:
        result = f"Sorry, but the computer chose {choice}"
    else:
        result = f"There is a draw ({choice})"
    return result


def get_choices() -> list[str]:
    choices = input()
    if not choices:
        return ["rock", "paper", "scissors"]
    return choices.split(",")


def get_initial_score(username: str) -> int:
    with open("rating.txt", "r") as file:
        for line in file:
            if username in line:
                return int(line.split()[1])
    return 0


def increment_score(game_outcome: GameOutcome, score: int) -> int:
    if game_outcome == GameOutcome.DRAW:
        score += 50
    if game_outcome == GameOutcome.USER:
        score += 100
    return score


def get_winner(user_choice: str, computer_choice: str, options: list[str]) -> GameOutcome:
    index = options.index(user_choice)
    sorted_options = options[index + 1:] + options[:index]
    strong_options = sorted_options[:len(sorted_options) // 2]
    if user_choice == computer_choice:
        return GameOutcome.DRAW
    else:
        if computer_choice in strong_options:
            return GameOutcome.COMPUTER
        else:
            return GameOutcome.USER


def main():
    username = input("Enter your name: ")
    greetings(username)
    choices = get_choices()
    score = get_initial_score(username)

    print("Okay, let's start")

    while True:
        user_choice = input()
        if "!exit" in user_choice:
            print("Bye!")
            break
        elif "!rating" in user_choice:
            print(f"Your rating: {score}")
        elif user_choice not in choices:
            print("Invalid input")
        else:
            computer_choice = random.choice(choices)
            outcome = get_winner(user_choice, computer_choice, choices)
            score = increment_score(outcome, score)
            print(message(computer_choice, outcome))


if __name__ == "__main__":
    main()
