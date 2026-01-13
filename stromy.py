class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu"""

    def __init__(self, data=None, levy=None, pravy=None):
        self.data = data  # číslo uložené ve vrcholu (nemělo by se měnit)

        self.levy = levy  # levé dítě
        self.pravy = pravy  # pravé dítě


def cena(koren: VrcholBinStromu) -> int:
    """
    koren : kořen zadaného binárního stromu
    vrátí : cenu zadaného stromu

    """
    if koren is None:
        return 0

    def dfs(v: VrcholBinStromu, hladina: int) -> int:
        # Uzel neexistuje vratime proto nulovou hodnotu
        if v is None:
            return 0
        # Jsme v listu vypocita jeho cenu
        if v.levy is None and v.pravy is None:
            return hladina * v.data
        # Vrati ceny listu z leveho a praveho podstromu
        return dfs(v.levy, hladina + 1) + dfs(v.pravy, hladina + 1)

    return dfs(koren, 0)


def nv(koren: VrcholBinStromu):
    """
    koren : kořen binárního stromu
    vrátí : nevyváženost zadaného stromu
    """
    if koren is None:
        return 0

    def nevyvazenost(v: VrcholBinStromu) -> tuple[int, int]:
        if v is None:
            return 0, 0

        if v.levy is None and v.pravy is None:
            return 1, 0
        else:
            levy_podstrom, balance_l = nevyvazenost(v.levy)
            pravy_podstrom, balance_p = nevyvazenost(v.pravy)
            max_balance = max(balance_l, balance_p)
            balance = abs(levy_podstrom - pravy_podstrom)
            if balance > max_balance:
                max_balance = balance
            return levy_podstrom + pravy_podstrom + 1, max_balance

    return nevyvazenost(koren)[1]


def pocetOp(koren: VrcholBinStromu) -> tuple[int, int]:
    """
    koren : kořen zadaného binárního stromu
    vrátí : maximální počet operátorů v podvýrazu bez dělení
    """
    if koren.levy is None:
        return 0, 0
    l_pocet, l_max = pocetOp(koren.levy)
    p_pocet, p_max = pocetOp(koren.pravy)
    max_pocet = max(l_max, p_max)
    if koren.data == "/":
        return 0, max_pocet
    pocet = l_pocet + p_pocet + 1
    if pocet > max_pocet:
        max_pocet = pocet
    return pocet, max_pocet


def hladina(koren: VrcholBinStromu, x: int):
    """
    koren : kořen zadaného binárního stromu
    x     : zadané ohodnocení hledaného vrcholu
    vrátí : seznam čísel vrcholů na hladině obsahující x
    """

    def najdi_hladinu_x(v: VrcholBinStromu, hladina: int, x: int) -> int:
        if v is None:
            return -1
        if v.data == x:
            return hladina
        levy = najdi_hladinu_x(v.levy, hladina + 1, x)
        pravy = najdi_hladinu_x(v.pravy, hladina + 1, x)
        return max(levy, pravy)

    hladina_x = najdi_hladinu_x(koren, 0, x)
    akt_hladina = 0
    prvky_na_hladine = []
    fronta = [koren]

    if hladina_x < 0:
        return prvky_na_hladine

    while len(fronta) > 0:
        prvku_na_hladine = len(fronta)
        for i in range(prvku_na_hladine):
            if akt_hladina == hladina_x:
                prvky_na_hladine.append(fronta[0].data)
            else:
                if fronta[i].levy is not None:
                    fronta.append(fronta[0].levy)
                if fronta[i].pravy is not None:
                    fronta.append(fronta[0].pravy)
            fronta.pop(0)
        if len(prvky_na_hladine) > 0:
            break
        akt_hladina += 1
    return prvky_na_hladine


def max_listy(koren: VrcholBinStromu):
    def posl_hladina(v: VrcholBinStromu, akt_hladina: int):
        if v is None:
            return 0
        if v.levy is None and v.pravy is None:
            return akt_hladina
        return max(posl_hladina(v.levy, akt_hladina + 1), posl_hladina(v.pravy, akt_hladina + 1))

    max_hladina = posl_hladina(koren, 0)
    fronta = [koren]
    aktualni_hladina = 0

    while len(fronta) > 0:
        pocet_na_hladine = len(fronta)
        for i in range(pocet_na_hladine):
            if aktualni_hladina == max_hladina:
                print(fronta[0].data)
            else:
                if fronta[0].levy is not None:
                    fronta.append(fronta[0].levy)
                if fronta[0].pravy is not None:
                    fronta.append(fronta[0].pravy)
            fronta.pop(0)
        aktualni_hladina += 1


def maxcena(koren: VrcholBinStromu):
    """
    koren : kořen zadaného binárního stromu
    vrátí : dvojici čísel (m,d), kde m je maximální součet čísel na cestě z kořenu do libovolného vrcholu stromu a
            a d je délka této cesty (je-li jich více, tak nejkratší)
    """

    def lepsi_kandidat(k1, k2):
        s1, d1 = k1
        s2, d2 = k2

        if s1 > s2:
            return k1
        if s2 > s1:
            return k2

        if d1 < d2:
            return k1
        else:
            return k2

    def hodnota(v: VrcholBinStromu, hloubka: int, soucet: int):
        if v is None:
            return None
        muj_soucet = soucet + v.data
        moje_cesta = (muj_soucet, hloubka)
        nejlepsi = moje_cesta

        if v.levy is not None:
            leva = hodnota(v.levy, hloubka + 1, muj_soucet)
            nejlepsi = lepsi_kandidat(leva, moje_cesta)
        if v.pravy is not None:
            prava = hodnota(v.pravy, hloubka + 1, muj_soucet)
            nejlepsi = lepsi_kandidat(prava, moje_cesta)
        return nejlepsi
    return hodnota(koren, 0, 0)


def vyska(koren: VrcholBinStromu, h: bool):
    """
    koren : kořen zadaného binárního stromu
    h     : True či False
    vrátí : maximální výšku podstromu reprezentujícího podvýraz, který se vyhodnotí na hodnotu h
    """
    def hloubka(v: VrcholBinStromu, hodnota: bool, hladinka: int):
        moje_hodnota = True
        if v is None:
            return -1, -1, -1
        if v.levy is None and v.pravy is None:
            moje_hodnota = v.data
            if moje_hodnota == hodnota:
                return hladinka, 0, moje_hodnota
            return hladinka, -1, moje_hodnota
        l_max_hladinka, l_max_vyska_podstromu, l_hodnota = hloubka(v.levy, hodnota, hladinka + 1)
        p_max_hladinka, p_max_vyska_podstromu, p_hodnota = hloubka(v.pravy, hodnota, hladinka + 1)
        max_hladina_v_podstromu = max(l_max_hladinka, p_max_hladinka)
        max_vyska_podstromu = max(l_max_vyska_podstromu, p_max_vyska_podstromu)
        if v.levy is not None:
            if v.data == "not":
                moje_hodnota = not l_hodnota
                if moje_hodnota == hodnota:
                    max_vyska_podstromu = l_max_hladinka - hladinka
                else:
                    max_vyska_podstromu = l_max_vyska_podstromu
            elif v.data == "and":
                moje_hodnota = l_hodnota and p_hodnota
                if moje_hodnota == hodnota:
                    max_vyska_podstromu = max_hladina_v_podstromu - hladinka
            else:
                moje_hodnota = l_hodnota or p_hodnota
                if moje_hodnota == hodnota:
                    max_vyska_podstromu = max_hladina_v_podstromu - hladinka
        return max_hladina_v_podstromu, max_vyska_podstromu, moje_hodnota
    return hloubka(koren, h, 0)


vrchol = VrcholBinStromu(
    2,
    VrcholBinStromu(
        1,
        None,
        VrcholBinStromu(
            8,
            VrcholBinStromu(6, None, None),
            VrcholBinStromu(7, None, None)
        )
    ),
    VrcholBinStromu(
        4,
        VrcholBinStromu(3, None, None),
        VrcholBinStromu(5, None, None)
    )
)

#print(nv(vrchol))

vrchol_operace = VrcholBinStromu(
    "-",
    VrcholBinStromu(
        "+",
        VrcholBinStromu(
            "*",
            VrcholBinStromu(
                "/",
                VrcholBinStromu(1, None, None),
                VrcholBinStromu(3, None, None)
            ),
            VrcholBinStromu(2, None, None)
        ),
        VrcholBinStromu(
            "+",
            VrcholBinStromu(
                "-",
                VrcholBinStromu(9, None, None),
                VrcholBinStromu(3, None, None)
            ),
            VrcholBinStromu(2, None, None)
        )
    ),
    VrcholBinStromu(
        "+",
        VrcholBinStromu(
            "*",
            VrcholBinStromu(5, None, None),
            VrcholBinStromu(
                "-",
                VrcholBinStromu(8, None, None),
                VrcholBinStromu(4, None, None)
            )
        ),
        VrcholBinStromu(6, None, None)
    )
)

#print(max(pocetOp(vrchol_operace.levy), pocetOp(vrchol_operace.pravy))[1])

#print(hladina(vrchol, 9))

#print(maxcena(vrchol))

vrchol_logika = VrcholBinStromu(
    "or",
    VrcholBinStromu(
        "not",
        VrcholBinStromu(
            "and",
            VrcholBinStromu(
                "or",
                VrcholBinStromu(True, None, None),
                VrcholBinStromu(False, None, None)
            ),
            VrcholBinStromu(
                "and",
                VrcholBinStromu(True, None, None),
                VrcholBinStromu(True, None, None)
            )
        ),
        None
    ),
    VrcholBinStromu(
        "or",
        VrcholBinStromu(
            "and",
            VrcholBinStromu(False, None, None),
            VrcholBinStromu(
                "or",
                VrcholBinStromu(False, None, None),
                VrcholBinStromu(True, None, None)
            )
        ),
        VrcholBinStromu(
            "not",
            VrcholBinStromu(True, None, None),
            None
        )
    )
)

print(vyska(vrchol_logika, True))