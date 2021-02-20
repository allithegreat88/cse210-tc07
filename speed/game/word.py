from game.actor import Actor

class Word(Actor):
    def __init__(self):
        super().__init__()
        word_bank = create_word_bank(self)
        pass

    def get_all(self):
        pass

    def generate_words(self):
        # Make sure there is an if statement that makes is so it only generates new words if the others reache the end
        pass

    def create_word_bank(self):
        pass