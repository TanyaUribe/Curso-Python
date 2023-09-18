#el metodo pop()
#elimina un elemento de una lista y lo almacena en otra variable
#tambien utiliza parentesis

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#se escribe el nombre de la lista, el método pop y dentro de los parentesis el nombre del elemento a eliminar
#el elemento eliminado se almacena en una variable
color1 = colores.pop(1)
color2 = colores.pop(-2)

print(colores)
print(color1 + ", " + color2)

#si se utiliza solo (sin especificar posicion) se elimina el último elemento
