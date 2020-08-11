elements = []
size = 7
x = 0
ans = []


def chunking_by(elements, size):
    x = 0
    ans = []
    for i in range(x, len(elements), size):
        x=i
        ans.append(elements[x:x+size])

    return ans

print(chunking_by(elements, size))
