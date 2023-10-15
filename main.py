from LinkedList import element
from LinkedList import linkedList
from ABR import node
from ABR import ABR
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
from hashTable import hashTable
import matplotlib.patches as mpatch
def createLinkedListFromGivenSet(K):
    newList = linkedList()
    for i in range (len(K)):
        newList.insert(element(K[i]))
    return newList
def createABRFromGivenSet(K):
    newABR = ABR()
    for i in range (len(K)):
        newABR.insert(node(K[i]))
    return newABR
def createHashTableFromGivenSet(K):
    newHashTable = hashTable(len(K))
    for i in range (len(K)):
        newHashTable.insert(K[i])
    return newHashTable
def testInsert(startDim, dimMax, dimIncrement, numPerDim):
    resultInsertLinkedList = []
    resultInsertABR = []
    resultInsertHash = []
    for i in range (startDim, dimMax, dimIncrement):

        totTimeLinkedList = 0
        totTimeABR = 0
        totTimeHash = 0
        U = []
        K = []
        for j in range(5000):
            U.append(j)
        for p in range(i):
            index = random.randint(0, len(U) - 1)
            K.append(U[index])
            U.remove(U[index])
        print(len(U))
        print(len(K))

        for r in range (1,numPerDim,1):

            keyToInsert = U[random.randint(0,len(U)-1)]

            #lavoro sempre su istanze di strutture dati "nuove"
            newLinkedList = createLinkedListFromGivenSet(K)
            elementToInsert = element(keyToInsert)
            startTimeStamp = timer()
            newLinkedList.insert(elementToInsert)
            finishTimeStamp = timer()
            iterationTimeLinkedList = (finishTimeStamp - startTimeStamp)
            totTimeLinkedList = totTimeLinkedList + iterationTimeLinkedList

            newABR = createABRFromGivenSet(K)
            nodeToInsert = node(keyToInsert)
            startTimeStamp = timer()
            newABR.insert(nodeToInsert)
            finishTimeStamp = timer()
            iterationTimeABR = (finishTimeStamp - startTimeStamp)
            totTimeABR = totTimeABR + iterationTimeABR

            newHashTable = createHashTableFromGivenSet(K)
            startTimeStamp = timer()
            newHashTable.insert(keyToInsert)
            finishTimeStamp = timer()
            newHashTable.printHashTable()
            iterationTimeHashTable = (finishTimeStamp - startTimeStamp)
            totTimeHash = totTimeHash + iterationTimeHashTable

        resultInsertLinkedList.append((totTimeLinkedList/numPerDim)*1000)
        resultInsertABR.append((totTimeABR/numPerDim)*1000)
        resultInsertHash.append((totTimeHash/numPerDim)*1000)

    x_axis = [i for i in range(startDim, dimMax, dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultInsertLinkedList, label="LinkedList insert ", color="orange")
    plot1.plot(x_axis, resultInsertABR, label="ABR insert ", color="green")
    plot1.plot(x_axis, resultInsertHash, label="HashTable insert ", color="blue")
    plot1.set_title("Risultati per Insert implementata con le s3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione vettore")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    insertLinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    insertABR_patch = mpatch.Patch(color='green', label='ABR')
    insertHash_patch = mpatch.Patch(color='blue', label='Hash')
    plot1.legend(handles=[insertLinkedList_patch, insertABR_patch, insertHash_patch])
    plt.show()
def testSearch(startDim, dimMax, dimIncrement, numPerDim):
    resultSearchLinkedList = []
    resultSearchABR = []
    resultSearchHash = []
    for i in range (startDim, dimMax, dimIncrement):
        totTimeLinkedList = 0
        totTimeABR = 0
        totTimeHash = 0
        U = []
        K = []
        for j in range(5000):
            U.append(j)
        for p in range(i):
            index = random.randint(0, len(U) - 1)
            K.append(U[index])
            U.remove(U[index])
        print(len(U))
        print(len(K))

        for r in range (1,numPerDim,1):

            keyToSearch = K[random.randint(0,len(K)-1)]

            #lavoro sempre su istanze di strutture dati "nuove"
            newLinkedList = createLinkedListFromGivenSet(K)
            startTimeStamp = timer()
            newLinkedList.search(keyToSearch)
            finishTimeStamp = timer()
            iterationTimeLinkedList = (finishTimeStamp - startTimeStamp)
            totTimeLinkedList = totTimeLinkedList + iterationTimeLinkedList

            newABR = createABRFromGivenSet(K)
            startTimeStamp = timer()
            newABR.search(keyToSearch)
            finishTimeStamp = timer()
            iterationTimeABR = (finishTimeStamp - startTimeStamp)
            totTimeABR = totTimeABR + iterationTimeABR

            newHashTable = createHashTableFromGivenSet(K)
            startTimeStamp = timer()
            newHashTable.search(keyToSearch)
            finishTimeStamp = timer()
            newHashTable.printHashTable()
            iterationTimeHashTable = (finishTimeStamp - startTimeStamp)
            totTimeHash = totTimeHash + iterationTimeHashTable

        resultSearchLinkedList.append((totTimeLinkedList/numPerDim)*1000)
        resultSearchABR.append((totTimeABR/numPerDim)*1000)
        resultSearchHash.append((totTimeHash/numPerDim)*1000)

    x_axis = [i for i in range(startDim, dimMax, dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultSearchLinkedList, label="LinkedList insert ", color="orange")
    plot1.plot(x_axis, resultSearchABR, label="ABR insert ", color="green")
    plot1.plot(x_axis, resultSearchHash, label="HashTable insert ", color="blue")
    plot1.set_title("Risultati per Search implementata con le 3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione vettore")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    searchLinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    searchABR_patch = mpatch.Patch(color='green', label='ABR')
    searchHash_patch = mpatch.Patch(color='blue', label='Hash')
    plot1.legend(handles=[searchLinkedList_patch, searchABR_patch, searchHash_patch])

    plt.show()
def testDelete(startDim, dimMax, dimIncrement, numPerDim):
    resultDeleteLinkedList = []
    resultDeleteABR = []
    resultDeleteHash = []
    for i in range (startDim, dimMax, dimIncrement):

        totTimeLinkedList = 0
        totTimeABR = 0
        totTimeHash = 0
        U = []
        K = []
        for j in range(5000):
            U.append(j)
        for p in range(i):
            index = random.randint(0, len(U) - 1)
            K.append(U[index])
            U.remove(U[index])
        print(len(U))
        print(len(K))

        for r in range (1,numPerDim,1):
            print("iterazione n°",r)
            keyToDelete = K[random.randint(0,len(K)-1)]

            #lavoro sempre su istanze di strutture dati "nuove"
            newLinkedList = createLinkedListFromGivenSet(K)
            startTimeStamp = timer()
            newLinkedList.delete(keyToDelete)
            finishTimeStamp = timer()
            iterationTimeLinkedList = (finishTimeStamp - startTimeStamp)
            totTimeLinkedList = totTimeLinkedList + iterationTimeLinkedList

            newABR = createABRFromGivenSet(K)
            nodeToDelete = newABR.search(keyToDelete)
            startTimeStamp = timer()
            newABR.delete(nodeToDelete)
            finishTimeStamp = timer()
            iterationTimeABR = (finishTimeStamp - startTimeStamp)
            totTimeABR = totTimeABR + iterationTimeABR

            newHashTable = createHashTableFromGivenSet(K)
            startTimeStamp = timer()
            newHashTable.delete(keyToDelete)
            finishTimeStamp = timer()
            iterationTimeHashTable = (finishTimeStamp - startTimeStamp)
            totTimeHash = totTimeHash + iterationTimeHashTable

        resultDeleteLinkedList.append((totTimeLinkedList/numPerDim)*1000)
        resultDeleteABR.append((totTimeABR/numPerDim)*1000)
        resultDeleteHash.append((totTimeHash/numPerDim)*1000)

    x_axis = [i for i in range(startDim, dimMax, dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, resultDeleteLinkedList, label="LinkedList delete ", color="orange")
    plot1.plot(x_axis, resultDeleteABR, label="ABR delete ", color="green")
    plot1.plot(x_axis, resultDeleteHash, label="HashTable delete ", color="blue")
    plot1.set_title("Risultati per Delete implementata con le 3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione vettore")

    deleteLinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    deleteABR_patch = mpatch.Patch(color='green', label='ABR')
    deleteHash_patch = mpatch.Patch(color='blue', label='Hash')
    plot1.legend(handles=[deleteLinkedList_patch, deleteABR_patch, deleteHash_patch])

    plt.show()

if __name__ == '__main__':
    startDim = 1
    dimMax = 1000
    dimIncrement = 100
    numPerDim = 100
    testInsert(startDim, dimMax, dimIncrement, numPerDim)
    testSearch(startDim, dimMax, dimIncrement, numPerDim)
    testDelete(startDim, dimMax, dimIncrement, numPerDim)


