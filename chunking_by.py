# Function splits a list into smaller lists of the same size (chunks).

def chunking_by(elements, size):
    x = 0
    ans = []
    for i in range(x, len(elements), size):
        x=i
        ans.append(elements[x:x+size])

    return ans

