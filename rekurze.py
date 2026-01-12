def otoc():
    u = input("Znak: ")
    if u != " ":
        otoc()
    print(u)


def palindrom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrom(s[1:-1])


def fib(n, pole):
    if n == 0 or n == 1:
        return n
    else:
        if pole[n] == 0:
            pole[n] = fib(n - 1, pole) + fib(n - 2, pole)
        return pole[n]


def cislo(c, n, k):
    for i in range(1, n):
        c.append(i)
        if len(c) < k:
            cislo(c, n, k)
        else:
            print(c)
        c.pop()


def kombinace_bez_opak(c, n, k, p):
    for i in range(p, n):
        c.append(i)
        if len(c) < k:
            kombinace_bez_opak(c, n, k, p + 1)
        else:
            print(c)
        c.pop()


def kombinace_s_opak(c, n, k, p):
    for i in range(p, n):
        c.append(i)
        if len(c) < k:
            kombinace_s_opak(c, n, k, p)
        else:
            print(c)
        c.pop()


def doplneni_znamenek(cisla, soucet, vysledek, znamenka, zbytek_cisel, index):
    if zbytek_cisel == index:
        if soucet == vysledek:
            for i in range(len(cisla)):
                print(znamenka[i], end="")
                print(cisla[i], end="")
            print()
    else:
        znamenka.append("+")
        doplneni_znamenek(cisla, soucet + cisla[index], vysledek, znamenka, zbytek_cisel, index + 1)
        znamenka.pop()
        znamenka.append("-")
        doplneni_znamenek(cisla, soucet - cisla[index], vysledek, znamenka, zbytek_cisel, index + 1)
        znamenka.pop()


def rozklad(zbyva, pole, n):
    if zbyva == 0:
        if pole[0] != n:
            for i in pole[:-1]:
                print(i, end="")
                print("+", end="")
            print(f"{pole[-1]} = {n}")
    else:
        for i in range(zbyva, 0, -1):
            if len(pole) == 0 or i <= pole[-1]:
                pole.append(i)
                rozklad(zbyva - i, pole, n)
                pole.pop()


def hanoj(n, a, b, c):
    """"
    řešení úlohy o Hanojských věžích:
    přenášíme "n" kotoučů
    z kolíku "a" na kolík "b";
    třetí kolík "c" je pomocný
    """
    if n > 0:
        hanoj(n-1, a, c, b)
        print(str(a) + " -> " + str(b))
        hanoj(n-1, c, b, a)


s = []
string_palindrom = "kokotporooreptokok"
for p in string_palindrom:
    s.append(p)
print(palindrom(s))

pole = [0] * 201
print(fib(200, pole))

#c1 = []
#print(cislo(c1, 3, 4))

c2 = []
print(kombinace_s_opak(c2, 5, 3, 1))

cisla = [3, 5, 7, 9, 4, 2, 1]
doplneni_znamenek(cisla, 0, 15, [], len(cisla), 0)

rozklad(7, [], 7)

hanoj(3, 1, 2, 3)
