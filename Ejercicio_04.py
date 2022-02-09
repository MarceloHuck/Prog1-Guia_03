ListaNumeros = []
ListaCuadrados = []
NumeroEntero = 1

#Cargar lista con Números Enteros
while NumeroEntero:
    NumeroEntero = int(input("Ingresar número entero (0 para terminar): "))
    if NumeroEntero:
        ListaNumeros.append(NumeroEntero)

#Cargar lista con los Cuadrados de los números cargados en la lista anterior    
for i in range(0,len(ListaNumeros),1):
    ListaCuadrados.append(pow(ListaNumeros[i], 2))
 
#Mostrar lista con los Cuadrados
for i in range(0,len(ListaCuadrados),1):
    print(f"Número almacenado: {ListaNumeros[i]} - Cuadrado: {ListaCuadrados[i]}")
