#el bucle while
#ejecuta una serie de declaraciones eiempre que la condicion se cumpla (TRUE)
#cuando es false se deja de ejecutar el codigo

#utilizamos el break para salir de un bucle independientemente
#de que se esté ejecutando
x = 0

while x <= 30:
	x += 1
	# x va aumentando en incrementos de 1

	if x == 4 or x == 6 or x == 10: #OR debe cumplirse cualquiera de las condiciones para que sea true
		print("Se saltó el valor ", x, " de x")
		continue
                #si x es 4, 6 o 10 los salta con continue
	
	#if para romper la ejecución del bucle
	if x == 15:
		print("Se rompió la ejecución del bucle cuando x valía: ", x)
		break
                #para imprimir una variable se pone , despues del string y se añade la variable

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)
