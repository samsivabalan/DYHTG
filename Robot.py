class Robot:

    def __init__(self):
        self.head = None
        self.body = None
        self.arms = None
        self.legs = None

    def assemble(self, part, type):
        self.part = type