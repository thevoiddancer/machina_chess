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

def crtanje_ploče() -> None:  # za sada ništa od ove funkcije, ali bi bila potrebna
    pass

def odredi_figuru(igrač, tip, lokacija) -> Figura:
    """
    Funkcija koja pogleda objekt igrača i onda vrati objekt figure koja se nalazi na tom mjestu.
    """
    pass

def unos_poteza(igrač) -> tuple[str, str, str]:
    """
    Funkcija kojom igrač unosi svoj potez. Potez se treba raastaviti na:
    - inicijal figure
    - polazište
    - odredište
    Funkcija nakon toga provjeri ima li igrač figuru na tom mjestu korištenjem metode
    .postoji_figura() na objektu Igrač.
    Ukoliko igrač nema figuru na tom mjestu, ponovo ga se pita za unos.
    """
    potez = input(f'{igrač.ime} unesi potez u obliku inicijal-polazište-odredište (npr S-A1-B3): ')
    pass

def legalan_potez(igrač, tip, polazište, odredište) -> bool:
    """
    Funkcija koja radi cjelokupnu provjeru je li potez moguć. Da to napravi mora se provjeriti 3
    stvari:
    - je li taj potez uopće legalan (pretpostavka prazne ploče, bez ikakvih figura)
    - smeta li neka figura na putu od polazišta do odredišta (osim za skakača)
        - za ovo bi bilo dobro napraviti funkciju koja će samo vraćati polja na tom putu
    - je li na odredištu protivnička figura

    Za legalnost poteza ignoriramo ploču i ostale figure.
    Za smetanje na putu gledamo i jedne i druge figure
        - ako smeta protivnička figura nećemo ništa posebno napraviti, neka igrač pazi na figure
    Ako smeta protivnička figura automatski ju jedemo.
    """
    pass

def pojedi_figuru(odredište, ploča):
    """
    Funkcija koja "pojede" protivničku figuru. Figuru je potrebno maknuti sa ploče i iz popisa
    figura koje se nalaze u objektu igrača. Mora vratiti promijenjenu ploču i objekt drugog igrača.
    """
    pass

def pomakni_figuru(figura, polazište, odredište, ploča):
    """
    Funkcija koja samo promjeni mjesto figuri. Potrebno je promijeniti lokaciju figure na objektu
    figure, ali i pomaknuti figuru na ploči. Mora vratiti promijenjenu ploču i objekt igrača.
    """
    pass

def napad(figura, polazište, odredište, ploča) -> bool:
    """
    Funkcija koja provjeri je li na odredištu protivnička figura. Vraća True/False
    """
    pass

def main() -> None:
    """
    Funkcija koja povezuje sve funkcije i stvara potpunu igru šaha.
    """
    igrači, ploča = postavljanje_ploče()

    # while True:
    na_potezu = 0
    for _ in range(3):  # zamijeniti beskonačnom petljom kad bude gotovo
        crtanje_ploče()

        igrač = igrači[na_potezu]
        protivnik = igrači[1 - na_potezu]
        tip, polazište, odredište = unos_poteza(igrač)
        figura = odredi_figuru(igrač, tip, polazište)

        if legalan_potez(figura, polazište, odredište):
            if napad(figura, polazište, odredište, ploča):
                ploča, protivnik = pojedi_figuru(odredište, ploča)
            ploča, igrač = pomakni_figuru(figura, polazište, odredište, ploča)

        igrači[na_potezu] = igrač
        igrači[1 - na_potezu] = protivnik
        na_potezu = 1 - na_potezu  # za 0 ovo bude 1, za 1 bude 0 = alterniranje 0-1-0-1...

    pass

main()