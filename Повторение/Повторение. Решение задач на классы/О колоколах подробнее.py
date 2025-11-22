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
        Bell.__init__(self, *args, **kwargs)

    def sound(self):
        print("ding")

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


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        Bell.__init__(self, *args, **kwargs)
        self.c = 0

    def sound(self):
        if self.c % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.c += 1

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


class BellTower(LittleBell, BigBell):
    def __init__(self, *args):
        self.kolokls = list(args)

    def sound(self):
        for i in self.kolokls:
            i.sound()
        print("...")

    def append(self, kolokol):
        self.kolokls.append(kolokol)
