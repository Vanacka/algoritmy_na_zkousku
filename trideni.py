def selection_sort(a):
    for i in range(len(a) - 1):
        k = i
        for j in range(i + 1, len(a)):
            if a[j] < a[k]:
                k = j
        if k > i:
            a[i], a[k] = a[k], a[i]
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        # vkladame cislo z pozice i
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a


def bubble_sort(a):
    vymena = len(a) - 1
    while vymena > 0:
        pruchod = vymena  # kam az prochazime seznam
        vymena = 0
        for j in range(pruchod):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                vymena = j  # misto posleni vymeny
    return a


def merge_sort_iterativni(a):
    n = len(a)  # Delka vstupniho seznamu
    temp = [None] * n  # Alokuje pomocny seznam

    # Postupne sleva sousedni useky delek 1, 2, 4, ...
    usek = 1
    while usek < n:
        for zacatek in range(0, n - usek, 2 * usek):
            stred = zacatek + usek - 1
            konec = min(stred + usek, n - 1)
            merge_iterativni(a, zacatek, stred, konec, temp)
        usek *= 2


# Sleje a[zac...stred] s a[stred + 1...kon] do a[zac...kon] pomoci temp[zac...kon]
def merge_iterativni(a, zac, stred, kon, temp):
    i = zac
    j = stred + 1
    k = zac

    # Sleje a[zac...stred] s a[stred + 1...kon] do temp
    while i <= stred and j <= kon:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    # Zapise do temp zbytek prvniho useku
    if i <= stred:
        temp[k:kon + 1] = a[i: stred + 1]
    # Zapise do temp zbytek druheho useku
    else:
        temp[k:kon + 1] = a[j: kon + 1]
    # Vysledek zkopiruje zpet do seznamu a
    a[zac:kon + 1] = temp[zac:kon + 1]


def merge_sort_rekurze(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    return merge_rekurze(merge_sort_rekurze(s[:mid]), merge_sort_rekurze(s[mid:]))


def merge_rekurze(x, y):
    i = j = 0
    out = []

    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            out.append(x[i])
            i += 1
        else:
            out.append(y[j])
            j += 1
    if i < len(x):
        out.extend(x[i:])
    if j < len(y):
        out.extend(y[j:])
    return out


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    vlevo = []
    stred = []
    vpravo = []
    for i in a:
        if i < pivot:
            vlevo.append(i)
        elif i > pivot:
            vpravo.append(i)
        else:
            stred.append(i)
    return quick_sort(vlevo) + stred + quick_sort(vpravo)


def quick_sort_na_miste(a, zac, kon):
    i = zac
    j = kon
    pivot = a[(i + j) // 2]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        elif i == j:
            i += 1
            j -= 1
    if zac < j:
        quick_sort_na_miste(a, zac, j)
    if i < kon:
        quick_sort_na_miste(a, i, kon)
    return a


def heap_sort(a):
    pass


def counting_sort(a, d, h):
    c = [0] * (h - d + 1)

    for x in a:
        c[x - d] += 1

    b = []
    for i in range(h - d):
        for j in range(c[i]):
            b.append(i + d)
    return b


cisla40 = [23, 4, 15, 38, 1, 19, 40, 7, 32, 11, 2, 28, 5, 34, 10, 25, 39, 12, 6, 33, 18, 22, 9, 31, 14, 29, 3, 37, 20,
           36, 8, 26, 17, 30, 13, 21, 35, 24, 16, 27]
cisla10 = [4, 9, 1, 6, 10, 3, 8, 2, 5, 7]
data_counting = [4, 2, 2, 8, 3, 3, 1, 0, 4, 2, 1, 0, 8, 3, 5, 4, 2, 5, 0, 1]
print(quick_sort_na_miste(cisla10, 0, len(cisla10) - 1))
print(counting_sort(data_counting, 0, 8))
