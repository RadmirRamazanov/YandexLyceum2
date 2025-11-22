with open("numbers.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    nums = {}
    c = 1
    for i in lines:
        i = i.split()
        if len(set(i)) == 4:
            h = {}
            num = ""
            lst = []
            for j in i:
                if j not in h:
                    h[j] = 1
                else:
                    h[j] += 1
            for k in h.keys():
                if h[k] == 3:
                    num = k
            if num != "":
                int_lst = []
                for j in i:
                    if j != num:
                        lst.append(int(j))
                    int_lst.append(int(j))
                if sum(lst) / 3 > int(num):
                    if max(int_lst) % min(int_lst) != 0:
                        nums[c] = sum(int_lst)
        c += 1
    print(sorted(nums.items(), key=lambda item: item[1])[0][0])
