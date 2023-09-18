#con el metodo len podemos contar la longitud de elementos

#con metodo del podemos eliminar un diccionario enter
#utilizando del nombreDiccionario,
#tambien podemos especificar en corchetes el nombre del elemento

#para añadir simplemente se esribe nombre["nuevacat"]="nuevovalor"

#primer diccionario
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #se elimina por completo el diccionario 1
del teclado2['Categoría'] #eliminamos la clave categoría
del teclado2['Precio']  #y precio
print(teclado2['Modelo'])
#solo queda la clave consola
