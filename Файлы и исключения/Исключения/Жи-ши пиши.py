def check(data):
    for i in data.split():
        zh = i.lower().find("ж")
        if zh != -1 and i[zh + 1] in "юяы":
            raise BrokenRuleError
        ch = i.lower().find("ч")
        if ch != -1 and i[ch + 1] in "юяы":
            raise BrokenRuleError
        sh = i.lower().find("ш")
        if sh != -1 and i[sh + 1] in "юяы":
            raise BrokenRuleError
        shc = i.lower().find("щ")
        if shc != -1 and i[shc + 1] in "юяы":
            raise BrokenRuleError
    return "That's right."


class BrokenRuleError(TypeError):
    def __str__(self):
        return "The rule is broken."
