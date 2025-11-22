def chirp(*args, **kwargs):
    ans = []
    if len(kwargs) == 0:
        raise NoSubstringError
    for i in args:
        if not isinstance(i, str):
            raise TypeError("The argument is not a string.")
        if kwargs["taboo"] not in i:
            ans.append(i)
    ans.sort()
    return ans


class NoSubstringError(TypeError):
    def __str__(self):
        return "No named argument."
    