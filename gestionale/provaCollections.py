import copy

from collections import Counter, deque

from gestionale.core.cliente import ClienteRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from gestionale.core.prodotto import ProdottoRecord

print("=====================================================")
print("Liste")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

#creo una lista, posso farla con i prodotti creati o crearne uno mentre lo aggiungo
carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}). {p.nome} - {p.prezzo_unitario}")

#aggiungo a una lista
carrello.append(ProdottoRecord("Monitor", 150))

carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}). {p.nome} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#metodi per aggiungere
carrello.append(ProdottoRecord("Penna", 100.0))
carrello.extend([ProdottoRecord("Caricatore", 110.0), ProdottoRecord("Cavo USB", 10.0)])
carrello.insert(2, ProdottoRecord("Agenda", 20.0))

#metodi per rimuovere
carrello.pop() #rimuovo ultimo
carrello.pop(2) #in pos 2
carrello.pop(p1) #elimino prima occorrenza p1
#carrello.clear() svuoto la lista

#metodi per sortare
#carrello.sort() #ordina seguendo ordinamento naturale -- non funziona senza lq
#carrello.sort(Reverse=True) #ordina al contrario
#carrello.sory(key = function)
#carrello_ordinato = sorted(carrello)

#metodi per copiare-altro
carrello.reverse() #inverte l'ordine
carrello_copia = carrello.copy() #shallow copy
carrello_copia2 = copy.deepcopy(carrello) #deep copy -> copia contenuto

#tuple
print("=====================================================")
print("Tuple")
sede_principale = (45,8) #lat, long sede di torino
sele_milano = (45,9) #lat, long di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA=(
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi)

tot, media, max, mid = calcola_statistiche_carrello(carrello)
#tot, *altri_campi = calcola_statistiche_carrello(carrello)

print("=====================================================")
print("Set")
#set
categorie = {"Gold", "Silver", "Bronze"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
#categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2 #unione
print(categorie_all)

categorie_comuni = categorie & categorie2 #solo comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 #solo in uno dei due
print(categorie_esclusive)

categorie_esclusive_sym = categorie ^ categorie2 # differenza simmetrice
print(categorie_esclusive_sym)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mouse", 20.0),
                     ProdottoRecord("Auricolari", 250.0)
}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                     ProdottoRecord("Mouse2", 20.0),
                     ProdottoRecord("Tablet", 700.0)
}

s = set()
s1 = set()

s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0),ProdottoRecord("bbb", 20.0),p1,p2,p3]) #più elementi

#s.remove(elem) #errore se non esiste
#s.discard(elem) #senza arrabbiarsi se non esiste
s.pop()
s.clear()

s.union(s1) # s | s1
s.intersection(s1) # s & s1
s.difference(s1) # s - s1 -> s non contenuti in s1
s.symmetric_difference(s1) # s ^ s1, s non contenuti in s1 e VICEVERSA

s1.issubset(s) #s1 contenuto in s?
s1.issuperset(s) #s in s1?
s1.isdisjoint(s) #s != s1?


print("=====================================================")
print("Dizionari")
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001": ProdottoRecord("Mouse", 20.0),
    "AUR001": ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

#print("Cerco un altro oggetto: {catalogo["Non esiste"]}")

prod1 = catalogo.get("Non esiste")

if prod1 is None:
    print("Prodotto non trovato")

prodotto2 = catalogo.get("Non esiste 2", ProdottoRecord("Sconosciuto", 0.0))
print(prodotto2)

#dizionario : chiave -> valore
#posso farmi una lista di chiavi e di valori
keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a: {val}")

#rimuovere dal dizionario
rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}
#Per ogni coppia codice, prod presente in catalogo,
# inserisci nel nuovo dizionario il codice come chiave
# e il prezzo unitario del prodotto come valore.

# DA RICORDARE PER DICT
# d[key] = v scrivo sul dizionario
# v = d[key] leggo -- key error se non esiste
# v= d.get(key, default) legge senza error

# d.pop (key) restituisce val cancellato
# d. clear elimina tutto

# d.keys() restituisce tutte le chiavi
# d.values() restituisce tutti i valori
# d.items() # restituisce coppie chiave -> valore
# key in d verifica se key è presente nel diz


print("=====================================================")
print("Esercizio")

"""Esercizio live"""

"""1) Memorizzare un elenco di ordini che dovranno poi essere prcessati FIFO"""
# Collection? LISTA

ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i CF dei clienti (univoco)"""
codici_fiscai = {"jsvnihfvb123", "sdhfbqw937283", "jvnapasm234n1", "iufnibo45i2u31"}
print(codici_fiscai)

"""3) Creare un database di prodotti che posso cercare con un codice univoco"""
listino_prodotti = {
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "KEY001": ProdottoRecord("Keyboard", 130.0)
}

"""4) Memorizzare coordinate gps della nuova sede di Roma"""
magazzino_roma = (45, 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un
certo range temporale"""
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Silver")

print("=====================================================")
print("Counter")
#COUNTER
lista_clienti =[
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "giuseppe@polito.it", "Siler"),
    ClienteRecord("Francesca Pistilli", "francesca@polito.it", "Bronze"),
    ClienteRecord("Carlitos Masone", "carlitos@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "corno@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("2 categorie più frequenti")
print(categorie_counter.most_common(2))

print("Totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)

vendite_bimestre = vendite_gennaio + vendite_febbraio

print(f"Vendite gennaio: {vendite_gennaio}")
print(f"Vendite febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

print(f"Differenza di vendite: {vendite_gennaio - vendite_febbraio}")

vendite_gennaio["Laptop"] += 4
print(f"Vendite gennaio: {vendite_gennaio}")

#c.most_common(n) restituisce n elementi più frequenti
#c.total() somma dei conteggi

#deque
print("=====================================================")
print("Deque")

coda_ordini = deque()

for i in range (1,10):
    cliente = ClienteRecord(f"Cliente {i}", f"cliente{i}@polito.it", "Gold")
    prodotto = ProdottoRecord(f"Prodotto {i}", 100.0*i)
    ordine = Ordine([RigaOrdine(prodotto, 1), cliente])
    coda_ordini.append(ordine)

print(f"Ordini in coda: {len({coda_ordini})}")

while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente {ordine_corrente.cliente}")

print("Ho processato tutti gli ordini!")