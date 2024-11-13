class KolejkaZPriorytetem:
    def __init__(self):
        self.items = []  
        self.limit = 5   
    
    def dodaj(self, wartosc, priorytet):
        if len(self.items) == self.limit:
            print("Brak miejsca w kolejce")
        else:
            element = (wartosc, priorytet)
            index = 0
            while index < len(self.items) and self.items[index][1] >= priorytet:
                index += 1
            self.items.insert(index, element)
            print(f"Dodano element {wartosc} z priorytetem {priorytet} do kolejki")
    
    def usun(self):
        if len(self.items) != 0:
            usuniety = self.items.pop(0)
            print(f"Element {usuniety[0]} z priorytetem {usuniety[1]} został usunięty z kolejki")
        else:
            print("Brak elementów do usunięcia, kolejka jest pusta")
    
    def pokaz(self):
        if len(self.items) == 0:
            print("Kolejka jest pusta")
        else:
            kolejka = [(elem[0], elem[1]) for elem in self.items]
            print(f"Kolejka ma {len(self.items)} elementów: {kolejka}")
    
    def szukaj(self, wartosc):
        for elem in self.items:
            if elem[0] == wartosc:
                print(f"Element {wartosc} z priorytetem {elem[1]} znajduje się w kolejce")
                return
        print(f"Element {wartosc} nie znajduje się w kolejce")

q = KolejkaZPriorytetem()

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
