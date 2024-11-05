#Teoría de Control II Parcial 2 - 20310392

import numpy as np
import matplotlib.pyplot as plt

def calcular_compensador(polo_x, polo_y):
    # Coordenadas del polo deseado
    polo = np.array([polo_x, polo_y])
    line_horizontal = np.array([[polo_x, polo_y], [polo_x - 100, polo_y]]) #Paso 1: Línea horizontal de P hacia la izq

    line_to_origin = np.array([[polo_x, polo_y], [0, 0]]) #Paso 2: Línea de P al origen
    angulo_origen = np.arctan2(polo_y, polo_x) #angulo línea a origen

    angulo_horizontal = 0  # ángulo de la línea horizontal, Horizontal es 0 radianes

    #Paso 3
    angulo_bisectriz = (angulo_horizontal - angulo_origen) / 2 #angulo entre línea horizontal y línea hacia el origen para bisectriz
    bisectriz = angulo_horizontal + angulo_bisectriz # Sumar el ángulo bisectriz al ángulo horizontal para obtener la bisectriz

    longitud = 100  # Longitud total de la línea bisectriz
    bisectriz_x1 = polo_x - longitud * np.cos(bisectriz)
    bisectriz_y1 = polo_y + longitud * np.sin(bisectriz)

    bisectriz_x2 = polo_x + longitud * np.cos(bisectriz)
    bisectriz_y2 = polo_y - longitud * np.sin(bisectriz)

    plt.figure(figsize=(10, 6)) #grafica
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')

    plt.plot(line_horizontal[:, 0], line_horizontal[:, 1], color='gray', linestyle='--')
    plt.plot(line_to_origin[:, 0], line_to_origin[:, 1], 'g--')

    #bisectriz
    plt.plot([bisectriz_x1, bisectriz_x2], [bisectriz_y1, bisectriz_y2], 'm:', label='Bisectriz')

    angulo2=angulo/2 # Paso 4: Líneas de contribucion de angulo
    angulo_izquierdo = bisectriz - np.radians(angulo2)
    angulo_derecho = bisectriz + np.radians(angulo2)

    # Paso 5: Intersecciones con el eje real (y = 0)
    x_izquierdo = polo_x + (polo_y / np.tan(angulo_izquierdo))
    x_derecho = polo_x + (polo_y / np.tan(angulo_derecho))

    # Líneas de contribucion de angulo
    plt.plot([polo_x, x_izquierdo], [polo_y, 0], 'b-')
    plt.plot([polo_x, x_derecho], [polo_y, 0], 'c-')

    plt.plot(polo_x, polo_y, marker='o',color='gray', label='P')
    plt.plot(x_izquierdo, 0,marker='o',
         markeredgecolor='blue', markerfacecolor='white', label='Zc')
    plt.plot(x_derecho, 0, 'cx', label='Pc')

    plt.xlim(-10, 10)
    plt.ylim(-5, 5)
    plt.title('Método geométrico para el compensador de adelanto')
    plt.xlabel('Eje Real')
    plt.ylabel('Eje Imaginario')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.grid()
    plt.legend()
    plt.show()

    return x_izquierdo, x_derecho

# datos
polo_x = float(input("Ingrese la coordenada del eje real del polo deseado: "))
polo_y = float(input("Ingrese la coordenada del eje imaginario del polo deseado: "))
angulo = float(input("Ingrese la contribución de ángulo deseada (Φ): "))

# Calcular y graficar
cero_izquierdo, cero_derecho = calcular_compensador(polo_x, polo_y)
print(f"Polo del compensador: {cero_derecho}")
print(f"Cero del compensador: {cero_izquierdo}")
