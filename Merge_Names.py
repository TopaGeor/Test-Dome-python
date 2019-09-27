#3. Merge Names
def unique_names(names1, names2):
    ls = []
    for i in names1:
        if i not in ls:
            ls.append(i)

    for i in names2:
        if i not in ls:
            ls.append(i)
    return ls

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia