numbers = [3, 4, 11, 13, 11, 4, 4, 7, 3]


def frequency_sorting(numbers):
    new_list = sorted(numbers)
    y = sorted(new_list, key=lambda x: new_list.count(x), reverse=True)

    return y

print(frequency_sorting(numbers))










