#user function

def sumar(i,j):
     return i+j

suma_anonima=lambda i,j:i+j
print(f"El total de la suma anonima con lambda es {suma_anonima}") #funcion anonima/lambda

def sumar_default(i,j,k=15):
    return i+j+k

def sumar_variable(*args):
    total=0
    for i in args:
        total+=i
    return total


suma=sumar(4,5)
print(f"El total de la suma es {suma}")

suma2=sumar_default(4,5)
print(f"El total de la suma con argumentos default es {suma2}")

suma3=sumar_variable(5,9,4,7)
print(f"la suma totalk de una funcion con argumentos variables es {suma3}")

#recursividad: una función que se llama a si misma las veces que haga falta.

def factorial(n):
    if n == 1:
        return n
    elif n <= 0:
        print("No hay factorial para 0 o menor que 0")
    else:
        return n*factorial(n-1) #recursividad porque se llama a si misma

resultado_factorial=factorial(5)
print(f"El factorial es {resultado_factorial}")




