from secondOOP.src.Figure import Figure


class Triangle(Figure):

    def __init__(self, x, y, z):
        super().__init__("Triangle")
        if x + y > z and x + z > y and y + z > x:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError('the sum of any two triangle sides should be higher than third one')

    # def __new__(cls, x, y, z):
    #     if x + y > z and x + z > y and y + z > x:
    #        triangle = super(Triangle, cls).__new__(cls)
    #        triangle.x = x
    #        triangle.y = y
    #        triangle.z = z
    #        return triangle
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
