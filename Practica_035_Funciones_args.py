#*args son argumentos arbitrarios
#tienen un amplio uso y se pueden utilizar de manera muy flexible

def colores(*args):
	pass
#se definen los argumentos para la funcion
colores('rojo', 'azul', 'verde', 'amarillo') #se utilizan 4 argumentos
colores('lila', 'negro', 'rojo')        #3 argumentos
colores('rosa')         #1 argumento
colores('marrón', 'naranja')    #2 argumentos


def colores1(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores1("verde","azul")


def suma(*args):
        res = args[0] + args[1] + args[2] + args[3] + args[-1]
        print("El resultado es: ",res) #la suma de los argumentos se imprime
suma(1,2,3,4,5) #se definen los argumentos a sumar


