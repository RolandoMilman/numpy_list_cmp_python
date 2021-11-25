# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas
def comprension_datos_str(list_numeros_str):
    
    # Utilizamos "isdigit" para evaluar si el string tiene forma de numero,
    # en caso de ser un caracter o un string vacio "isdigit" retorna "False"

    lista_filtrada = [int(x) for x in list_numeros_str if x.isdigit() is True]
    
    print(lista_filtrada)

    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    comprension_datos_str(list_numeros_str)
    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?

    list_numeros_str = ['5', '-2', '3', '', '-7', 'NaN']

    comprension_datos_str(list_numeros_str)

    print("terminamos")