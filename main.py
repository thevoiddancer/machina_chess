from objekti import Igrač, Figura

def postavljanje_ploče() -> tuple[list[Igrač], dict[str, Figura]]:
    igrač1 = input('Unesi ime igrača 1: ')
    igrač2 = input('Unesi ime igrača 2: ')
    prvi = input('Koji igrač je bijeli (1/2): ')
    if prvi == '1':
        igrači = [
            Igrač(igrač1, 'bijelo'),
            Igrač(igrač2, 'crno'),
        ]
    elif prvi == '2':
        igrači = [
            Igrač(igrač2, 'bijelo'),
            Igrač(igrač1, 'crno'),
        ]

    ploča = {}
    for igrač in igrači:
        for figura in igrač.figure:
            ploča[figura.položaj_str] = figura

    return igrači, ploča

def main() -> None:
    igrači, ploča = postavljanje_ploče()
    pass

main()