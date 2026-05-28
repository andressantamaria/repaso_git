print("Hola soy Gabriel García bla...")

#pero veamos que puedo hacer:

k = 8.0
i = int(k)

print(k, i)

for i in range(1,6):
    j = i
    while j > 0:
        print("*", end=" ")
        j -= 1
    print("")
        
for i in range(6,0,-1):
    j = 0
    while j < i:
        print("*", end=" ")
        j += 1
    print("")

#mi primero arreglo

cato = [1,2,3, "cato"]

print("el gato", cato[3])