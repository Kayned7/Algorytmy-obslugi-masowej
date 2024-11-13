class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc  # Wartość przechowywana w węźle
        self.next = None  # Wskaźnik na następny węzeł
        self.prev = None  # Wskaźnik na poprzedni węzeł


class DLL:
    def __init__(self):
        self.head = None  # Wskaźnik na pierwszy węzeł listy
        self.elements = []  # Lista pomocnicza do przechowywania wartości węzłów przy wyświetlaniu
    
    def dodaj(self, wartosc, pozycja):
        new_node = Node(wartosc)  # Tworzenie nowego węzła z podaną wartością

        # Dodawanie do pustej listy
        if self.head is None:
            self.head = new_node
            print(f"Lista była pusta, dodano element {wartosc} na pozycję 0")
            return

        # Dodawanie nowego węzła na początku listy
        if pozycja == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print(f"Dodano element {wartosc} na pozycję 0")
            return

        # Dodawanie nowego węzła w określonej pozycji
        current = self.head
        indeks = 0
        while current and indeks < pozycja - 1:
            current = current.next
            indeks += 1

        if current is None:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
        else:
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            new_node.prev = current
            current.next = new_node
            print(f"Dodano element {wartosc} na pozycję {pozycja}")

    def usun(self, pozycja):
        # Sprawdzanie, czy lista jest pusta
        if not self.head:
            print("Lista jest pusta")
            return
        
        # Usuwanie pierwszego elementu
        current = self.head
        if pozycja == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            print(f"Element na pozycji {pozycja} został usunięty z listy")
            return
        
        # Przechodzenie do określonej pozycji
        for i in range(pozycja):
            current = current.next
            if current is None:
                print(f"Pozycja {pozycja} jest poza zakresem listy")
                return

        # Usuwanie elementu
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        print(f"Element na pozycji {pozycja} został usunięty z listy")

    def pokaz(self):
        # Czyszczenie listy pomocniczej
        self.elements = []
        
        # Sprawdzanie, czy lista jest pusta
        if not self.head:
            print("Lista jest pusta")
        else:
            # Przechodzenie przez listę i dodawanie wartości węzłów do listy pomocniczej
            current = self.head
            while current:
                self.elements.append(current.wartosc)
                current = current.next
            print("Lista zawiera:", self.elements)
        
    def szukaj(self, wartosc):
        # Sprawdzanie, czy element o zadanej wartości znajduje się na liście
        if wartosc in self.elements:
            print(f"Element {wartosc} znajduje się na liście")
        else:
            print(f"Element {wartosc} nie znajduje się na liście")


lista = DLL()

# Pętla główna do obsługi listy, oparta na wejściu użytkownika
while True:
    a = input(
    """         
        d=dodaj
        u=usuń
        s=szukanie liczby
        p=pokaż listę
        z=zakończ 
Co chcesz wykonać: """).strip()

    if a == "d":
        try:
            wartosc = int(input("Podaj wartość: "))
            pozycja = int(input("Podaj pozycję (zaczyna się od 0): "))
            lista.dodaj(wartosc, pozycja)
        except ValueError:
            print("Wartość musi być liczbą całkowitą")
    
    elif a == "u":
        try:
            pozycja = int(input("Podaj pozycję do usunięcia: "))
            lista.usun(pozycja)
        except ValueError:
            print("Pozycja musi być liczbą całkowitą")
    
    elif a == "s":
        try:
            wartosc = int(input("Podaj szukaną liczbę: "))
            lista.szukaj(wartosc)
        except ValueError:
            print("Szukana wartość musi być liczbą całkowitą")
    
    elif a == "p":
        lista.pokaz()

    elif a == "z":
        break

    else:
        continue
