class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        elif self.name == other.name and self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __gt__(self, other):
        if self.name != other.name:
            return self.name > other.name
        elif self.name == other.name and self.x != other.x:
            return self.x > other.x
        return self.y > other.y

    def __le__(self, other):
        if self.name != other.name:
            return self.name <= other.name
        elif self.name == other.name and self.x != other.x:
            return self.x <= other.x
        return self.y <= other.y

    def __ge__(self, other):
        if self.name != other.name:
            return self.name >= other.name
        elif self.name == other.name and self.x != other.x:
            return self.x >= other.x
        return self.y >= other.y

    def __eq__(self, other):
        if self.name != other.name:
            return self.name == other.name
        elif self.name == other.name and self.x != other.x:
            return self.x == other.x
        return self.y == other.y


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        Point.__init__(self, name, x, y)
        self.RGB = rgb

    def get_color(self):
        return self.RGB

    def __str__(self):
        return Point.__str__(self)

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, (255 - self.RGB[0], 255 - self.RGB[1], 255 - self.RGB[2]))

