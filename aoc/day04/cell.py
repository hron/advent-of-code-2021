class Cell:
    def __init__(self, value: int):
        self.value = value
        self.marked = False

    def mark(self):
        self.marked = True

    def is_marked(self) -> bool:
        return self.marked

    def __repr__(self):
        return "{:>2}{:>1}".format(self.value, '*' if self.is_marked() else '')
