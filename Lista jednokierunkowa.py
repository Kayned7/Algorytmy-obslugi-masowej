class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc  # Wartość przechowywana w węźle
        self.next = None  # Wskaźnik na następny węzeł


class SLL:
    def __init__(self):
        self.head = None  # Wskaźnik na pierwszy element listy
        self.elements = []  # Lista do przechowywania wartości w celach pomocniczych (pokazywanie listy)
    
    def dodaj(self, wartosc, pozycja):
        new_node = Node(wartosc)  # Tworzenie nowego węzła z podaną wartością
            
        # Jeśli lista jest pusta, nowy węzeł staje się głową listy
        if self.head is None:
            self.head = new_node
            print(f"Lista była pusta, dodano element {wartosc} na pozycję 0")
            return
            
        # Dodanie nowego węzła na początku listy (pozycja 0)
        if pozycja == 0:
            new_node.next = self.head  # Nowy węzeł wskazuje na dotychczasową głowę listy
            self.head = new_node  # Nowy węzeł staje się nową głową
            print(f"Dodano element {wartosc} na pozycję 0")
            return

        # Przechodzenie przez listę, aby znaleźć właściwą pozycję do wstawienia węzła
        current = self.head
        indeks = 0
        while current and indeks < pozycja - 1:  # Znajdź węzeł przed podaną pozycją
            current = current.next
            indeks += 1

        # Sprawdzenie, czy pozycja jest poza zakresem listy
        if current is None:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
        else:
            # Wstawienie nowego węzła na wskazaną pozycję
            new_node.next = current.next
            current.next = new_node
            print(f"Dodano element {wartosc} na pozycję {pozycja}")
            
    def usun(self, pozycja):
        if not self.head:  # Sprawdzenie, czy lista jest pusta
            print("Lista jest pusta")
            return
        
        # Przypadek usunięcia pierwszego elementu
        current = self.head
        last = None  # Wskaźnik na poprzedni element
        i = 0  # Licznik pozycji
        
        while current and i <= pozycja:  # Przechodzenie przez listę do podanej pozycji
            if i == pozycja:  # Znaleziono pozycję do usunięcia
                if last is None:
                    self.head = current.next  # Jeśli usuwany jest pierwszy element, przesuń głowę
                else:
                    last.next = current.next  # Usuń element, aktualizując wskaźnik poprzedniego węzła
                print(f"Element na pozycji {pozycja} został usunięty z listy")
                return
            last = current
            current = current.next
            i += 1

        print(f"Pozycja {pozycja} jest poza zakresem listy")
        
    def pokaz(self):
        # Odświeżanie listy elementów do wyświetlenia
        self.elements = []  
        if not self.head:
            print("Lista jest pusta")
        else:
            current = self.head
            # Przechodzenie przez całą listę i dodawanie wartości do `elements`
            while current:
                self.elements.append(current.wartosc)
                current = current.next
            print("Lista zawiera:", self.elements)
        
    def szukaj(self, wartosc):
        # Przeszukiwanie listy bezpośrednio po węzłach
        current = self.head
        found = False
        while current:
            if current.wartosc == wartosc:  # Znaleziono wartość
                found = True
                break
            current = current.next
        
        if found:
            print(f"Element {wartosc} znajduje się na liście")
        else:
            print(f"Element {wartosc} nie znajduje się na liście")


# Inicjalizacja listy i interfejsu użytkownika
lista = SLL()

# Pętla obsługująca interfejs użytkownika
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
            print("Dane muszą być liczbami całkowitymi")
    
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
