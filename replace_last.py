items = [1, 2, 3, 5]


def replace_last(items):
    new_list = []
    if len(items) >= 1:
        new_list.append(items[-1])
        for i in items:
            new_list.append(i)
        new_list = new_list[:-1]
        return new_list
    else:
        return items

print(replace_last(items))

