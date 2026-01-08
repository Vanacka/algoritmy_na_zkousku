def nsd(x: int, y: int) -> int:
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def nsd2(x: int, y: int) -> int:
    while y > 0:
        z = x % y
        x = y
        y = z
    return x

print(nsd2( 324, 396))