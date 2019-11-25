class Guess:
    def __init__(self, word):
        self.word = word
        self.guessedChars = set()
        self.numTries = 0
        self.filledWord = "_" * len(word)

    def display(self):
        print("Current: " + self.filledWord)
        print("Tries: " + str(self.numTries))
        pass


    def guess(self, character):
        self.guessedChars.add(character)
        if not character in self.word:
            self.numTries+=1
        else:
            wl = list(self.filledWord);
            for i in range(len(self.word)):
                if self.word[i] == character:
                    wl[i] = character
            self.filledWord = ''.join(wl)
        if not self.word.find('_'):
            return True
        return False
