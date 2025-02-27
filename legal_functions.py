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

def legal_kula (figura:dict[str,str],cilj : str) -> bool:
    """
    Funkcija koja provjerava dali je potez topa legalan, a pravila koja prati su:
        - Top se može pomicati bilo koji broj slobodnih polja vodoravno ili uspravno.
        - Moze izvrsiti i rosadu sa kraljem.
        - Nije dopusteno ostati na mjestu.
        - Funkcija ne testira mogućnost da se "pojede" protivnička figura. To je potrebno dodati.
        - Funkcija ne mijenja položaj figure, samo javlja je li novi položaj legalan.
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
    polazište = koord_to_tuple(figura["mjesto"])
    odredište = koord_to_tuple(cilj)

    #Ako se figura krece samo po slovima a ne po brjevima (A1 -> D1)
    if polazište[0] != odredište[0] and polazište[1] == odredište[1]:
        return True
    #Ako se figura krece samo po brojevima a ne po slovima (A1 -> A7)
    if polazište[0] == odredište[0] and polazište[1] != odredište[1]:
        return True
    
    #Ako se figura nije pomaknula
    if polazište == odredište:
        return False


LEGAL_FUNCITONS = {
    'pijun': legal_pijun,
    # 'konj': legal_konj,
    "kula" : legal_kula
}

def is_move_legal(figura: dict[str, str], cilj) -> bool:
    tip = figura['tip']
    legal_funkcija = LEGAL_FUNCITONS[tip]
    dopušteno = legal_funkcija(figura, cilj)
    return dopušteno