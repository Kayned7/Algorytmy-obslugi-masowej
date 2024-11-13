class Node:
    def __init__(self, wartosc=None):
        self.wartosc = wartosc
        self.next = None
        self.prev = None


class SentinelNode:
    def __init__(self):
        self.elements = []
        self.wartownik = Node()  
        self.wartownik.next = self.wartownik  
        self.wartownik.prev = self.wartownik  

    def dodaj(self, wartosc, pozycja):
        new_node = Node(wartosc)
        current = self.wartownik.next
        indeks = 0

        while current != self.wartownik and indeks < pozycja:
            current = current.next
            indeks += 1

        if indeks != pozycja:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
            return

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        print(f"Dodano element {wartosc} na pozycję {pozycja}")

    def usun(self, pozycja):
        current = self.wartownik.next 
        indeks = 0

        if current == self.wartownik:
            print("Lista jest pusta")
            return

        while current != self.wartownik and indeks < pozycja:
            current = current.next
            indeks += 1

        if current == self.wartownik:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            print(f"Element na pozycji {pozycja} został usunięty z listy")

    def pokaz(self):
        self.elements = []  

        current = self.wartownik.next
        while current != self.wartownik:
            self.elements.append(current.wartosc)
            current = current.next
        print("Lista zawiera:", self.elements)
        return self.elements
        
    def szukaj(self, wartosc):
        if wartosc in self.elements:
            print(f"Element {wartosc} znajduje się na liście")
        else:
            print(f"Element {wartosc} nie znajduje się na liście")

lista = SentinelNode()

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
            wartosc = int(input("Podaj wartość do usunięcia: "))
            lista.usun(wartosc)
        except ValueError:
            print("Wartość musi być liczbą całkowitą")
    
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
 