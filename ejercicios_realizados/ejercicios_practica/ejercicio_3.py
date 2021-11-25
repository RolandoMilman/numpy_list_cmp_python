# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas

import random

def generar_lista_0_10(numeros):
        print('Práctica con compresión de listas | Generadores')

       
        lista_0_10 = [x for x in numeros]
        print(lista_0_10)

def generar_tabla_5(numeros):
    lista_5 = [x*5 for x in numeros]
    print('Tabla múltiplicado por 5: ' , lista_5)

def generar_lista_random():
    print('Generar lista aleatoria con compresión de listas | Generadores')
    lista_random = [random.randint(1, 30)for x in range(10)]
    print('Lista random: ' , lista_random)



lista_generada = [2*x for x in range(10)]

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]
    numeros = [0, 1, 2, 3, 4,5,6,7,8,9,10]
    generar_lista_0_10(numeros)
       
    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista
    # Lo esperable es que realicen una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5.

    # tabla_5 = [......]
    generar_tabla_5(numeros)
    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar el módulo random y utilizar randrange
    # o randint para generar números aleatorios.
    # https://docs.python.org/3/library/random.html

    generar_lista_random()
    # dias_mes = [.....]
    print("terminamos")