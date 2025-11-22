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


class LoudNote(Note):
    def __init__(self, nota, is_long=False):
        Note.__init__(self, nota, is_long)

    def __str__(self):
        if self.s:
            if self.nota == "ре":
                return (self.nota + "-" + "э").upper()
            elif self.nota == "соль":
                return (self.nota[:-2] + "-" + "оль").upper()
            elif self.nota == "ля":
                return (self.nota + "-" + "а").upper()
            return (self.nota + "-" + self.nota[-1]).upper()
        else:
            return self.nota.upper()


class DefaultNote(Note):
    def __init__(self, nota="до", is_long=False):
        Note.__init__(self, nota, is_long)

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


class NoteWithOctave(Note):
    def __init__(self, nota, a, is_long=False):
        self.a = a
        Note.__init__(self, nota, is_long)

    def __str__(self):
        if self.s:
            if self.nota == "ре":
                return f"{self.nota}-э ({self.a})"
            elif self.nota == "соль":
                return f"{self.nota[:-2]}-оль ({self.a})"
            elif self.nota == "ля":
                return f"{self.nota}-а ({self.a})"
            return f"{self.nota}-{self.nota[-1]} ({self.a})"
        else:
            return f"{self.nota} ({self.a})"
