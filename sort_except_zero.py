elements = [5, 3, 0, 0, 4, 1, 4, 0, 7]


def except_zero(elements):
    index = [i for i in range(len(elements)) if elements[i] == 0]
    elements = [elem for elem in elements if elem != 0]
    ans = sorted(elements)
    for i in index:
        ans.insert(i, 0)

    return ans

print(except_zero(elements))