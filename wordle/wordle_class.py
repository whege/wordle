__all__ = ['Wordle']

import random
from string import ascii_lowercase

from english_words import english_words_lower_alpha_set


class Wordle:
    def __init__(self):
        self._answer = random.choice([w for w in english_words_lower_alpha_set if len(w) == 5])
        self._attempts = []
        self._display_answer = ["-"] * 5
        self._in_word = []
        self._lives = 5
        self._playing = True
        self._unused = list(ascii_lowercase)

    @property
    def active(self):
        return self._playing

    @property
    def answer(self):
        return self._answer

    @property
    def attempts(self):
        return self._attempts

    @property
    def display_answer(self):
        return "".join(self._display_answer)

    @property
    def in_word(self):
        return self._in_word

    @property
    def lives(self):
        return self._lives

    @property
    def unused_letters(self):
        return self._unused

    def handle_guess(self, guess: str):
        assert len(guess) == len(self._answer)

        if guess == self._answer:
            self._win()

        else:
            self._lives -= 1
            self._attempts.append(guess)

            for i in range(len(guess)):
                try:
                    self._unused.remove(guess[i])
                except ValueError:
                    pass

                if guess[i] == self._answer[i]:
                    self._display_answer[i] = guess[i]
                    if guess[i] not in self._in_word:
                        self._in_word.append(guess[i])

                elif (guess[i] in self._answer) and (guess[i] not in self._in_word):
                    self._in_word.append(guess[i])

    def _win(self):
        print(f"'{self._answer}' is right! You win! Thanks for playing :D")
        self._playing = False
