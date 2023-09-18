#el metodo sort()
#ordena alfabeticamente los elementos de una lista
#los cambios que hace sort() son permanentes

#el metodo sorted()
#tambien ordena alfabeticamente los elementos de una lista
#los cambios que hace sorted() son temporales

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print(sorted(colores)) #sorted lleva sus propios parentesis

#para ordenarlos en orden descendente (z-a)
#se utiliza reverse
colores.sort(reverse = True)
print(colores)


#para contar elementos podemos utilzar len()
#print(len(colores))
#esto imprime el numero total de la lista
