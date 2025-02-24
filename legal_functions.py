from helper_functions import koord_to_tuple, tuple_to_koord


def legal_pijun(figura: dict[str, str], cilj: str) -> bool:
    """
    Funkcija koja provjerava je li najavljeni pomak pijuna legalan. Pravila koja prati su:
    - nije dopušten pomak u stranu
    - nije dopušteno ostati na mjestu
    - nije dopušteno pomak veći od 2 polja
    - pomak od 2 polja je dopušten samo sa početne pozicije
    - pomak od 1 polja je dopušten samo "naprijed", ovisno o boji
    Funkcija ne testira mogućnost da se "pojede" protivnička figura. To je potrebno dodati.
    Funkcija ne mijenja položaj figure, samo javlja je li novi položaj legalan.

    Parameters
    ----------
    figura : dict[str, str]
        Dictionary koji nosi podatke o figuri - boja, tip i mjesto.
    cilj : str
        Šahovski zapis položaja
    
    Returns
    -------
    bool
        Odgovor je li najavljen potez dopušten
    
    Raises
    ------
    None
    """
    polazište = koord_to_tuple(figura['mjesto'])
    odredište = koord_to_tuple(cilj)

    # Ako je kretanje u stranu automatski False
    if polazište[0] != odredište[0]:
        return False
    # Ako je polazište i odredište isto
    # Gornja grana garantira da su 1. koordinate nadalje uvijek iste
    elif polazište[1] == odredište[1]:
        return False
    # Potez više od 2 je uvijek nedopušten
    elif abs(odredište[1] - polazište[1]) > 2:
        return False
    # Potez od točno 2 je dopušten u jednom slučaju
    elif abs(odredište[1] - polazište[1]) == 2:
        # Startni red bijelih pijuna je 2
        if figura['boja'] == 'bijelo' and polazište[1] == 2 and odredište[1] == 4:
            return True
        # Startni red crnih pijuna je 7
        elif figura['boja'] == 'crno' and polazište[1] == 7 and odredište[1] == 5:
            return True
        # Inače je pomak od 2 koraka nedopušten
        else:
            return False
    # Ostale su samo kombinacije jednog koraka
    else:
        # Bijele mogu ići samo naprijed
        if figura['boja'] == 'bijelo' and odredište[1] == polazište[1] + 1:
            return True
        # Crne mogu ići samo nazad
        elif figura['boja'] == 'crno' and odredište[1] == polazište[1] - 1:
            return True
        else:
            return False

# Ovdje ostale funkcije
def legal_lovac(figura:dict[str, str], cilj:str)-> bool:
    """
    Funkcija provjerava je li najavljeni pomak lovca legalan. Pravila koja prati su:
    -nije dopušten pomak u naprijed
    -nije dopušteno ostati na mjestu
    -smije se pomaknuti za neograničeno do kraja ploče samo u dijagonalu, ovisno o boji
    Funkcija ne testira mogućnost da se "pojede" protivnička figura. To je potrebno dodati.
    Funkcija ne mijenja položaj figure, samo javlja je li novi položaj legalan.

    Parameters
    ----------
    figura : dict[str, str]
        Riječnik koji nosi podatke o figuri- boja, tip i mjesto.
    cilj : str
        Šahovski zapis položaja
    
    Returns
    -------
    bool
        Odgovor je li najavljen potez dopušten
    
    Raises
    ------
    None
    """
    polazište = koord_to_tuple(figura['mjesto'])
    odredište = koord_to_tuple(cilj)

   

     # Ako je polazište i odredište isto
    if polazište == odredište:
        return False

    # Razlika u stupcu i retku
    dx = abs(polazište[0] - odredište[0])
    dy = abs(polazište[1] - odredište[1])

    # Lovac se smije kretati samo dijagonalno (isti broj koraka po x i y)
    if dx != dy:
        return False

    # Provjera boje polja (bijeli lovac -> bijela polja, crni -> crna)
    suma = odredište[0] + odredište[1]
    if figura['boja'] == 'bijelo' and suma % 2 != 0:
        return False
    elif figura['boja'] == 'crno' and suma % 2 == 0:
        return False

    return True


LEGAL_FUNCITONS = {
    'pijun': legal_pijun,
    'lovac': legal_lovac,
    # 'konj': legal_konj,
    # ...
}

def is_move_legal(figura: dict[str, str], cilj) -> bool:
    tip = figura['tip']
    legal_funkcija = LEGAL_FUNCITONS[tip]
    dopušteno = legal_funkcija(figura, cilj)
    return dopušteno