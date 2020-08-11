items = [1, 2, 3, 4, 5, 6]


def split_list(items):
    if len(items) % 2 == 0:
        index = len(items) // 2
    else:
        index = (len(items) // 2) + 1
    first_list = items[:index]
    second_list = items[index:]
    splitted = [first_list, second_list]
    return splitted


print(split_list(items))
