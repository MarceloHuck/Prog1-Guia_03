ListaNumeros = []
NumeroEntero = 0
for i in range(0,10,1):
    NumeroEntero = int(input("Ingresar número entero: "))
    ListaNumeros.append(NumeroEntero)
contador = 0
for i in range(0,10,1):
    if ListaNumeros[i] > 23:
        contador += 1
        print(f"Número almacenado: {ListaNumeros[i]} - Contador: {contador}")
i = 0
largo = len(ListaNumeros)
#print(largo)
while i < largo:
    if ListaNumeros[i] <= 23:
#        print(ListaNumeros[i])
        ListaNumeros.pop(i)
        largo -= 1
#        print(i)
#        print(largo)
    else:
        i += 1
#        print(i)
#        print(largo)
print(ListaNumeros)