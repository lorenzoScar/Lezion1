import flet as ft

class View:
    def __init__(self, page):
        self._page = page
        self._controller = None
        self._titolo = None
        self._page_title = "Tdp 2025 - Software Gestionale"
        self._page.horizontal_alignment = ("CENTER")
        self.txtInNome = None
        self.update_page()

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Gestionale ordini",
                               color="blue", size=24)
        #caricare l'interfaccia che voglio

        """Prodotto"""
        self._txtInNomeP = ft.TextField(label="Nome prodotto", width=200)
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantita = ft.TextField(label="Quantità", width=200)

        row1 = ft.Row(
            controls=[self._txtInNomeP,self._txtInPrezzo,self._txtInQuantita],
            alignment= ft.MainAxisAlignment.CENTER)

        """Cliente"""
        self._txtInNomeC = ft.TextField(label="Nome cliente", width=200)
        self._txtInMail = ft.TextField(label="Mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)

        row2 = ft.Row(
            controls=[self._txtInNomeC, self._txtInMail, self._txtInCategoria],
            alignment= ft.MainAxisAlignment.CENTER)

        """Bottoni"""
        self._btnAdd = ft.ElevatedButton(text="Aggiungi ordine",
                                         on_click=self._controller.add_ordine,
                                         width=200)
        self._btnGestisciOrdine = ft.ElevatedButton(text="Gestici prossimo ordine",
                                                    on_click=self._controller.gestisci_ordini,
                                                    width=200)
        self._btnGestisciAllOrdini = ft.ElevatedButton(text="Gestici tutti gli ordini",
                                                       on_click=self._controller.gestisci_all_ordini,
                                                       width=200)
        self._btnStampaInfo = ft.ElevatedButton(text="Stampa info",
                                                on_click=self._controller.stampa_sommario,
                                                width=200)

        row3 = ft.Row(
            controls=[self._btnAdd, self._btnGestisciOrdine,
                      self._btnGestisciAllOrdini, self._btnStampaInfo],
            alignment= ft.MainAxisAlignment.CENTER
        )

        self._lvOut = ft.ListView(expand=True)
        self._page.add(row1, row2, row3, self._lvOut)


    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()