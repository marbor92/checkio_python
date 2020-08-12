# Function finds the N-th power of the element in the array with the index N.
# If N is outside of the array, then return -1.

def index_power(my_list, power) -> int:
    pos = 0
    index = []
    for i in my_list:
        index.append(pos)
        pos += 1
    if power not in index:
        ans = -1
    else:
        ans = my_list[power] ** power

    return ans
