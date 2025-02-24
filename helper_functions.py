SLOVA = 'abcdefgh'

def koord_to_tuple(koord_slova: str) -> tuple | None:
    """
    Funkcija koja zamjenjuje klasičan zapis polja ('A1') s jednim koji će biti prikladniji
    za računanje (1, 1).

    Parameters
    ----------
    koord_slova : str
        Klasičan šahovski zapis polja
    
    Returns
    -------
    tuple | None
        Vraća tuple ako je podatak legalan, None ako nije.
    
    Raises
    ------
    None
    """
    slovo = koord_slova[0]
    broj = koord_slova[1:]

    if slovo.lower() in SLOVA:
        koord_1 = SLOVA.index(slovo.lower()) + 1
    else:
        return None

    if broj.isnumeric() and 1 <= int(broj) <= 8:
        koord_2 = int(broj)
    else:
        return None

    koord_tuple = (koord_1, koord_2)
    return koord_tuple

def tuple_to_koord(koord_tuple: tuple) -> str | None:
    """
    Funkcija koja zamjenjuje zapis polja u obliku brojeva u tupleu (1, 1) s klasičnim šahovskim
    zapisom ('A1').

    Parameters
    ----------
    koord_tuple : tuple
        Tuple zapis polja pomoću samo brojeva.
    
    Returns
    -------
    str | None
        Vraća str ako je podatak legalan, None ako nije.
    
    Raises
    ------
    None
    """
    koord_1, koord_2 = koord_tuple
    if 1 <= koord_1 <= 8:
        slovo = SLOVA[koord_1 - 1].upper()
    else:
        return None
    
    if 1 <= koord_2 <= 8:
        broj = str(koord_2)
    else:
        return None
    
    koord_slova = slovo + broj
    return koord_slova

