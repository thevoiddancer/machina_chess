from helper_functions import koord_to_tuple, tuple_to_koord

POČETNI_POLOŽAJI = {
    "bijelo": {
        "Kralj": ["E1"],
        "Dama": ["D1"],
        "Top": ["A1", "H1"],
        "Lovac": ["C1", "F1"],
        "Skakač": ["B1", "G1"],
        "Pješak": ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    },
    "crno": {
        "Kralj": ["E8"],
        "Dama": ["D8"],
        "Top": ["A8", "H8"],
        "Lovac": ["C8", "F8"],
        "Skakač": ["B8", "G8"],
        "Pješak": ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    },
}


class Figura:
    def __init__(
        self, boja: str, tip: str, položaj_str: str = None, položaj_tup: tuple = None
    ) -> None:
        self.boja = boja
        self.tip = tip  # Kralj, Dama, Top, Lovac, Skakač, Pješak
        self.slovo = tip[0].upper()
        if položaj_str and not položaj_tup:
            self.položaj_str = položaj_str
            self.položaj_tup = koord_to_tuple(položaj_str)
        elif položaj_tup and not položaj_str:
            self.položaj_tup = položaj_tup
            self.položaj_str = tuple_to_koord(položaj_tup)
        else:
            self.položaj_tup = položaj_tup
            self.položaj_str = položaj_str
            if položaj_str != tuple_to_koord(položaj_tup):
                print("GREŠKA U POSTAVLJANJU FIGURE")

    def __repr__(self) -> str:
        return f"{self.slovo}({self.položaj_str})"


class Igrač:
    def __init__(self, ime: str, boja: str) -> None:
        self.ime = ime
        self.boja = boja
        self.kralj = [Figura(boja, "Kralj", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Kralj"]]
        self.dama = [Figura(boja, "Dama", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Dama"]]
        self.top = [Figura(boja, "Top", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Top"]]
        self.skakač = [Figura(boja, "Skakač", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Skakač"]]
        self.lovac = [Figura(boja, "Lovac", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Lovac"]]
        self.pješak = [Figura(boja, "Pješak", položaj) for položaj in POČETNI_POLOŽAJI[boja]["Pješak"]]
        self.figure = self.kralj + self.dama + self.top + self.skakač + self.lovac + self.pješak

    def __repr__(self) -> str:
        return f'{self.ime} {self.boja[0].upper()}'