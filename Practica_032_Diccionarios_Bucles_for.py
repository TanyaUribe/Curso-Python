#los diccionarios son capaces de almacenar una coleccion de objetos
#con claves y valores

#los valores de un diccionario se pueden modificar
#llamando a la posición del elemento y dandole el nuevo valor

#primer diccionario
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

#esta iteracion devuelve las 3 claves con sus valores
for x in teclado1:
	print(x, '=', teclado1[x] + '.')
	#x para claves, diccionario[x] para valores
