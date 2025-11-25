class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def dodaj_na_koniec(self, data):
        nowy_wezel = Node(data)
        if not self.head:
            self.head = nowy_wezel
            return
        ostatni = self.head
        while ostatni.next:
            ostatni = ostatni.next
        ostatni.next = nowy_wezel

    def do_listy(self):
        elementy = []
        obecny = self.head
        while obecny:
            elementy.append(obecny.data)
            obecny = obecny.next
        return elementy


def usun_duplikaty(ll):
    if not ll.head:
        return

    widziane = set()
    obecny = ll.head
    poprzedni = None

    while obecny:
        if obecny.data in widziane:
            poprzedni.next = obecny.next
        else:
            widziane.add(obecny.data)
            poprzedni = obecny

        obecny = obecny.next

ll = LinkedList()
for x in [1, 2, 2, 3, 3, 1, 4, 5]:
    ll.dodaj_na_koniec(x)

usun_duplikaty(ll)
print(ll.do_listy())