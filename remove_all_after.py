# Remove all of the elements after the given one from list.


def remove_all_after(items: list, border: int):
    if border in items:
        index = items.index(border)
        ans = items[:(index+1)]
    elif len(items) == 0:
        ans = []
    elif border not in items:
        ans = items

    return ans




