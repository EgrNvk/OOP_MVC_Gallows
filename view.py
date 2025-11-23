import tkinter as tk

class GallowsView:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Шибениця")
        self.root.geometry("500x500")

        self.title_label=tk.Label(self.root, text="Я загадав слово", font=("Arial", 16))
        self.title_label.pack(pady=(10, 5))

        self.word_label=tk.Label(self.root, text="", font=("Arial", 18))
        self.word_label.pack(pady=(0, 10))

        self.attempts_label=tk.Label(self.root, text="Спроби: 0/6", font=("Arial", 12))
        self.attempts_label.pack(pady=(0, 10))

        self.letter_var=tk.StringVar()
        self.entry=tk.Entry(self.root, textvariable=self.letter_var, width=5, font=("Arial", 16))
        self.entry.pack(pady=(5, 5))

        self.button=tk.Button(self.root, text="Вгадати", font=("Arial", 12))
        self.button.pack(pady=(5, 5))

        self.message_label=tk.Label(self.root, text="", font=("Arial", 12))
        self.message_label.pack(pady=(5, 5))

    def set_word(self, masked_list):
        self.word_label.config(text=f"Слово: {' '.join(masked_list)}")

    def set_attempts(self, wrong, maximum):
        self.attempts_label.config(text=f"Спроби: {wrong}/{maximum}")

    def set_message(self, message):
        self.message_label.config(text=message)

    def set_guess_handler(self, handler):
        self.button.config(command=handler)

    def mainloop(self):
        self.root.mainloop()