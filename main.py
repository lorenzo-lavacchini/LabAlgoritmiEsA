from LinkedList import element
from LinkedList import listConc
from ABR import node
from ABR import ABR
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
from hashTable import hashTable
if __name__ == '__main__':
    n = 50
    table = hashTable(n)
    table.insert(6)
    table.insert(68)
    table.printHashTable()

