from LinkedList import element
from LinkedList import linkedList
from ABR import node
from ABR import ABR
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
from hashTable import hashTable
import matplotlib.patches as mpatch
import numpy as np
import os
from numpy import ndarray
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

            #lavoro sempre su istanze di strutture dati "nuove", così non sono alterate dalle iterazioni precedenti
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
    plot1.set_title("Risultati per Insert implementata con le 3 strutture dati")
    plot1.set_ylabel("tempo impiegato (millisecondi)")
    plot1.set_xlabel("dimensione vettore")

    # aggiungo a entrambi i grafici una piccola legenda visiva
    insertLinkedList_patch = mpatch.Patch(color='orange', label='Linked List')
    insertABR_patch = mpatch.Patch(color='green', label='ABR')
    insertHash_patch = mpatch.Patch(color='blue', label='Hash')
    plot1.legend(handles=[insertLinkedList_patch, insertABR_patch, insertHash_patch])
    plt.show()

    # crea la catella per le tabelle se non esiste
    if not os.path.exists("tables"):
        os.makedirs("tables")

    # Disegna la tabella
    traceTables(
        *[
            [
                [i for i in range(startDim, dimMax, dimIncrement)],
                ["{:.3e}".format(val) for val in resultInsertLinkedList],
                ["{:.3e}".format(val) for val in resultInsertABR],
                ["{:.3e}".format(val) for val in resultInsertHash],
            ],
            (
                "Nr elementi",
                "Insert",
                "Linked List",
                "ABR",
                "HashTable"
            ),
            "Inserimento eseguito sulle 3 strutture dati",
        ]
    )

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

    # crea la catella per le tabelle se non esiste
    if not os.path.exists("tables"):
        os.makedirs("tables")

    # Disegna la tabella
    traceTables(
        *[
            [
                [i for i in range(startDim, dimMax, dimIncrement)],
                ["{:.3e}".format(val) for val in resultSearchLinkedList],
                ["{:.3e}".format(val) for val in resultSearchABR],
                ["{:.3e}".format(val) for val in resultSearchHash],
            ],
            (
                "Nr elementi",
                "Search",
                "Linked List",
                "ABR",
                "HashTable"
            ),
            "Ricerca eseguita sulle 3 strutture dati",
        ]
    )
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

    # crea la catella per le tabelle se non esiste
    if not os.path.exists("tables"):
        os.makedirs("tables")

    # Disegna la tabella
    traceTables(
        *[
            [
                [i for i in range(startDim, dimMax, dimIncrement)],
                ["{:.3e}".format(val) for val in resultDeleteLinkedList],
                ["{:.3e}".format(val) for val in resultDeleteABR],
                ["{:.3e}".format(val) for val in resultDeleteHash],
            ],
            (
                "Nr elementi",
                "Delete",
                "Linked List",
                "ABR",
                "HashTable"
            ),
            "Cancellazione eseguita sulle 3 strutture dati",
        ]
    )
def traceTables(columns: list, headers: tuple, title: str):
    fig, ax = plt.subplots(figsize=(8, 10))

    # Dati per il plot della tabella (è necessario convertire in it is necessary to convert il tutto in un array numpyy)
    data = np.column_stack(columns)

    # Setta il titolo delle tabella
    ax.axis("off")
    table = ax.table(cellText=data, colLabels=headers, loc="center", cellLoc="center")
    table.auto_set_column_width(col=list(range(len(columns))))
    table.scale(1, 1.5)

    # Colora i titoli e le righe pari
    cell_colors = {
        cell: ("#ffd1d1", {"weight": "bold"})
        if table[cell].get_text().get_text() in headers
        else ("#ffe4e4", {})
        for cell in table._cells
        if cell[0] % 2 == 0
    }
    for cell, (color, text_props) in cell_colors.items():
        # setta il colore delle celle
        table[cell].set_facecolor(color)
        # set the text properties of the cell
        table[cell].set_text_props(**text_props)
        # ** used to expand the dictionary

    # save the plot as a png file
    fig.savefig(f"tables/{title}.png", dpi=300, bbox_inches="tight")
    # clear figure for the next plot
    plt.clf()

if __name__ == '__main__':
    startDim = 1
    dimMax = 1000 #5000
    dimIncrement = 50 #250
    numPerDim = 100 #1000
    #testInsert(startDim, dimMax, dimIncrement, numPerDim)
    #testSearch(startDim, dimMax, dimIncrement, numPerDim)
    #testDelete(startDim, dimMax, dimIncrement, numPerDim)

