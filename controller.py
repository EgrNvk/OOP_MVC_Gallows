from model import GallowsModel
from view import GallowsView

class GallowsController:
    def __init__(self):
        self.model = GallowsModel()
        self.view = GallowsView()
        self.view.set_guess_handler(self.on_guess)
        self.update_view()

    def update_view(self):
        masked=self.model.masked_word()
        self.view.set_word(masked)
        self.view.set_attempts(self.model.wrong_attempts, self.model.max_attempts)

    def on_guess(self):
        letter=self.view.letter_var.get().strip().lower()
        self.view.letter_var.set("")
        self.view.entry.focus()

        if not letter:
            self.view.set_message("Введіть літеру.")
            return

        if len(letter) != 1:
            self.view.set_message("Вводьте тільки одну літеру.")
            return

        result=self.model.guess_letter(letter)
        if result=="вгадано":
            self.view.set_message("Буква вгадана.")
        elif result=="помилка":
            self.view.set_message("Такої букви немає.")
        else:
            self.view.set_message("Цю літеру вже відкривали.")
        self.update_view()

        if self.model.is_won():
            self.view.set_word(self.model.masked_word())
            self.view.set_message(f"Ви вгадали слово: {self.model.secret}")

            self.view.button.config(state="disabled")
            self.view.entry.config(state="disabled")

        elif self.model.is_lost():
            self.view.set_message(f"Ви програли. Слово було {self.model.secret}")

            self.view.button.config(state="disabled")
            self.view.entry.config(state="disabled")

    def run(self):
        self.view.mainloop()