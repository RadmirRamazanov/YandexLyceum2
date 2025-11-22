a = [i for i in input().split("; ")]
all_words = []
words = {}
st = set()
for file in a:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        d = set()
        for i in lines:
            st.add(i)
            d.add(i)
        for i in d:
            all_words.append(i)
for i in st:
    words[i] = 0
for i in all_words:
    if i in words:
        words[i] += 1
for i in words.keys():
    if words[i] == 2:
        print(i[:-1])

