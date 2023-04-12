from abc import abstractmethod


class Figure:

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        geometric_list = ['Square', 'Rectangle', 'Triangle', 'Circle']
        if figure.name in geometric_list:
            area = self.area
            added_area = figure.area
            return area + added_area
        else:
            raise ValueError('attempt to add non-geometric figure area')
