class Game:
    def __init__(self, word):
        self.word = word
        self.right_guess = 0
        self.wrong_guess = 0
        self.guessed_correct = []
        self.total_guesses = len(word)

        for letter in word:
            self.guessed_correct.append("_")

    def display(self):
        print("Hangman Time")
        print("Hidden word has {} letters to guess".format(str(len(self.word))))
        print("{} guesses left!".format(self.total_guesses))
        temp = ""
        for spot in self.guessed_correct:
            temp += spot + " "
        print(temp)

    def guess_spot(self, guess):
        self.total_guesses -= 1
        for idx, letter in enumerate(self.word):
            if guess == letter:
                self.guessed_correct[idx] = guess

    def winner(self):
        for spot in self.guessed_correct:
            if spot == "_":
                return False
        return True

    def loser(self):
        if self.total_guesses == 0:
            return True
        else:
            return False

    def get_right_guesses(self):
        for spot in self.guessed_correct:
            if spot != "_":
                self.right_guess += 1
        return self.right_guess
