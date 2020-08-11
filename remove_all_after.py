items = []
border = 8


def remove_all_after(items: list, border: int):
    if border in items:
        index = items.index(border)
        ans = items[:(index+1)]
    elif len(items) == 0:
        ans = []
    elif border not in items:
        ans = items

    return ans

print(remove_all_after(items,border))



