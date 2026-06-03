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
#TRABAJANDO CON LISTA (CAP4)
#++++++++++++++++++++

