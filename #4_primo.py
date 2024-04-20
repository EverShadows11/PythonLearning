"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""


def es_primo(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def imprime_primos():
    for i in range(1,101):
        prueba_primo = es_primo(i)
        if prueba_primo:
            print(i)
            """
            print(i, " Si es primo")
        else:
            print(i, " No es primo")
            """

imprime_primos()