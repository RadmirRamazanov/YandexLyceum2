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


class CheckMark:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.a.name + self.b.name + self.c.name)

    def __bool__(self):
        if self.a.x * (self.b.y - self.c.y) + self.b.x * (self.c.y - self.a.y) + self.c.x * (self.a.y - self.b.y) == 0:
            return False
        elif (self.a.x == self.b.x and self.a.y == self.b.y) or (self.a.x == self.c.x and self.a.y == self.c.y) \
                or (self.b.x == self.c.x and self.b.y == self.c.y):
            return False
        return True

    def __eq__(self, other):
        if self.b.x != other.b.x or self.b.y != other.b.y:
            return False
        if (self.a.x == other.a.x and self.a.y == other.a.y) and (self.c.x == other.c.x and self.c.y == other.c.y):
            return True
        elif (self.a.x == other.c.x and self.a.y == other.c.y) and (self.c.x == other.a.x and self.c.y == other.a.y):
            return True
        return False
