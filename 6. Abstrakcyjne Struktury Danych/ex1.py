class Drukarka:
    def __init__(self):
        self.kolejka = []

    def dodaj_zadanie(self, dokument):
        self.kolejka.append(dokument)

    def drukuj(self):
        if self.kolejka:
            return self.kolejka.pop(0)
        return "Brak zadań w kolejce."

    def ile_czeka(self):
        return len(self.kolejka)

drukarka = Drukarka()
drukarka.dodaj_zadanie("CV.pdf")
drukarka.dodaj_zadanie("Zdjęcie.jpg")
drukarka.dodaj_zadanie("Raport.docx")

print(drukarka.drukuj())
print(drukarka.ile_czeka())
print(drukarka.drukuj())
print(drukarka.ile_czeka())