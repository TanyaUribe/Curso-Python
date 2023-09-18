#con condicional elif
#podemos añadir cuantas condiciones queramos a las condiciones IF

#el operador and se utiliza para hacer que dos condiciones deban cumplirse para
#que se ejecute el codigo (ambas deben ser true)

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
#input() es para que el usuario introduzca un dato
#por default, input almacena datos como strings, por eso se le define como int aquí
        
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad. Joven adulto.')
elif edad > 45 and edad < 100:
	print('Eres mayor de edad. Adulto - Adulto mayor ')
elif edad >= 100 and edad <= 120:
	print('Eres aún más mayor de edad.')
else:
	print('Edad no válida.')
