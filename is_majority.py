# Function checks if the majority of elements are true.

def is_majority(items: list) -> bool:
    t = items.count(True)
    f = items.count(False)
    if len(items) == 0 or f == t or f > t:
        return False
    else:
        return True
