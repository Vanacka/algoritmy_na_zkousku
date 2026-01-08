# Poradi vsech dlouhych cifer v seznamu je zadavano od predu,
# neboli cifra s nejmensi hodnotou v celkovem zapisu cisla bude v poli na 0 pozici
def scitani(a, b):
    prenos = 0
    c = []
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        cislo = a[i] + b[i] + prenos
        prenos = cislo // 10
        c.insert(0, cislo % 10)
    for i in range(len(b), len(a)):
        cislo = a[i] + prenos
        prenos = cislo // 10
        c.insert(0, cislo % 10)
    if prenos > 0:
        c.insert(0, prenos)
    return c


def odcitani(a, b):
    prenos = 0
    c = []
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        if a[i] == 0:
            cislo = 10 - b[i] - prenos
            prenos = 1
        elif a[i] < b[i] + prenos:
            cislo = 10 + a[i] - b[i] - prenos
            prenos = 1
        else:
            cislo = a[i] - b[i] - prenos
            prenos = 0
        c.insert(0, abs(cislo))
    for i in range(len(b), len(a)):
        if a[i] == 0:
            cislo = 10 - prenos
            prenos = 1
        else:
            cislo = a[i] - prenos
            prenos = 0
        c.insert(0, abs(cislo))
    if c[0] == 0:
        c.pop(0)
    return c


def nasobeni(a, b):
    prenos = 0
    c = []
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        for j in range(len(a)):
            cislo = (a[j] * b[i]) + prenos
            prenos = cislo // 10
            if len(c) == 0:
                c.append(cislo % 10)
            elif len(c) - 1 < i + j:
                c.insert(i + j, cislo % 10)
                prenos = cislo // 10
                if prenos > 0:
                    c.insert(i + j + 1, prenos)
                    prenos = 0
            else:
                c[i + j] += cislo % 10
                if c[i + j] >= 10:
                    prenos += c[i + j] // 10
                    c[i + j] %= 10

    if prenos > 0:
        c.append(prenos)
    return list(reversed(c))

a = []
b = []
cis_a = "8120" #"1209"
cis_b = "3404" #"1030454"
for cifra in cis_a:
    a.insert(0, int(cifra))
for cifra in cis_b:
    b.insert(0, int(cifra))

print(scitani(a, b))
print(odcitani(a, b))
print(nasobeni(a, b))