import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self,minlen):
        maxlen = len(max(self.words,key=lambda x:len(x)))
        if maxlen < minlen:
            minlen = maxlen
        while True:
            r = random.randrange(self.count)
            if len(self.words[r])>=minlen:break
        return self.words[r]
