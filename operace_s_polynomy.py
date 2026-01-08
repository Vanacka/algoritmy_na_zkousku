def hornerovo_schema(polynom, x):
    '''
    vypocet hodnoty polynomu Hornerovym schematem
    polynom: seznam s koeficienty polynomu polynom[i] * x^i
    x: bod z def oboru
    '''
    h = 0
    for i in range(len(polynom) - 1, -1, -1):
        h = h * x + polynom[i]
    return h

def soucet_pol(a, b):
    c = []
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(b)):
        c.append(a[i] + b[i])
    for i in range(len(b), len(a)):
        c.append(a[i])
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return list(reversed(c))


def soucin_pol(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c


a = list(reversed([-1, 3, 4, 3, 7, 0, -2])) # -x^6 + 3x^5 + 4x^4 + 3x^3 + 7x^2 - 2
b = list(reversed([2, 0, 11, 3, -3])) # 2x^4 + 11x^2 + 3x - 3
x = 5


print(f"Hodnota polynomu v bode {x} je {hornerovo_schema(list(reversed(a)), x)}")
print(f"Soucet dvou polynomu {list(reversed(a))} a {list(reversed(b))} je {soucet_pol(a, b)}")
print(f"Soucin dvou polynomu {list(reversed(a))} a {list(reversed(b))} je {soucin_pol(a, b)}")