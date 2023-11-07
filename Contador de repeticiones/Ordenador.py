lista = [1,1,1,2,2,3,3,3,3,66,66,666,66,1,2]

def ConRep():
    contador = []
    cantidad = len(lista)
    for i in range(0,cantidad):
        if lista[i] not in contador:
            contador.append(lista[i])
    for x in contador:
        repes = 0
        for i in lista:
            if i == x:
                repes = repes + 1
        print(x,repes,"\n")

ConRep()

