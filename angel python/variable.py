#esto es un comentario de una sola linea
"""esto es un comentario de 
varias lineas"""

#iniciando variables
nombre="nombre del estudiante" 
edad=58
estado=True
nota=5.0

#mostar el contenido de las variables print()
print(nombre)
print(edad)
print(estado)
print(nota)

#que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos a utilizar la funcion input para recoger datos del teclado
nombre=input("¿como te llamas? " )
edad=input("¿q edad tienes? ")
estado=input("¿en que estado te encuentras?" )
nota=input("¿cual es tu nota? ")

#para visualizar que guardamos en las tablas anteriores
print("hola,",nombre,"un gusto conocerte")
print("tu edad es:",edad)
print(" tu estado es:",estado)
print("tu nota es:",nota)