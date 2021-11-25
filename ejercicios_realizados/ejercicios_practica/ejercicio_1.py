# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # Crear una funcion lambda que multiplique por 2
    # el valor pasado a la función

    print()
    print('Función lambda')   
    print('Lista origen de números:   ',numeros)
    numeros_lambda = list(map(lambda x: 2*x, numeros))
    print('Lista multiplicada por 2 en el lambda:  ',numeros_lambda)
    # [2, -10, -12, 8]

    # numeros_potencia = list(map....)
    print()
    print('Función list map')
    print('Lista origen de números:   ',numeros)
    mult_by_2 = lambda x: 2*x    
    numeros_mult_by_2 = list(map(mult_by_2, numeros))
    print('Lista nueva multiplicada por 2 en el list map: ', numeros_mult_by_2)

    print("terminamos")