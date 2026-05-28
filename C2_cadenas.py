#vamos a ver qué dice el libro sobre cadenas
cadena0 = "!!!!"
cadena1 = "Los pollitos dicen pío"

#metodos
cadena2 = cadena1.title() #Los Pollitos Dicen Pío
cadena3 = cadena1.upper() #LOS POLLITOS DICEN PÍO
cadena4 = cadena1.lower() #"Los pollitos dicen pío"

print("upper:", cadena1.upper())

#insertando valores de variable en cadenas, con f
cadena5 = f"{cadena1}{cadena0}" #SE CONOCE COMO f-string
cadena6 = f"{cadena1}   {cadena0}"

print(cadena5.title())
print(cadena6.title())

#componiendo mensajes con f-string
#usando la información asociada a la variable

print(f"¡¡¡{cadena5.title()}")

cadena7 = f"¡¡¡{cadena5.title()}"   #¡¡¡Los Pollitos Dicen Pío!!!!

#formateando el texto

print("\tHola qué es que te pasa?!")    #tabulación
print("Hola,  \n¿1qué es que te pasa?!")    #salto de línea
print("Hola,  \n\t¿qué es que te pasa?!")    #combinación



#Eliminando el espacio en blanco al inicio lstrip()
#  o final rstrip(), o a ambos extremos strip()

cadena8 = "Los Pollitos Dicen "
#solo para mostrar.
print(cadena8.rstrip(), end="")
print(cadena8)
#permanentemente
cadena8 = " Los Pollitos Dicen "
cadena9 = cadena8.rstrip()
print(cadena9)
cadena9 = cadena8.lstrip()
print(cadena9)
print(cadena8.strip())

#uso de comillas simples y dobles
print("fueron los 2d's quienes se rieron")
print('fueron los 2ds los que se rieron')

#pero esto marcaría error:

#   print('fueron los 2d's los que se rieron')

#unterminated string literal , porque el apóstrofe despues de 2d cierra
#toda la expresión de imprimir cadena.