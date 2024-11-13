class KolejkaZPriorytetem:
    def __init__(self):
        self.items = []  # Lista przechowująca elementy w kolejce wraz z ich priorytetami
        self.limit = 5   # Maksymalna liczba elementów w kolejce
    
    def dodaj(self, wartosc, priorytet):
        # Sprawdzenie, czy kolejka osiągnęła limit
        if len(self.items) == self.limit:
            print("Brak miejsca w kolejce")
        else:
            # Tworzenie elementu jako krotki (wartość, priorytet)
            element = (wartosc, priorytet)
            index = 0  # Inicjalizacja indeksu, gdzie element będzie wstawiony
            
            # Szukanie właściwej pozycji do wstawienia elementu, aby zachować kolejność według priorytetów
            while index < len(self.items) and self.items[index][1] >= priorytet:
                index += 1
            
            # Wstawienie elementu na odpowiednie miejsce w kolejce
            self.items.insert(index, element)
            print(f"Dodano element {wartosc} z priorytetem {priorytet} do kolejki")
    
    def usun(self):
        # Sprawdzenie, czy kolejka nie jest pusta
        if len(self.items) != 0:
            usuniety = self.items.pop(0)  # Usunięcie elementu o najwyższym priorytecie (pierwszego w kolejce)
            print(f"Element {usuniety[0]} z priorytetem {usuniety[1]} został usunięty z kolejki")
        else:
            print("Brak elementów do usunięcia, kolejka jest pusta")
    
    def pokaz(self):
        # Wyświetlenie zawartości kolejki
        if len(self.items) == 0:
            print("Kolejka jest pusta")
        else:
            # Przygotowanie listy do wyświetlenia tylko wartości i priorytetów
            kolejka = [(elem[0], elem[1]) for elem in self.items]
            print(f"Kolejka ma {len(self.items)} elementów: {kolejka}")
    
    def szukaj(self, wartosc):
        # Przeszukiwanie kolejki w celu znalezienia elementu o zadanej wartości
        for elem in self.items:
            if elem[0] == wartosc:
                print(f"Element {wartosc} z priorytetem {elem[1]} znajduje się w kolejce")
                return
        print(f"Element {wartosc} nie znajduje się w kolejce")

q = KolejkaZPriorytetem()

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
        try:
            wartosc = int(input("Podaj wartość: "))
            priorytet = int(input("Podaj priorytet (większa liczba oznacza wyższy priorytet): "))
            q.dodaj(wartosc, priorytet)
        except ValueError:
            print("Wartość i priorytet muszą być liczbami całkowitymi")
    
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
