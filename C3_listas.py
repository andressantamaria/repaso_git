#colección de elementos en un orden determinado
bicicletas = ['trek', 'redline', 'avispa']
print(bicicletas)

elemento = 1
#acceder a elementos mediante índice
#Los elementos comienzan en el índice 0, ¡NO UNO!
print(f"Este es elemento {elemento + 1} de bicicletas: {bicicletas[elemento]}")

#como son string podemos usar los métodos de strings.
print(f"Este es elemento {elemento + 1} de bicicletas: {bicicletas[elemento].title()}")

#Los índices negativos nos permiten recorrer la lista en orden inverso, de adelante hacia atrás. 
elemento = -3
print(f"Este es elemento {elemento} de bicicletas: {bicicletas[elemento]}")
elemento = -1
print(f"Este es elemento {elemento} de bicicletas: {bicicletas[elemento]}")

#guardar cadenas con f string
mensaje = f"Este es elemento {elemento} de bicicletas: {bicicletas[elemento].title()}"
print(mensaje)

#
#Escogiendo, agregando y eliminando elementos
#
motos = ["royal enfield","honda","yamaha"]

#Modificar
motos[2]='ducati'
print(motos)

#Agregar, se hace al final de la lista
motos.append("yamaha")
print(motos)

#inserción (se hace en un índice específico)
motos.insert(0, 'harley davidson')
print(motos)

#elimninar elementos con índice específico
del motos[0]
print(motos)

#elimninar elementos con método pop(), el último elemento
motos.pop()
print(motos)

#también podemos almacenar la variable eliminada con pop
ultimo = motos.pop()
print(ultimo)
print(motos)

motos.append('harley davidson')
motos.append('ducati')
motos.append('yamaha')

#uso de pop para eliminar índice específico
print(motos)
motos.pop(2)
print(motos)

#eliminar item por valor
motos.remove('ducati')
print(motos)

#ordenamiento

#método sort(), cambia la lista de forma permanente
motos.sort()
print(motos)

#orden inverso
motos.sort(reverse=True)
print(motos)

#orden temporal con la función sorted().
print(sorted(motos))
print(motos)

#orden inverso. Permite recorrer el orden de adelante hacia atrás
deportivos = ['lamborhini', 'ferrari', 'maserati', 'bugatti', 'rools royce', 'bentley', 'pagani', 'aston martin', 'porsche']
print(deportivos)
deportivos.reverse()
print(deportivos)

#logitud de una lista.
print(len(deportivos))
print(len(motos))
variable = len(deportivos)
print(f"longitud deportivos: {variable}")

#"list index out of range"
# print(motos[8])

#++++++++++++++++++++
#TRABAJANDO CON LISTA (CAPÍTULO 4)
#++++++++++++++++++++

#Recorrido de listas
for marcas in deportivos:
    print(marcas)

#Listas numéricas range(start, (stop-1), step)
#si se omite step por defecto será 1.
for value in range(1, 5):
    print(value, end=" ")
print("\n")

for value in range(0, 10, 3):
    print(value)

#crear lista con range
lista = list(range(1,8))
print(lista)

lista_impar = list(range(1, 8, 2))
print(lista_impar)

cuadrados = []
for numero in range(1,11):
    cuadrados.append(numero ** 2)

print(cuadrados)

#estadísticas con lista de número
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))

#lista comprimida, método en una sola línea
otros_cuadrados = [value**2 for value in range(1,11)]
print(otros_cuadrados)


#partir (slicing) lista[inicio:(fin-1)]
jugadores = ['elizabeth','gonzalo', 'martina', 'gabriel','norela','andrés']
print(jugadores)
print(jugadores[1:5])
#por defecto inicia en 1
print(jugadores[:5])
#también por defecto termina en el último
print(jugadores[2:])
#para imprimir los últimos 3 también puedo usar
print(jugadores[-4:])

#recorriendo bucle a través de un slice
print("\nEstos son los primeros tres jugadores")
for jugador in jugadores[:3]:
    print(jugador.title())

#copiando listas
copia_jugadores = jugadores[:]
jugadores.append('Vicente')
copia_jugadores.append('Carla')

print(jugadores)
print(copia_jugadores)

#referenciando listas
copia2_jugadores = jugadores
jugadores.append('Romina')
print(jugadores)
print(copia2_jugadores)
#   tanto copia2_jugadores como jugadores
#   son dos nombres con una misma lista 
#   como referencia.

#
#  TUPLAS (SON INMUTABLES)
#
dimensiones = (200, 100)
print(dimensiones[0])
print(dimensiones[1])

#error
#dimensiones[0] = 280
#'tuple' object does not support item assigment

#recorrido
for dimension in dimensiones:
    print(dimension)

#reasignación de valores a la variable

dimensiones = (280,100)
print(dimensiones)