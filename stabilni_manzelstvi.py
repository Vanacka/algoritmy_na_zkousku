def stabilni_par(seznamy_muzu, seznamy_zen, seznam_muzu, seznam_zen):
    seznam_zasnub = {}
    while True:
        for muz, nezadany in seznam_muzu.items():
            if nezadany:
                for i, (zena, zkousel) in enumerate(seznamy_muzu[muz]):
                    volna = seznam_zen[zena]
                    seznamy_muzu[muz][i] = (zena, True)
                    if not zkousel and volna:
                        seznam_zasnub[muz] = zena
                        seznam_muzu[muz] = False
                        seznam_zen[zena] = False
                        break
                    elif not zkousel and not volna:
                        obraceny_seznam_zasnub = {v: k for k, v in seznam_zasnub.items()}
                        snoubenec = obraceny_seznam_zasnub[zena]
                        seznam = seznamy_zen[zena]
                        body_snoubenec, body_muz = 0, 0
                        for chlap, body in seznam:
                            if chlap == snoubenec:
                                body_snoubenec = body
                            elif chlap == muz:
                                body_muz = body
                        if body_snoubenec < body_muz:
                            seznam_zasnub[muz] = zena
                            seznam_zasnub.pop(snoubenec)
                            seznam_muzu[snoubenec] = True
                            seznam_muzu[muz] = False
                        break
        if not any(seznam_muzu.values()):
            return seznam_zasnub


seznamy_muzu = {
    1: [("A", False), ("B", False), ("C", False)],
    2: [("B", False), ("C", False), ("A", False)],
    3: [("C", False), ("A", False), ("B", False)]
}
seznamy_zen = {
    "A": [(2, 3), (3, 2), (1, 1)],
    "B": [(3, 3), (1, 2), (2, 1)],
    "C": [(1, 3), (2, 2), (3, 1)]
}
seznam_muzu = {
    1: True,
    2: True,
    3: True
}
seznam_zen = {
    "A": True,
    "B": True,
    "C": True
}

print(stabilni_par(seznamy_muzu, seznamy_zen, seznam_muzu, seznam_zen))
