"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine, lo aggiungo a una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
import random
from collections import defaultdict, deque, Counter

from dao.dao import DAO
from gestionale.core.cliente import (ClienteRecord)
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        #conteggio statistiche prodotti, conta in automatico occorrenze, most common
        self._ordini_per_categoria = defaultdict(list)
        #conteggio degli ordini per categoria di cliente con dizionario
        #chiave = gategoria -> valore = ordini
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self):
        self._allP.extend(DAO.getAllProdotti())
        self._allC.extend(DAO.getAllClienti())

        for i in range(10):
            indexP = random.randint(0,len(self._allP)-1)
            indexC = random.randint(0,len(self._allC)-1)

            ordine = Ordine( [RigaOrdine(self._allP[indexP],
                                         random.randint(1,5))],
                                         self._allC[indexC])

    def add_ordine(self, ordine: Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto nuovo ordine da parte di {ordine.cliente}.")
        #print(f"Ordini ancora da evadere: {self.ordini_da_processare}")
        #se voglio il numero -> len
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine(self, nomeP, prezzoP, quantitaP,
                     nomeC, mailC, categoriaC):

        prod = ProdottoRecord(nomeP, prezzoP)
        cliente = ClienteRecord(nomeC, mailC, categoriaC)

        self._update_DB(prod, cliente)

        return Ordine([RigaOrdine(prod, quantitaP)], cliente)

    def _update_DB(self, prod, cliente):
        if not DAO.hasProdotto(prod):
            DAO.addProdotto(prod)

        if not DAO.hasCliente(cliente):
            DAO.addCliente(cliente)

    def processa_prossimo_ordine(self):
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)

        #controllo se la coda è vuota
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("","",""))

        #se non è vuota, processo il primo e lo stampo all'utente
        ordine = self._ordini_da_processare.popleft() #logica fifo
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #aggiorno il counter per ogni riga
        #cioè le statistiche sui prodotti venduti
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.nome] += riga.quantita

        #categorizzo gli ordini in fuzione della categoria del cliente
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato.")
        return True, ordine

    def processa_tutti_ordini(self):

        """for ordine in self._ordini_da_processare:
            self.processa_prossimo_ordine()"""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")

        ordini = []

        while self._ordini_da_processare:
            _, ordine = self.processa_prossimo_ordine()
            ordini.append(ordine)
            #_ variabile che non ci serve, per convenzione
        print("Tutti gli ordini sono stati processati.")

        return ordini

    def get_statistiche_prodotti(self, top_n: int = 5):

        valori = []

        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto,quantita))

        return valori

    def get_distribuzione_categorie(self):

        valori = []

        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum( [o.totale_lordo(0.22) for o in ordini] )
            valori.append((cat,totale_fatturato))

        return valori

    def get_riepilogo(self):
        sommario = ""
        sommario += "\n" + "=" * 60
        sommario += "\nStato attuale del business:"
        sommario += f"\nOrdini correttamente gestiti: {len(self._ordini_processati)}"
        sommario += f"\nOrdini in coda: {len(self._ordini_da_processare)}"

        sommario += "\nProdotti più venduti: "
        for prodotto, quantita in self.get_statistiche_prodotti():
            sommario += f"\n{prodotto}: {quantita}"

        sommario += f"\nFatturato per categoria: "
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario += f"\n{cat}: {fatturato}"

        sommario += "\n" + "=" * 60
        return sommario

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
            RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Fulvio Bianchi", "bianchi@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
            ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Francesca Pistilli", "francesca@gmail.com", "Bronze"))
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()
    sistema.get_riepilogo()

if __name__ == "__main__":
    test_modulo()