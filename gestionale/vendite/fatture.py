from dataclasses import dataclass
from datetime import date

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            "=" * 60,
            f"FATTURA N. {self.numero_fattura}".center(60),
            f"Data: {self.data.strftime('%d/%m/%Y')}".center(60),
            f"=" * 60,
            "",
            f"Cliente: {self.ordine.cliente.nome}",
            f"Email: {self.ordine.cliente.mail}",
            f"Categoria: {self.ordine.cliente.categoria}",
            "",
            "-" * 60,
            "DETTAGLIO PRODOTTI",
            "-" * 60,
        ]
        """f"="*60, #formattazione, output
                    f"Fattura no. {self.numero_fattura} del {self.data}"
                    f"="*60,
                    f"Cliente: {self.ordine.cliente.nome}",
                    f"Categoria: {self.ordine.cliente.categoria}",
                    f"Mail: {self.ordine.cliente.email}",
                    f"=" * 60,
                    f"DETTAGLIO ORDINE"""
        for i, riga in enumerate(self.ordine.righe, 1):
            linee.append(
                f"{i}. {riga.prodotto.nome:<22} "
                f"Q.tà {riga.quantita:>3} x {riga.prodotto.prezzo_unitario:>8.2f} $ = "
                f"{riga.totale_riga():>10.2f} $"
            )

        """f"{i+1}. " #formattazione elenco
                        f"{riga.prodotto.nome}"
                        f"Q.tà {riga.quantita} x {riga.prodotto.prezzo_unitario} = "
                        f"Tot. {riga.totale_riga()}"""

        linee.extend([
            "-" * 60,
            "",
            f"{'Totale netto:':<40} {self.ordine.totale_netto():>18.2f}$",
            f"{'IVA 22%:':<40} {self.ordine.totale_netto()*0.22:>18.2f}$",
            f"{'TOTALE FATTURA:':<40} {self.ordine.totale_lordo(0.22):>18.2f}$",
            "",
            "=" * 60
        ])

        """f"=" * 60,
                    f"Totale netto: {self.ordine.totale_netto()}",
                    f"IVA(22%):{self.ordine.totale_netto()*0.22}",
                    f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
                    f"=" * 60"""

        return "\n".join(linee)

def _test_modulo():

    p1 = ProdottoRecord("Laptop", 1200.0)
    p2 = ProdottoRecord("Mouse", 20)
    p3 = ProdottoRecord("Tablet", 600.0)

    #cliente = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    cliente = ClienteRecord("Mario Bianchi", "mario.bianchi@polito.it", "Gold")

    ordine = Ordine(righe=[
        RigaOrdine(p1,1),
        RigaOrdine(p2,5),
        RigaOrdine(p3,2),
    ], cliente = cliente)

    fattura = Fattura(ordine, "2026/01", date.today())

    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()