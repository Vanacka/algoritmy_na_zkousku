def bin_to_dec(x):
    vysledek = 0
    for znak in x:
        vysledek = vysledek * 2 + int(znak)
    return vysledek


def dec_to_bin(x):
    vysledek = []
    while x != 0:
        vysledek.insert(0, x % 2)
        x //= 2
    return vysledek


def hex_to_dec(x):
    cifry = "0123456789ABCDEF"
    vysledek = 0
    for znak in x:
        vysledek = vysledek * 16 + cifry.index(znak)
    return vysledek


def dec_to_hex(x):
    vysledek = []
    cifry = "0123456789ABCDEF"
    while x != 0:
        zbytek = x % 16
        cislo = cifry[zbytek]
        vysledek.insert(0, cislo)
        x //= 16
    return vysledek


def mocnina(x, n):
    v = 1
    while n > 0:
        if n % 2 == 1:
            v *= x
        x *= x
        n //= 2
    return v


print(bin_to_dec("101"))
for i in dec_to_bin(4):
    print(f"{i}", end="")
print()
print(hex_to_dec("1F"))

for i in dec_to_hex(31):
    print(f"{i}", end="")
print()

print(mocnina(3, 1))
