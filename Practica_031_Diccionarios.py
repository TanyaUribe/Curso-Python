#los diccionarios son capaces de almacenar una coleccion de objetos
#con claves y valores

#primer diccionario
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
        #cada diccionario contiene 3 claves (keys) con sus respectivos valores
}

#segundo diccionario
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

#se pueden imprimir con un print
print("El modelo", teclado2['Modelo'], "cuesta: $", teclado2['Precio'])
