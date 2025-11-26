class Note:
    def __init__(self, nota, s=False):
        self.nota = nota
        self.s = s

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
    