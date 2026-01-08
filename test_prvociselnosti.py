import math

def je_prvocislo(x):
    horni_hranice = int(math.sqrt(x)) + 1
    if x % 2 == 0:
        return  f"{x}: Neni prvocislo je sude"
    for i in range(3, horni_hranice, 2):
        if x % i == 0:
            return f"{x}: Neni prvocislo, {i} je jeho delitel"
    return f"{x}: Je prvnocislo"

def eratosthenovo_sito(n):
    prvocisla_v_rozsahu = []
    jsou_prvocisla = [True] * n
    jsou_prvocisla[0] = False
    jsou_prvocisla[1] = False

    # Zjisti co vsechno jsou prvocisla
    for i in range(2, n):
        if jsou_prvocisla[i]:
            for j in range(i*i, n, i):
                jsou_prvocisla[j] = False

    # Zapise vsechna prvocisla z rozsahu do seznamu
    for i in range(n):
        if jsou_prvocisla[i]:
            prvocisla_v_rozsahu.append(i)

    return prvocisla_v_rozsahu

print(je_prvocislo(5))
print(je_prvocislo(48))
print(je_prvocislo(3495872047))
print(je_prvocislo(3495345322394834773892837490092383047334237453466657657))

print(f"Vsechan prvocisla do cisla {100} jsou: {eratosthenovo_sito(100)}")