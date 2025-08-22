def rem(lst, word):
    n = []
    for item in lst:
        if item != word:
            n.append(item)
    return n

lst = ["Mudasir", "mubashir", "ali", "mu"]

print(rem(lst, "an"))
