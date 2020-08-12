# Function return median of given list

def median(items):
    sorted_items = sorted(items)
    index = len(sorted_items) // 2
    if len(sorted_items) % 2 == 0:
        med = (sorted_items[index] + sorted_items[(index - 1)]) / 2
    else:
        med = sorted_items[index]

    return med



