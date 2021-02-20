from game.actor import Actor

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.buffer = None
        pass

    def add_letter(self, letter):
        pass

    def get_buffer(self):
        return self._buffer