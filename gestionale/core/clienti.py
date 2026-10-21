from dataclasses import dataclass

# Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria"
# ("Gold", "Silver", "Bronze").
# Vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

"""
Si modifichi la classe cliente in maniera tale che la proprietà 
categoria sia "protetta" e accetti solo ("Gold", "Silver", "Bronze")
"""

categorie_valide = {"Gold", "Silver", "Bronze"}

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
        if input not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. "
                             "Scegliere tra Gold, Silver, Bronze")

        self._categoria = input

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

def test_modulo():
    c1 = Cliente("Mario Bianchi","mario.bianchi@polito.it", "Gold")
    print(c1.descrizione())
    #c2 = Cliente("Carlo Masone", "carlo.masone@polito.it", "Platinum")

if __name__ == "__main__":
    test_modulo()


"""
ho preso quello che c'era nel main che riguardava cliente e l'ho inserito
nella classe apposita, così risulta tutto più ordinato e se, in futuro, volessi
fare modifiche del cliente... non mi perdo in 200 righe di codice
"""