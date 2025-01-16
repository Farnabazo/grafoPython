class Nodo:

    #cont è il contenuto del nodo e può essere qualsiasi cosa
    #listaAdiacenza è la lista di tutti i nodi adiacenti all'istanza del Nodo in questione

    def __init__(self, cont):
        self.listaAdiacenza = []
        self.cont = cont
    
    def getCont(self):
        return self.cont
    
    def getListaAdiacenza(self):
        return self.listaAdiacenza
    
    #aggiungo un nodo alla lista di adiacenza, da usare nella classe grafo
    
    def addListaAdiacenza(self, newNodo):
        self.listaAdiacenza.append(newNodo)

    def isEqual(self, x):
        return self.cont == x.cont