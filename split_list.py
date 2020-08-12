# Function splits list into two lists.
# If it has an odd amount of elements, then the first array should have more elements.
# If it has no elements, then two empty arrays should be returned.


def split_list(items):
    if len(items) % 2 == 0:
        index = len(items) // 2
    else:
        index = (len(items) // 2) + 1
    first_list = items[:index]
    second_list = items[index:]
    splitted = [first_list, second_list]
    return splitted



