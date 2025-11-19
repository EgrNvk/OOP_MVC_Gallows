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
        result.append(self.secret[0])
        for _ in range(len(self.secret)-2):
            result.append("-")
        result.append(self.secret[-1])
        return result

    def guess_letter(self, letter: str):
        if letter not in self.secret:
            return "помилка"
        if letter in self.secret:
            return "вгадано"