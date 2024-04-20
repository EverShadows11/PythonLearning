### ANAGRAMA ###

"""
Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def es_un_anagrama(first_value: str, second_value: str):
    if first_value == second_value:
        return False

    first_value = first_value.replace(' ', '').lower()
    second_value = second_value.replace(' ', '').lower()

    if not len(first_value) == len(second_value):
        return False

    for i in first_value:
        first_count = first_value.count(i)
        second_count = second_value.count(i)
        if not first_count == second_count:
            return False

    return True



prueba_anagrama = es_un_anagrama("animales", "Milanesa")
if prueba_anagrama:
    print("SI es un anagrama")
else:
    print("NO es un anagrama")

es_un_anagrama("Hola", "Funcion")