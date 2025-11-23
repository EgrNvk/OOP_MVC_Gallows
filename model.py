import random

class GallowsModel:
    def __init__(self):
        self.words=["коробка", "смартфон"]

        self.secret=random.choice(self.words)
        self.guessed=set()
        self.max_attempts=6
        self.wrong_attempts=0
        self.guessed.add(self.secret[0])
        self.guessed.add(self.secret[-1])

    def masked_word(self):
        result = []
        for ch in self.secret:
            if ch in self.guessed:
                result.append(ch)
            else:
                result.append("-")
        return result

    def open_letter(self, letter):
        self.guessed.add(letter)

    def guess_letter(self, letter: str):
        letter = letter.lower()

        if letter in self.guessed:
            return "повтор"

        if letter in self.secret:
            self.open_letter(letter)
            return "вгадано"
        else:
            self.wrong_attempts = self.wrong_attempts + 1
            return "помилка"

    def is_won(self):
        return all(ch in self.guessed for ch in self.secret)

    def is_lost(self):
        return self.wrong_attempts >= self.max_attempts