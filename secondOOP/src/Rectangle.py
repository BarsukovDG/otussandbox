from secondOOP.src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, x, y):
        super().__init__("Rectangle")
        self.x = x
        self.y = y

    @property
    def area(self):
        return self.x * self.y

    @property
    def perimeter(self):
        return (self.x + self.y) * 2
