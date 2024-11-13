class Kolejka:
    def __init__(self):
        self.items = []  # Lista przechowująca elementy w kolejce
        self.limit = 5   # Maksymalna liczba elementów w kolejce
        self.licznik = 1 # Licznik do dodawania kolejnych elementów z unikalną wartością
    
    def dodaj(self):
        # Sprawdzenie, czy kolejka osiągnęła limit
        if len(self.items) == self.limit:
            print("Brak miejsca w kolejce")
        else:
            # Dodanie nowego elementu do kolejki
            self.items.append(self.licznik)
            print(f"Dodano element {self.licznik} do kolejki")
            self.licznik += 1  # Zwiększenie licznika dla następnego elementu

    def usun(self):
        # Sprawdzenie, czy kolejka nie jest pusta
        if len(self.items) != 0:   
            usuniety = self.items.pop(0)  # Usunięcie pierwszego elementu z kolejki
            print(f"Element początkowy {usuniety} został usunięty z kolejki")
        else: 
            print("Brak elementów do usunięcia, kolejka jest pusta")

    def pokaz(self):
        # Wyświetlenie zawartości kolejki
        if len(self.items) == 0:
            print("Kolejka jest pusta")
        else:
            print(f"Kolejka ma {len(self.items)} elementów: {self.items}")

    def szukaj(self, wartosc):
        # Sprawdzenie, czy element o zadanej wartości znajduje się w kolejce
        if wartosc in self.items:
            print(f"Element {wartosc} znajduje się w kolejce")
        else:
            print(f"Element {wartosc} nie znajduje się w kolejce")

q = Kolejka()

# Pętla główna do obsługi kolejki, oparta na wejściu użytkownika
while True:
    a = input(
    """         
        d=dodaj
        u=usuń
        s=szukanie liczby
        p=pokaż kolejkę
        z=zakończ 
Co chcesz wykonać: """).strip()

    if a == "d":
        q.dodaj()
    
    elif a == "u":
        q.usun()
    
    elif a == "s":
        try:
            f = int(input("Podaj szukaną liczbę: "))
            q.szukaj(f)
        except ValueError:
            print("Szukana wartość musi być liczbą całkowitą")
    
    elif a == "p":
        q.pokaz()

    elif a == "z":
        break

    else:
        continue
