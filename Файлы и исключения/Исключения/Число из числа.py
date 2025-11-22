a = input()
new_a = ""
try:
    assert len(a) > 4, "There are not enough discharges."
    new_a += a[len(a) - 4:]
    for i in range(len(a) - 4):
        new_a += a[i]
    assert len(a) == len(str(int(new_a))), "The number has decreased."
    sm = 0
    for i in new_a:
        sm += int(i)
    assert (int(new_a) + sm) % 2 == 0, "Odd result."
    print(int(new_a) + sm)
except AssertionError as e:
    print(e)
    