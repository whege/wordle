from wordle.wordle_class import Wordle


def wordle():
    input("Welcome to Terminal Wordle, aka TermiNordle! Press enter to begin: ")

    game = Wordle()

    while game.active and (game.lives != 0):
        print(f"{game.display_answer} | Correct letters {game.in_word} | Attempts {game.attempts}")
        print(f"Letters left: {game.unused_letters} | Lives left: {game.lives}")
        guess: str = input("Guess: ")

        if not guess.isalpha():
            print("That's not a word! Try again.")
            continue

        elif len(guess) != 5:
            print("Valid guesses must be 5 letters.")
            continue

        else:
            game.handle_guess(guess)
            if not game.active:
                return
            else:
                continue

    print(f"The correct answer was '{game.answer}'! Thanks for playing :D ")


if __name__ == '__main__':
    wordle()
