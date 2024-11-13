class Node:
    def __init__(self, wartosc=None):
        # Inicjalizacja węzła, który przechowuje wartość i wskaźniki do sąsiednich węzłów
        self.wartosc = wartosc
        self.next = None  # Wskaźnik do następnego węzła
        self.prev = None  # Wskaźnik do poprzedniego węzła


class SentinelNode:
    def __init__(self):
        # Inicjalizacja listy z wartownikiem
        self.elements = []  # Lista pomocnicza do wyświetlania zawartości
        self.wartownik = Node()  # Utworzenie węzła wartownika
        # Wartownik tworzy strukturę cykliczną
        self.wartownik.next = self.wartownik  
        self.wartownik.prev = self.wartownik  

    def dodaj(self, wartosc, pozycja):
        # Dodanie nowego elementu na wskazaną pozycję
        new_node = Node(wartosc)
        current = self.wartownik.next  # Start od początku listy
        indeks = 0

        # Przemieszczanie się po liście aż do osiągnięcia podanej pozycji
        while current != self.wartownik and indeks < pozycja:
            current = current.next
            indeks += 1

        # Jeśli pozycja jest poza zakresem
        if indeks != pozycja:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
            return

        # Wstawianie nowego węzła w odpowiednim miejscu
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        print(f"Dodano element {wartosc} na pozycję {pozycja}")

    def usun(self, pozycja):
        # Usunięcie elementu na wskazanej pozycji
        current = self.wartownik.next  # Start od początku listy
        indeks = 0

        # Jeśli lista jest pusta
        if current == self.wartownik:
            print("Lista jest pusta")
            return

        # Przemieszczanie się do wskazanej pozycji
        while current != self.wartownik and indeks < pozycja:
            current = current.next
            indeks += 1

        # Jeśli pozycja jest poza zakresem
        if current == self.wartownik:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
        else:
            # Aktualizacja wskaźników w celu usunięcia elementu
            current.prev.next = current.next
            current.next.prev = current.prev
            print(f"Element na pozycji {pozycja} został usunięty z listy")

    def pokaz(self):
        # Wyświetlanie zawartości listy
        self.elements = []  # Resetowanie listy pomocniczej `elements`

        current = self.wartownik.next  # Start od początku listy
        # Przechodzenie przez listę aż do osiągnięcia wartownika
        while current != self.wartownik:
            self.elements.append(current.wartosc)  # Dodanie wartości do `elements`
            current = current.next
        print("Lista zawiera:", self.elements)
        return self.elements
        
    def szukaj(self, wartosc):
        # Wyszukiwanie wartości w liście
        if wartosc in self.elements:
            print(f"Element {wartosc} znajduje się na liście")
        else:
            print(f"Element {wartosc} nie znajduje się na liście")


# Inicjalizacja listy i interfejsu użytkownika
lista = SentinelNode()

# Pętla główna dla obsługi użytkownika
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
            wartosc = int(input("Podaj wartość: "))  # Pobranie wartości
            pozycja = int(input("Podaj pozycję (zaczyna się od 0): "))  # Pobranie pozycji
            lista.dodaj(wartosc, pozycja)  # Dodanie wartości do listy
        except ValueError:
            print("Wartość musi być liczbą całkowitą")
    
    elif a == "u":
        try:
            pozycja = int(input("Podaj pozycję do usunięcia: "))  # Pobranie pozycji do usunięcia
            lista.usun(pozycja)  # Usunięcie wartości z listy
        except ValueError:
            print("Pozycja musi być liczbą całkowitą")
    
    elif a == "s":
        try:
            wartosc = int(input("Podaj szukaną liczbę: "))  # Pobranie wartości do wyszukania
            lista.szukaj(wartosc)  # Wyszukanie wartości w liście
        except ValueError:
            print("Szukana wartość musi być liczbą całkowitą")
    
    elif a == "p":
        lista.pokaz()  # Wyświetlenie zawartości listy

    elif a == "z":
        break  # Zakończenie programu

    else:
        continue
