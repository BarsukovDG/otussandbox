from secondOOP.src.Figure import Figure


class Square(Figure):

    def __init__(self, x):
        super().__init__("Square")
        self.x = x

    @property
    def perimeter(self):
        return self.x * 4

    @property
    def area(self):
        return self.x * self.x
