#utilizando in podemos biscar un elemento en una lista o tupla

tupla = ("azul","indigo","morado","verde")
#si aqui imprimieramos ("azul" in tupla) nos devolvería un TRUE

color = input("Introduce un color: \n")
if color in tupla[0]: #podemos especificar la posicion del elemento a buscar
        print("El color azul esta admitido")
elif color in tupla[1]:
        print("El color indigo esta admitido")
elif color in tupla[2]:
        print("El color morado esta admitido")
elif color in tupla[3]:
        print("El color verde esta admitido")
else:
        print("El color no esa permitido")
