"""
Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    list = []
    first_value = 0
    second_value = 1
    print(first_value, second_value)

    list.append(first_value)
    list.append(second_value)

    for x in range(1, 49):
        new_value = second_value + first_value
        print(new_value)
        list.append(new_value)
        first_value = second_value
        second_value = new_value

    print(len(list))

fibonacci()
