"""
* Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

"""

# Triangulo: a * b / 2
# Cuadrado: l^2
# Rectangulo: a * b

def calcular_area (poligono, a, b=0):
  if poligono == "triangulo":
    print("a*b/2")
    return (a * b) / 2

  if poligono == "cuadrado":
    print("lado^2")
    return a * a

  if poligono == "rectangulo":
   print("a * b")
   return a * b


print(calcular_area("triangulo", 3, 5))
print(calcular_area("cuadrado", 4))
print(calcular_area("rectangulo", 2, 3))


