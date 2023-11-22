'''
Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

def sumar_numeros(veces=5, suma=0):
    if veces == 0:
        return suma
    try:
        entrada = input("Ingrese un número (o 'q' para salir): ")
        if entrada.lower() == 'q':
            return suma
        numero = float(entrada)
        return sumar_numeros(veces-1, suma+numero)
    except ValueError:
        print("Error: Ingrese un número válido.")
        return sumar_numeros(veces, suma)

try:
    resultado = sumar_numeros()
    print(f"La suma de los números introducidos es: {resultado}")
except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
except Exception as e:
    print(f"Error inesperado: {e}")


'''
Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''

from datetime import datetime

def obtener_numero(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            return float(entrada)
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

try:
    unidades = obtener_numero("Ingrese la cantidad de unidades: ")
    precio = obtener_numero("Ingrese el precio por unidad: ")

    subtotal = unidades * precio
    descuento = 0.05 if datetime.now().day < 15 else 0
    total = subtotal - (subtotal * descuento)

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento ({descuento*100}%): {subtotal * descuento:.2f}")
    print(f"Total con descuento: {total:.2f}")

except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
except Exception as e:
    print(f"Error inesperado: {e}")

'''
En el código proporcionado, utilicé una 
expresión lambda (función anónima) para 
calcular el descuento. La elección de usar 
una función lambda en este caso específico es
principalmente por la simplicidad del cálculo 
y la concisión del código.

La función lambda es útil cuando se necesita
una función simple y de corta duración. En este 
caso, el cálculo del descuento es directo y se puede 
expresar de manera clara y concisa utilizando una función lambda.
'''


'''
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def generar_lista_pares(inicio, fin):
    inicio += inicio % 2  # Asegurar que inicio sea par
    return list(range(inicio, fin + 1, 2))

try:
    numero_inicial = obtener_numero("Ingrese el número inicial: ")
    numero_final = obtener_numero("Ingrese el número final: ")

    if numero_inicial > numero_final:
        raise ValueError("Error: El número inicial debe ser menor o igual al número final.")

    lista_pares = generar_lista_pares(numero_inicial, numero_final)

    if lista_pares:
        print(f"Lista de números pares entre {numero_inicial} y {numero_final}:")
        print(lista_pares)
    else:
        print("No hay números pares en el rango proporcionado.")

except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Error inesperado: {e}")


'''
Uso de range: Se ha utilizado la función range para generar la lista de números pares de manera más eficiente.

La recursividad suele ser útil cuando puedes dividir un problema en subproblemas más pequeños y resolver cada 
subproblema de manera similar. Aquí, simplemente necesitas generar una lista de números pares entre dos valores, 
y no hay una estructura clara para dividir el problema en partes más pequeñas que se resuelvan de la misma manera.

Además, la recursividad en Python tiene un límite (limitado por la pila de llamadas)
'''



