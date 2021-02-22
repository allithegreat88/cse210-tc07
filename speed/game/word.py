from game.actor import Actor

class Word(Actor):
    def __init__(self):
        super().__init__()
        self.word_bank = self.create_word_bank()
        pass

    def get_all(self):
        # Returns a list of all the words on the screen
        pass

    def generate_words(self):
        # Make sure there is an if statement that makes is so it only generates new words if the others reache the end
        pass

    def create_word_bank(self):
        pass