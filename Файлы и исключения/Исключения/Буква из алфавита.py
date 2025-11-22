RUS = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ")
ENG = list("ABCDEFGHIJKLNMOPQRSTUVWXYZ")
a, b = input(), int(input())
try:
    if a == "RUS":
        print(f"Буква {RUS[b - 1]} стоит в алфавите RUS под номером {b}.")
    else:
        print(f"Буква {ENG[b - 1]} стоит в алфавите ENG под номером {b}.")
except IndexError:
    if a == "RUS":
        print(f"Буквы под номером {b} в алфавите RUS нет.")
    else:
        print(f"Буквы под номером {b} в алфавите ENG нет.")
        