from nodo import Nodo
from grafo import Grafo

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

g = Grafo(nodo1)
g.addNodo(nodo2, nodo1)
g.addNodo(nodo3, nodo1)

for i in range(g.getSize()):
    
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