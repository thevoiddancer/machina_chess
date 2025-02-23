from helper_functions import koord_to_tuple, tuple_to_koord, board


def legal_kula (figura: dict[str, str], cilj: str) -> bool:
    """
    Funkcija koja provjerava je li najavljeni pomak kule legalan. Pravila koja prati su:
    + nije dopušteno ostati na mjestu 
    + željeni potez je pravocrtan. (X ili Y koordinata je uvijek ista)
    + potez je legalan ako između polazišta i odredišta nema niti jedne figure ili ako postoji suparnicka figura 


    Parameters
    ----------
    figura : dict[str, str]
        Dictionary koji nosi podatke o figuri kula - boja, tip i mjesto.
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

    # Provjera pravocrtnog poteza (horizontalno ili vertikalno)
    if polazište[0] == odredište[0]:  # Horizontalni potez
        min_y, max_y = polazište[1], odredište[1]
        if min_y > max_y:
            min_y, max_y = max_y, min_y  # Zamjena ako je potrebno
        for y in range(min_y + 1, max_y):
            if board[polazište[0]][y] is not None:  
                return False  # Figura blokira putanju

    elif polazište[1] == odredište[1]:  # Vertikalni potez
        min_x, max_x = polazište[0], odredište[0]
        if min_x > max_x:
            min_x, max_x = max_x, min_x  # Zamjena ako je potrebno
        for x in range(min_x + 1, max_x):
            if board[x][polazište[1]] is not None:  
                return False  # Figura blokira putanju

    return True  # Ako nema prepreka, potez je legalan

# Ovdje ostale funkcije
#Potrebne funkcije koja ce ako je potez legalan:
#   -pojesti suparnicku figuru ako postoji na odredistu
#   -maknuti pojedenu figuri s ploce
#   -upisati novu vrijednost koordinate na listu i vratiti novu listu za board

LEGAL_FUNCITONS = {
    'kula': legal_kula
}

def is_move_legal(figura: dict[str, str], cilj) -> bool:
    tip = figura['tip']
    legal_funkcija = LEGAL_FUNCITONS[tip]
    dopušteno = legal_funkcija(figura, cilj)
    return dopušteno