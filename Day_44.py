class MyHashSet:

    def __init__(self):
        self.myHashSet = set()

    def add(self, key: int) -> None:
        self.myHashSet.add(key)  

    def remove(self, key: int) -> None:
        self.myHashSet.discard(key) 

    def contains(self, key: int) -> bool:
        return key in self.myHashSet  
