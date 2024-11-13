class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None
        self.elements = []
        
    def dodaj(self, wartosc, pozycja):
        new_node = Node(wartosc)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(f"Lista była pusta, dodano element {wartosc} na pozycję 0")
            return
        
        
        current = self.head
        liczba_wezlow = 1
        while current.next != self.head:
            liczba_wezlow += 1
            current = current.next
        if pozycja > liczba_wezlow:
            print(f"Pozycja {pozycja} jest poza zakresem listy (maksymalna pozycja to {liczba_wezlow})")
            return
        
        if pozycja == 0:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
            print(f"Dodano element {wartosc} na pozycję 0")
            return

        current = self.head
        indeks = 0
        while current.next != self.head and indeks < pozycja - 1:
            current = current.next
            indeks += 1

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        print(f"Dodano element {wartosc} na pozycję {pozycja}")
    
    def usun(self, pozycja):
        if not self.head:
            print("Lista jest pusta")
            return

        current = self.head
        i = 0

        if current.next == self.head and pozycja == 0:
            self.head = None
            print(f"Usunięto jedyny element na pozycji {pozycja}")
            return

        if pozycja == 0:
            tail = self.head.prev 
            self.head = self.head.next
            self.head.prev = tail 
            tail.next = self.head 
            print(f"Element na pozycji {pozycja} został usunięty z listy")
            return

        last = None
        while current.next != self.head and i < pozycja:
            last = current
            current = current.next
            i += 1

        if i == pozycja:
            if current.next == self.head:
                last.next = self.head 
                self.head.prev = last
            else:
                last.next = current.next
                current.next.prev = last
            print(f"Element na pozycji {pozycja} został usunięty z listy")
        else:
            print(f"Pozycja {pozycja} jest poza zakresem listy")


    def pokaz(self):
        self.elements = []  
        if not self.head:
            print("Lista jest pusta")
        else:
            current = self.head
            while True:
                self.elements.append(current.wartosc)
                current = current.next
                if current == self.head:
                    break
            print("Lista zawiera:", self.elements)
        
    def szukaj(self, wartosc):
        if wartosc in self.elements:
            print(f"Element {wartosc} znajduje się na liście")
        else:
            print(f"Element {wartosc} nie znajduje się na liście")

lista = CDLL()

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
 
