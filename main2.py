# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...

#aggiornamento del main, con piccole modifiche
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

myProduct1 = Prodotto(nome="Laptop", prezzo=1200.0, quantita=12, fornitore="ABC")
Prodotto.aliquota_iva = 0.24
print(f"Valore lordo di myproduct1: {myProduct1.valore_lordo()}")

print(myProduct1)

p_a = Prodotto("Laptop", 1200.0, 12, "ABC")

p_b = Prodotto("Mouse", 10.0, 14, "CDE")

print("myyproduct1 == p_a?", myProduct1 == p_a) #mi aspetto True

print("p_a == p_b?", p_a == p_b)  #mi aspetto False

#lista prodotti, molto generica - il sort funziona per eq/lq implementati
mylist = [p_a, p_b, myProduct1]
mylist.sort(reverse=True)

print("lista di prodotti ordinati")

for p in mylist:
    print(f"- {p}")

my_product_scontato = ProdottoScontato("Auricolari", 320, 1, "ABC", 10)

my_service = Servizio("Consulenza", 100, 3)

mylist.append(my_product_scontato)
mylist.append(my_service)

mylist.sort(reverse=True)

for elem in mylist:
    print(elem.nome, " -> ", elem.prezzo_finale())

print("-------------------------------------------------------------")

# Definire una classe Abbonamento che abbia come attributi: "nome, prezzo_mensile,
# mesi". Abbonamento dovrà avere un metodo per calcolare il prezzo finale,
# ottenuto come prezzo_mensile*mesi

class Abbonamento:
    def __init__(self, nome, prezzo_mensile, mesi):
        self.nome = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile*self.mesi

abb = Abbonamento("Software gestionale", 30.0, 24)

mylist.append(abb)
for elem in mylist:
    print(elem.nome, " -> ", elem.prezzo_finale())

def calcola_totale(elementi):
    tot = 0
    for e in elementi:
        tot += e.prezzo_finale()
    return tot

print(f"Il totale è: {calcola_totale(mylist)}")

from typing import Protocol

# definisco un "contratto", qualsiasi oggetto che HAPREZZOFINALE
# deve avere un metodo prezzo_finale() e restituisce float

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) -> float:
        ... # simile a pass, non devo per forza implementarlo

def calcola_totale(elementi: list[HaPrezzoFinale]):
    return sum(e.prezzo_finale() for e in elementi)

print(f"Il totale è: {calcola_totale(mylist)}")
print("-----------------------------------------------------")

print("Sperimentiamo con Dataclass")

from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    nome: str
    prezzo_unitario: float

@dataclass
class ClienteRecord:
    nome: str
    email: str
    categoria: str

@dataclass
class RigaOrdine:
    prodotto: ProdottoRecord
    quantita: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario * self.quantita

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()+self.totale_netto()*aliquota_iva

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine):
    sconto_percentuale: float

    def totale_scontato(self):
        return self.totale_lordo()-self.totale_lordo()*self.sconto_percentuale

    def totale_netto(self):
        # return self.totale_netto()-self.totale_netto()*self.sconto_percentuale
        netto_base = super().totale_netto()
        return netto_base-netto_base*self.sconto_percentuale
        # posso ridefinirmi tramite override i metodi ereditati

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto: ", ordine_scontato.totale_netto())
print("Totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))

print("-----------------------------------------------------------------")


#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

class Cliente:
    def __init__(self, nome, email, categoria):
        self.nome = nome
        self.email = email
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, input):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if input not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere tra Gold, Silver, Bronze")

        self._categoria = input

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

c1 = Cliente("Mario Bianchi","mario.bianchi@polito.it", "Gold")
print(c1.descrizione())
#c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Platinum")