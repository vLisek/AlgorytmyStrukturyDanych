from collections import OrderedDict

class LRUCache:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.cache = OrderedDict()

    def get(self, klucz):
        if klucz not in self.cache:
            return None
        self.cache.move_to_end(klucz)
        return self.cache[klucz]

    def put(self, klucz, wartosc):
        if klucz in self.cache:
            self.cache[klucz] = wartosc
            self.cache.move_to_end(klucz)
            return

        if len(self.cache) >= self.pojemnosc:
            self.cache.popitem(last=False)

        self.cache[klucz] = wartosc

cache = LRUCache(pojemnosc=2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))

cache.put("c", 3)
print(cache.get("b"))
print(cache.get("c"))