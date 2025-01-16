from nodo import Nodo
from grafo import Grafo

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

#da sistemare bene

g = Grafo(nodo1)
g.addNodo(nodo2, nodo1)
g.addNodo(nodo3, nodo1)
g.addNodo(nodo2, nodo3)
g.addNodo(nodo3, nodo2)

#fino a qui

for i in range(g.getSize() - 1):
    
    print()
    x = g.getListaNodi()
    cont = x[i].getCont()
    print(cont)
    y = g.getListeAdiacenza()
    l = y[i]
    print()

    for j in range(len(l)):
        adiacente = l[j]
        print(adiacente.getCont())