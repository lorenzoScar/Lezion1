from dataclasses import dataclass

class Prodotto:

    aliquota_iva = 0.22 #variabile di classe

    def __init__(self, nome, prezzo, quantita, fornitore):
        self.nome = nome
        self._prezzo = None
        self.prezzo = prezzo
        self.quantita = quantita
        self.fornitore = fornitore

    def valore_netto(self):
        return self._prezzo*self.quantita

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto + netto*self.aliquota_iva
        return lordo

    @classmethod
    def costruttore_con_quantita_uno(cls,nome: str, prezzo: float, fornitore: str):
        cls(nome, prezzo, 1, fornitore)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return (prezzo - (prezzo * percentuale))

    @property
    def prezzo(self): #getter di java
        return self._prezzo

    @prezzo.setter
    def prezzo(self, input):
        if input < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo")
        self._prezzo = input

    def __str__(self): #toString java
        return f"{self.nome} - disponibili {self.quantita} pezzi a {self.prezzo} $"

    def __repr__(self):
        return f"Prodotto (nome = {self.nome}, prezzo = {self.prezzo}, quantita = {self.quantita}, fornitore = {self.fornitore})"

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Prodotto):
            return NotImplemented

        return (self.nome == other.nome
                and self.prezzo == other.prezzo
                and self.quantita == other.quantita
                and self.fornitore == other.fornitore)

    def __lt__(self, other: object) -> bool:
        return self.prezzo < other.prezzo

    def prezzo_finale(self) -> float:
        return (self.prezzo + self.prezzo*self.aliquota_iva)


class ProdottoScontato(Prodotto): #ereditarietà
    def __init__(self, nome, prezzo, quantita, fornitore, sconto_percento):
        super().__init__(nome, prezzo, quantita, fornitore)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return (self.valore_lordo()-self.valore_lordo()*self.sconto_percento/100)


class Servizio(Prodotto):
    def __init__(self, nome, tariffa_oraria, ore):
        super().__init__(nome=nome, prezzo = tariffa_oraria, quantita = 1, fornitore = None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.prezzo * self.ore

#--------------------------------------------------------------------#

class Abbonamento:
    def __init__(self, nome, prezzo_mensile, mesi):
        self.nome = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile*self.mesi

MAX_QUANTITA = 1000

def crea_prodotto_stndard(nome: str, prezzo: float):
    return Prodotto(nome,prezzo, 1, None)

def test_modulo():
    print("Sto testando il modulo prodotty.py")

    myProduct1 = Prodotto(nome="Laptop", prezzo=1200.0, quantita=12, fornitore="ABC")
    print(f"Nome Prodotto: {myProduct1.nome} - prezzo: {myProduct1.prezzo}")
    print(f"Il totale lordo di myProduct1 è: {myProduct1.valore_lordo()}")
    print(f"Prezzo scontato di myProduct1 è: "
          f"{Prodotto.applica_sconto(myProduct1.prezzo,0.15)}")

    p3 = Prodotto.costruttore_con_quantita_uno("Auricolari", 200.0, "ABC")
    myProduct2 = Prodotto("Mouse", 10, 25, "CDE")
    print(f"Nome Prodotto: {myProduct2.nome} - prezzo: {myProduct2.prezzo}")
    print(f"Il totale lordo di myProduct2 è: {myProduct2.valore_lordo()}")

    print(myProduct1)
    Prodotto.aliquota_iva = 0.24

    p_a = Prodotto("Laptop", 1200.0, 12, "ABC")

    p_b = Prodotto("Mouse", 10.0, 14, "CDE")

    print("myyproduct1 == p_a?", myProduct1 == p_a)  # mi aspetto True

    print("p_a == p_b?", p_a == p_b)  # mi aspetto False

    # lista prodotti, molto generica - il sort funziona per eq/lq implementati
    mylist = [p_a, p_b, myProduct1]
    mylist.sort(reverse=True)

    print("lista di prodotti ordinati")

    for p in mylist:
        print(f"- {p}")


if __name__  == "main":
    test_modulo()