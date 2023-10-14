from LinkedList import element
from LinkedList import linkedList
from ABR import node
from ABR import ABR
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
from hashTable import hashTable

def createListConc(n,U):
    newList = linkedList()
    for i in range (n):
        key = random.randint(0,len(U)-1)
        U.remove(key)
        newList.insert(element(key))
    return newList
def createABR(n,U):
    newTree = ABR()
    for i in range (n):
        key = random.randint(0, len(U) - 1)
        U.remove(key)
        newTree.insert(node(key))
    return newTree

def createHashTable(n,U):
    newHashTable = hashTable(n)
    for i in range (n):
        key = random.randint(0, len(U)-1)
        U.remove(key)
        newHashTable.insert(key)
    return newHashTable


if __name__ == '__main__':
    #creo l'insieme universo U (ciop l'insieme delle chiavi ammissibili. Esso va da 0 a 4999)
    U = []
    for i in range (5000):
        U.append(i)

    startDim = 50
    dimMax = 1000
    dimIncrement = 50





