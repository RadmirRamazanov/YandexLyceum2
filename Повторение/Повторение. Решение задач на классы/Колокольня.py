class LittleBell:
    def sound(self):
        print("ding")


class BigBell:
    def __init__(self):
        self.c = 0

    def sound(self):
        if self.c % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.c += 1


class BellTower(LittleBell, BigBell):
    def __init__(self, *args):
        self.kolokls = list(args)

    def sound(self):
        for i in self.kolokls:
            i.sound()
        print("...")

    def append(self, kolokol):
        self.kolokls.append(kolokol)
    