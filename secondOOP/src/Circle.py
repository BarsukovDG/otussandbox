from secondOOP.src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        super().__init__("Circle")
        self.r = radius
        self.p = 3.14

    @property
    def perimeter(self):
        return (self.r * self.p) * 2

    @property
    def area(self):
        return (self.r ** 2) * self.p
