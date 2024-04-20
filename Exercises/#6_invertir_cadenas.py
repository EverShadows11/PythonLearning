"""

Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

def invertir_cadena(cadena):
    retval = ""
    for i in range(len(cadena) -1, -1, -1):
        retval += cadena[i]

    return retval


print(invertir_cadena("Hola"))




