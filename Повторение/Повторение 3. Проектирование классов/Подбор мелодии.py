N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, nota, is_long=False):
        self.nota = nota
        self.s = is_long

    def __str__(self):
        if self.s:
            if self.nota == "ре":
                return self.nota + "-" + "э"
            elif self.nota == "соль":
                return self.nota[:-2] + "-" + "оль"
            elif self.nota == "ля":
                return self.nota + "-" + "а"
            return self.nota + "-" + self.nota[-1]
        else:
            return self.nota

    def __lt__(self, other):
        return PITCHES.index(self.nota) < PITCHES.index(other.nota)

    def __gt__(self, other):
        return PITCHES.index(self.nota) > PITCHES.index(other.nota)

    def __le__(self, other):
        return PITCHES.index(self.nota) <= PITCHES.index(other.nota)

    def __ge__(self, other):
        return PITCHES.index(self.nota) >= PITCHES.index(other.nota)

    def __eq__(self, other):
        return PITCHES.index(self.nota) == PITCHES.index(other.nota)

    def __rshift__(self, other):
        inota = PITCHES.index(self.nota)
        if not self.s:
            k = (inota + other) % len(PITCHES)
            return Note(PITCHES[k], self.s)
        else:
            k = (inota + other) % len(PITCHES)
            return Note(PITCHES[k], self.s)

    def __lshift__(self, other):
        inota = PITCHES.index(self.nota)
        if not self.s:
            k = (inota - other) % len(PITCHES)
            return Note(PITCHES[k], self.s)
        else:
            k = (inota - other) % len(PITCHES)
            return Note(PITCHES[k], self.s)

    def get_interval(self, other):
        return INTERVALS[abs(PITCHES.index(self.nota) - PITCHES.index(other.nota))]

    def __getitem__(self, item):
        if self.s:
            if self.nota == "ре":
                return (self.nota + "-" + "э")[item]
            elif self.nota == "соль":
                return (self.nota[:-2] + "-" + "оль")[item]
            elif self.nota == "ля":
                return self.nota + "-" + "а"
            return (self.nota + "-" + self.nota[-1])[item]
        else:
            return self.nota[item]


class Melody:
    def __init__(self, lst=None):
        if lst is None:
            self.lst = []
        else:
            self.lst = lst

    def __str__(self):
        if not self.lst:
            return ""
        r = str(self.lst[0])
        if r:
            r = r[0].upper() + r[1:]
        if len(self.lst) > 1:
            for i in self.lst[1:]:
                r += ", " + str(i)
        return r

    def append(self, cl):
        self.lst.append(cl)

    def replace_last(self, cl):
        if self.lst:
            self.lst[-1] = cl

    def remove_last(self):
        if self.lst:
            self.lst.pop()

    def clear(self):
        self.lst.clear()

    def __len__(self):
        return len(self.lst)

    def transpose(self, s):
        for i in self.lst:
            ind = PITCHES.index(i.nota)
            nind = ind + s
            if nind < 0 or nind >= len(PITCHES):
                return Melody([Note(note.nota, note.s) for note in self.lst])
        new = []
        for i in self.lst:
            ind = PITCHES.index(i.nota)
            nind = ind + s
            new.append(Note(PITCHES[nind], i.s))
        return Melody(new)

    def __rshift__(self, s):
        return self.transpose(s)

    def __lshift__(self, s):
        return self.transpose(-s)

