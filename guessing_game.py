class GuessingGame:
    def __init__ (self, answer):
        self.answer= answer
        self.answer_found = False

    def guess(self, guess):
        if guess == self.answer:
            self.answer_found=True
            return 'correct'
        elif guess < self.answer:
            self.answer_found= False
            return 'low'
        elif guess > self.answer:
            self.answer_found = False
            return 'high'    

    def solved(self):
        return self.answer_found        


game = GuessingGame(10)
print(game.guess(15))
print(game.solved())
print(game.guess(10))
print(game.solved())
print(game.guess(6))
print(game.solved())






