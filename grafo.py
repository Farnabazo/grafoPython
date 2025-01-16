from nodo import Nodo

class Grafo:

    #definisco un insieme di nodi a partire da un nodo centrale e la sua dimensione (1 inizialmente)

    def __init__(self, firstNodo):
        self.size = 1
        self.firstNodo = firstNodo
        self.listaNodi = [firstNodo]



    def addNodo(self, newNodo, oldNodo):

        #siccome il grafo non è orientato, non si possono creare cappi

        if newNodo.isEqual(oldNodo):
            print("Non puoi collegare un nodo a sé stesso")
            return

        checkNewNodo = False

        #per ogni nodo nella lista, verifico che il nodo che dovrà essere adiacente al nuovo sia presente (altrimenti il metodo non verra eseguito)
        #e che non sia già presente il nuovo nodo

        for n in range(len(self.listaNodi)):
            x = self.listaNodi[n]

            if newNodo.isEqual(x):
                checkNewNodo = True

            if oldNodo.isEqual(x):
                break

            #se raggiungo l'ultimo nodo della lista e comunque è diverso dal nodo passato come oldNodo, allora so che non è presente

            elif not oldNodo.isEqual(x) and n == len(self.listaNodi):
                print("Il nodo adiacente non è presente")
                return

        if checkNewNodo == False:
            self.listaNodi.append(newNodo)
            self.size += 1

        #essendo il grafo non orientato, (x -> y) implica sempre (y -> x)

        if not newNodo in oldNodo.getListaAdiacenza():
            oldNodo.addListaAdiacenza(newNodo)

        if not oldNodo in newNodo.getListaAdiacenza():
            newNodo.addListaAdiacenza(oldNodo) 


        
    def getSize(self):
        return self.size
    

    
    def getFirstNodo(self):
        return self.firstNodo
    

    
    def getListaNodi(self):
        return self.listaNodi
    

    
    def getListeAdiacenza(self):

        #salvo tutte le liste in una lista di liste

        listeAdiacenza = []

        #per ogni nodo x nella lista dei nodi, aggiungo la sua lista di adiacenza alla lista di liste

        for n in range(len(self.listaNodi)):
            x = self.listaNodi[n]
            listeAdiacenza.append(x.getListaAdiacenza())
        return listeAdiacenza
    
    #override
    
    def print(self):

        for i in range(self.size):
            print()
            x = self.listaNodi
            cont = x[i].getCont()
            print(cont)
            y = self.getListeAdiacenza()
            l = y[i]
            print()

            for j in range(len(l)):
                adiacente = l[j]
                print(adiacente.getCont())