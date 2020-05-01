from .sheet import Sheet
from .beeper import Beeper
from animals.monkey import Monkey

class Printer(object):
    def __init__(self):
        self.sound = Beeper()
        self.paper = Sheet()
        self.spy = Monkey()

    def print_paper(self, value):
        self.paper.write(value)
        self.sound.activate()

    def read_paper(self):
        self.spy.talk()
        self.paper.read()
