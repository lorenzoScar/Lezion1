# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...

class Prodotto:

    aliquota_iva = 0.22 #variabile di classe

    def __init__(self, nome, prezzo, quantita, fornitore):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        self.fornitore = fornitore

    def valore_netto(self):
        return self.prezzo*self.quantita

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

myProduct1 = Prodotto(nome="Laptop", prezzo=1200.0, quantita=12, fornitore="ABC")

print(f"Nome prodotto: {myProduct1.nome} - prezzo: {myProduct1.prezzo}")

print(f"Il totale lordo di myproduct1 è {myProduct1.valore_lordo()}")
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari", 200.0, "ABC")
# prodotto costruito con un diverso costruttore
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myProduct1.prezzo, 0.15)}")

myProduct2 = Prodotto("Mouse", 10, 25, "ABC")
print(f"Nome prodotto: {myProduct2.nome} - prezzo: {myProduct2.prezzo}")

#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

class Cliente:
    def __init__(self, nome, email, categoria):
        self.nome = nome
        self.email = email
        self.categoria = categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

c1 = Cliente("Mario Bianchi","mario.bianchi@polito.it", "Gold")
print(c1.descrizione())