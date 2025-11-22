class Bell:
    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = kwargs

    def print_info(self):
        ans = ""
        c = 0
        if len(self.kwargs) > 0:
            for k, i in sorted(self.kwargs.items()):
                c += 1
                if c != len(self.kwargs):
                    ans += f"{k}: {i}"
                    ans += ", "
                else:
                    if len(self.args) > 0:
                        ans += f"{k}: {i}"
                        ans += "; "
                    else:
                        ans += f"{k}: {i}"
        if len(self.args) > 0:
            for i in self.args:
                if i != self.args[-1]:
                    ans += i
                    ans += ", "
                else:
                    ans += i
        if len(self.args) == 0 and len(self.kwargs) == 0:
            print("-")
        else:
            print(ans)


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "LittleBell"

    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = 0
        self.name = "BigBell"

    def sound(self):
        if self.c % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.c += 1


class BellTower:
    def __init__(self, *args):
        self.kolokls = list(args)

    def sound(self):
        for i in self.kolokls:
            i.sound()
        print("...")

    def append(self, kolokol):
        self.kolokls.append(kolokol)

    def print_info(self):
        c = 1
        for i in self.kolokls:
            print(c, i.name)
            i.print_info()
            c += 1
        print("")


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        super().__init__()
        self.size = size
        for bell in args:
            self.append(bell)

    def append(self, kolokol):
        if len(self.kolokls) >= self.size:
            self.kolokls.pop(0)
        self.kolokls.append(kolokol)


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        self.bell_type = bell_type
        filter = [i for i in args if type(i) is self.bell_type]
        super().__init__(*filter)

    def append(self, kolokol):
        if type(kolokol) is self.bell_type:
            super().append(kolokol)
    