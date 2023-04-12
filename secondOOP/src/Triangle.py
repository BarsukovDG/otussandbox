from secondOOP.src.Figure import Figure


class Triangle(Figure):

    def __init__(self, x, y, z):
        super().__init__("Triangle")
        if x + y > z and x + z > y and y + z > x:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise AttributeError('the sum of any two triangle sides should be higher than third one')

    # def __new__(cls, x, y, z):
    #     if x + y > z and x + z > y and y + z > x:
    #         cls.x = x
    #         cls.y = y
    #         cls.z = z
    #     else:
    #         return None

    @property
    def area(self):
        s = (self.x + self.y + self.z) / 2
        area = (s * (s - self.x) * (s - self.y) * (s - self.z)) ** 0.5
        return area

    @property
    def perimeter(self):
        return self.x + self.y + self.z
