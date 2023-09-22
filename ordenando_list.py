####################################################
# objetivo: ordenar un objeto "list" sin utilizar  #
# el metodo list.sort                              #
####################################################

mazo = [21,4,7,3,1]
aux = 0
carta_anterior = 0

print("Mazo desordenado")          
print(mazo)


#recorro la cantidad de veces del list 
for i in range(0, len(mazo)-1):
      
     #ordeno en la pasada i de mayor a menor, ergo, queda el mayor al final
     #en la siguiente pasada se achica el rango de x
     for x in range(0, len(mazo)-i):
          #pregunto si no es la primera carta accede
          if x != 0:
           #si la carta anterior es mayor a la carta en x
           if carta_anterior > mazo[x]: 
            #cambio la cartas de lugar
            aux = mazo[x]
            mazo[x] = carta_anterior 
            mazo[x-1] = aux 
          
          carta_anterior = mazo[x]

print("Mazo ordenado")          
print(mazo)

  