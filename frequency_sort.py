items = [4, 6, 2, 2, 6, 4, 4, 4]


def frequency_sort(items):
    pos = 0
    pos1 = 0
    new_list = []
    counted = []
    result = []
    if len(items) == 0:
        result = items
    else:
        for i in items:
            if i not in new_list:
                new_list.append(i)
        for n in new_list:
            counter = items.count(new_list[pos])
            pos += 1
            counted.append(counter)
        zipped = zip(new_list, counted)
        zipped_list = list(zipped)
        res = sorted(zipped_list, key=lambda x: x[1], reverse=True)
        number1, number2 = zip(*res)
        for c in number1:
            result += [c] * number2[pos1]
            pos1 += 1

    return result


print(frequency_sort(items))
