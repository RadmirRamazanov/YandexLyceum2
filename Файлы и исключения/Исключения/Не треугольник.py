def istriangle(*data):
    if len(data) != 3:
        raise NotEnoughError
    a, b, c = data[0], data[1], data[2]
    if len(a) == 2 and len(b) == 2 and len(c) == 2:
        S = 0.5 * abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
        return S != 0
    else:
        raise DoNotMatchError


class NotEnoughError(IndexError):
    def __str__(self):
        return "Not enough arguments."


class DoNotMatchError(IndexError):
    def __str__(self):
        return "The number of coordinates does not match."
