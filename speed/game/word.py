from game.actor import Actor

class Word(Actor):
    def __init__(self):
        super().__init__()
        self.word_bank = []
        self.words_on_screen = []

    def get_all(self):
        # Returns a list of all the words on the screen
        return self.words_on_screen

    def generate_words(self):
        # Make sure there is an if statement that makes is so it only generates new words if the others reache the end
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.SNAKE_LENGTH):
            text = "8" if n == 0 else "#"
            position = Point(x - n, y)
            velocity = Point(1, 0)

    def create_word_bank(self):
        with open("words.txt", "rt") as reader:
            self.word_bank = reader.readlines()
        return self.word_bank