my_list = [1, 2, 3, 4]
power = 7


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

print(index_power(my_list, power))