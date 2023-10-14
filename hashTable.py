import LinkedList
from LinkedList import element
from LinkedList import linkedList
class hashTable:
   
    #m -> grandezza della tabella
    #n -> numero di chiavi da memorizzare nella tabella (cardinalità di K)
    def __init__(self,n):
        self.m = (int)(n / 0.8)
        self.T = [linkedList] * self.m
        for i in range(self.m):
            self.T[i] = linkedList()


    def hashFunction(self, k):
        return k % self.m

    def insert(self,k):
        self.T[self.hashFunction(k)].insert(element(k))

    def search(self,k):
        self.T[self.hashFunction(k)].search(k)

    def delete(self,k):
        self.T[self.hashFunction(k)].delete(k)

    def printHashTable(self):
        for i in range(0,len(self.T)):
            print("Lista n°",i)
            print(self.T[i].printAll())
