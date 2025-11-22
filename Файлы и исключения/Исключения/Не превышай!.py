def not_exceed(*data):
    fines = []
    for i in data:
        f = 0
        if "settlement" not in i:
            i["settlement"] = False
        if "limit" in i:
            if i["settlement"] and i["limit"] > 60:
                raise SpeedLimitError
        if "limit" not in i:
            if i["settlement"]:
                i["limit"] = 60
            else:
                i["limit"] = 90
        if i["fine"] == 0:
            raise DataError
        if i["speed"] > i["limit"] + i["delta"]:
            f += i["fine"]
        fines.append(f)
    return fines


class SpeedLimitError(TypeError):
    def __str__(self):
        return "Speed limit controversy."


class DataError(TypeError):
    def __str__(self):
        return "Error in data."
