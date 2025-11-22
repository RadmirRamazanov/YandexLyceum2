def prime(n):
    count = 0
    x = abs(n)
    d = 2
    while d * d <= x:
        if x % d == 0:
            count += 1
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        count += 1
    return count


def strangers(*data):
    p = []
    if len(data) == 0:
        raise NoArgsError
    for i in data:
        if not isinstance(i, int):
            raise ValueError("There are not only numbers among the arguments!")
        else:
            if prime(i) != 5:
                p.append(i)
    if len(p) == 0:
        raise EmptyListError
    p.sort()
    return p


class NoArgsError(TypeError):
    def __str__(self):
        return "The arguments are not passed."


class EmptyListError(TypeError):
    def __str__(self):
        return "There were no suitable numbers."

    def __str__(self):
        return "There were no suitable numbers."

