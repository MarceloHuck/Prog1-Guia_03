from os import supports_bytes_environ


ListaNumeros = []
NumeroEntero = 1

#Cargar lista con Números Enteros
while NumeroEntero:
    NumeroEntero = int(input("Ingresar número entero (0 para terminar): "))
    if NumeroEntero:
        ListaNumeros.append(NumeroEntero)

#Invertir el orden en la lista
PosicionIntercambio = 0
Intercambiar        = 0    
for i in range(0,len(ListaNumeros)-1,1):
    ListaNumeros.insert(i, ListaNumeros[len(ListaNumeros)-1])
    ListaNumeros.pop(len(ListaNumeros)-1)
print(f"Lista invertida: {ListaNumeros}")