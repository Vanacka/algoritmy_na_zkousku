def rozklad_cis_na_cif(x):
    y = 0
    while x != 0:
        y += x % 10
        x //= 10
    return y


print(rozklad_cis_na_cif(34902))
