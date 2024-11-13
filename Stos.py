class Stos:
    def __init__(self):
        self.items = []
        self.limit = 5
        self.licznik = 1   
    
    def dodaj(self):
        if len(self.items) == self.limit:
            print("Brak miejsca w kolejce")
        else:
            self.items.append(self.licznik)
            print(f"Dodano element {self.licznik} do kolejki")
            self.licznik += 1 

    def usun(self):
        if len(self.items) != 0:
            usuniety = self.items.pop() 
            print(f"Element {usuniety} został usunięty ze stosu")
        else:
            print("Brak elementów do usunięcia, stos jest pusty")
    
    def pokaz(self):
        if len(self.items) == 0:
            print("Stos jest pusty")
        else:
            print(f"Stos ma {len(self.items)} elementów: {self.items}")
    
    def szukaj(self, wartosc):
        if wartosc in self.items:
            print(f"Element {wartosc} znajduje się na stosie")
        else:
            print(f"Element {wartosc} nie znajduje się na stosie")

s = Stos()

while True:
    a = input(
    """         
        d=dodaj
        u=usuń
        s=szukanie liczby
        p=pokaż stos
        z=zakończ 
Co chcesz wykonać: """).strip()

    if a == "d":
        s.dodaj()

    elif a == "u":
        s.usun()
    
    elif a == "s":
        try:
            f = int(input("Podaj szukaną liczbę: "))
            s.szukaj(f)
        except ValueError:
            print("Szukana wartość musi być liczbą całkowitą")
    
    elif a == "p":
        s.pokaz()

    elif a == "z":
        break

    else:
        continue
