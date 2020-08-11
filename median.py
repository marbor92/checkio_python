items = [3, 1, 2, 5, 3]


def median(items):
    sorted_items = sorted(items)
    index = len(sorted_items) // 2
    if len(sorted_items) % 2 == 0:
        med = (sorted_items[index] + sorted_items[(index - 1)]) / 2
    else:
        med = sorted_items[index]

    return med


print(median(items))
