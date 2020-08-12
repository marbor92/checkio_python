# Function sorts the numbers in an array without changing the position of zeros.


def except_zero(elements):
    index = [i for i in range(len(elements)) if elements[i] == 0]
    elements = [elem for elem in elements if elem != 0]
    ans = sorted(elements)
    for i in index:
        ans.insert(i, 0)

    return ans

