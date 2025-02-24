from helper_functions import koord_to_tuple, tuple_to_koord

def legal_kula(figura_kula: dict[str, str], cilj_kula: str, ploča: list[list]) -> bool:
    """
    Funkcija koja provjerava je li najavljeni pomak kule legalan. Pravila koja prati su:
    - Nije dopušteno ostati na mjestu
    - 1 korak naprjed
    - 1 korak nazad
    - 3 koraka naprjed
    - 3 koraka nazad
    - Nije dopušten pomak dijagonalno
    - Ako se na njenoj putanji nalazi protivnička figura, može je uzeti i zauzeti to polje.
    
    Parameters
    ----------
    figura_kula : dict[str, str]
        Dictionary koji nosi podatke o figuri - boja, tip i mjesto.
    cilj_kula : str
        Šahovski zapis položaja
        
    Returns
    -------
    bool
        Odgovor je li najavljen potez dopušten
    """
    
    polazište = koord_to_tuple(figura_kula['mjesto'])
    odredište = koord_to_tuple(cilj_kula)
    
    # Kula ne može ostati na istom mjestu
    if polazište == odredište:
        return False

    # Ako potez nije horizontalan ili vertikalan, nije legalan
    if polazište[0] != odredište[0] and polazište[1] != odredište[1]:
        return False


    # Provjera završnog polja
    ciljano_polje = ploča[odredište[0]][odredište[1]]
    if ciljano_polje is None:
        return True  # Prazno polje → legalan potez
    elif ciljano_polje['boja'] != figura_kula['boja']:
        return True  # Protivnička figura → legalan potez
    else:
        return False  # Vlastita figura → ilegalan potez

LEGAL_FUNCITONS = {
    'kula': legal_kula,
}

def is_move_legal(figura: dict[str, str], cilj: str, ploča: list[list]) -> bool:
    tip = figura['tip']
    legal_funkcija = LEGAL_FUNCITONS[tip]
    dopušteno = legal_funkcija(figura, cilj, ploča)  
    return dopušteno

