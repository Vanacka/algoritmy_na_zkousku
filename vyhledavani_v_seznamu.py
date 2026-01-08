def vyhledavani_cyklem(x, seznam):
    i = 0
    while seznam[i] != x and i < len(seznam):
        i += 1
    if i == len(seznam):
        print("Neni tam")
    else:
        print("Je na pozici", i)


def vyhledavani_zarazkou(x, seznam):
    seznam.append(x)
    i = 0
    while seznam[i] != x:
        i += 1
    seznam.pop()

    if i == len(seznam):
        print("Neni tam")
    else:
        print("Je na pozici", i)


def bin_vyhledavani(x, seznam):
    i = 0                   # Zacatek useku
    j = len(seznam) - 1     # Konec useku
    k = (i + j) // 2        # Stred useku
    while seznam[k] != x and i <= j:
        if x >= seznam[k]:
            i = k + 1
        else:
            j = k - 1
        k = (i + j) // 2
    if x == seznam[k]:
        print("Je na pozici", i)
    else:
        print("Neni tam")


def odmocnina(n):
    eps = 0.0001        # Zvolena presnost vypoctu
    if n > 1:
        dolni, horni = 1, n
    else:
        dolni, horni = 0, 1
    stred = (dolni + horni) / 2
    while horni - dolni >= eps:
        if stred**2 < n:
            dolni = stred
        else:
            horni = stred
        stred = (dolni + horni) / 2
    return stred



seznam = [3, 54, 2, 3, 98, 23, 55, 223, 1, 5, 643, 5, 234, 664, 521, 234, 3, 5, 7, 8, 34, 9, 0, 1, 2123, 23, 67, 19, 69]
vyhledavani_cyklem(69, seznam)
vyhledavani_zarazkou(3000, seznam)
bin_vyhledavani(223, sorted(seznam))
print(f"{odmocnina(900): 0.3f}")

