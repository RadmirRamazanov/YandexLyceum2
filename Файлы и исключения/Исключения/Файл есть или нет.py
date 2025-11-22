import json


a, b = input(), input()
s = ""
ans = ""
try:
    with open(a, "r", encoding="utf-8") as f:
        data = json.load(f)
        for i in data:
            try:
                ans += i[b]
                ans += " "
            except KeyError:
                print("The key is missing.")
                ans = ""
                break
            except TypeError:
                print("It is impossible to add non-line with line.")
                ans = ""
                break
        try:
            s = ans[0]
        except IndexError:
            pass
        else:
            print(ans)
except FileNotFoundError:
    print("There is no such file in the directory.")


