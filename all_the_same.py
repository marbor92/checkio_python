elements = []


def all_the_same(elements):
    unique = []
    for i in elements:
        if i not in unique:
            unique.append(i)
    if len(unique) > 1:
        return False
    else:
        return True


print(all_the_same(elements))
