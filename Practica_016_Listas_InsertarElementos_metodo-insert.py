#el metodo insert()
#añade un elemento en cualquier posición de la lista

#el elemento nuevo se posicionará en el lugar del elemento
#que ocupaba la posición que especificamos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#se escribe el nombre de la lista, el método append
#y entre parentesis, la posición se especifica en el primer parametro,
#y en el segundo el elemento a añadir

#se pueden utilizar posiciones negativas, pero funcionan algo distinto
#si ponemos -1, el nuevo elemento se posiciona en la penultima posicion
#con -2 en la posicion antes de la penultima posicion y asi sucesivamente

colores.insert(-4,"magenta")
colores.insert(-1,"turquesa")
print(colores)
