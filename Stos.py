class Stos:
    def __init__(self):
        # Inicjalizacja stosu z ograniczoną liczbą elementów
        self.items = []  # Lista reprezentująca stos
        self.limit = 5   # Maksymalna liczba elementów na stosie
        self.licznik = 1 # Licznik dla kolejnego dodawanego elementu
    
    def dodaj(self):
        # Dodawanie elementu na stos, jeśli nie został osiągnięty limit
        if len(self.items) == self.limit:
            print("Brak miejsca w kolejce")
        else:
            self.items.append(self.licznik)  # Dodanie elementu na stos
            print(f"Dodano element {self.licznik} do kolejki")
            self.licznik += 1  # Inkrementacja licznika, aby nadawać kolejne numery elementom

    def usun(self):
        # Usuwanie elementu ze stosu, jeśli jest co usuwać
        if len(self.items) != 0:
            usuniety = self.items.pop()  # Usunięcie ostatniego elementu (LIFO)
            print(f"Element {usuniety} został usunięty ze stosu")
        else:
            print("Brak elementów do usunięcia, stos jest pusty")
    
    def pokaz(self):
        # Wyświetlanie elementów na stosie
        if len(self.items) == 0:
            print("Stos jest pusty")
        else:
            print(f"Stos ma {len(self.items)} elementów: {self.items}")
    
    def szukaj(self, wartosc):
        # Wyszukiwanie podanej wartości na stosie
        if wartosc in self.items:
            print(f"Element {wartosc} znajduje się na stosie")
        else:
            print(f"Element {wartosc} nie znajduje się na stosie")

# Inicjalizacja stosu i obsługa użytkownika
s = Stos()

# Pętla główna do interakcji użytkownika z programem
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
        # Dodanie elementu na stos
        s.dodaj()

    elif a == "u":
        # Usunięcie elementu ze stosu
        s.usun()
    
    elif a == "s":
        # Wyszukiwanie elementu na stosie
        try:
            f = int(input("Podaj szukaną liczbę: "))
            s.szukaj(f)
        except ValueError:
            print("Szukana wartość musi być liczbą całkowitą")
    
    elif a == "p":
        # Wyświetlenie zawartości stosu
        s.pokaz()

    elif a == "z":
        # Zakończenie programu
        break

    else:
        # Ignorowanie nieprawidłowych poleceń
        continue
