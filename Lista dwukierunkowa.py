class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.elements = []
        
    def dodaj(self, wartosc, pozycja):
        new_node = Node(wartosc)

        if self.head is None:
            self.head = new_node
            print(f"Lista była pusta, dodano element {wartosc} na pozycję 0")
            return

        if pozycja == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print(f"Dodano element {wartosc} na pozycję 0")
            return

        current = self.head
        indeks = 0
        while current and indeks < pozycja - 1:
            current = current.next
            indeks += 1

        if current is None:
            print(f"Pozycja {pozycja} jest poza zakresem listy")
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            print(f"Dodano element {wartosc} na pozycję {pozycja}")

    def usun(self, pozycja):
        current = self.head
        last = None
        i = 0
        
        if not self.head:
            print("Lista jest pusta")
            return
        
        while i<=pozycja:
            if i == pozycja:
                if last is None:
                    self.head = current.next
                else:
                    last.next = current.next
                    current.prev = last
                print(f"Element {pozycja} został usunięty z listy")
                return
            i+=1
            last= current
            current = current.next
        
        print(f"Element {pozycja} nie znajduje się na liście")

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



lista = DLL()

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
