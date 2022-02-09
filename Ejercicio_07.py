ListaNumeros = []
NumeroEntero = 0
Sumatoria    = 0
Promedio     = 0.0
#Cargar 7 números enteros
for i in range(0,7,1):
    NumeroEntero = int(input("Ingresar número entero: "))
    ListaNumeros.append(NumeroEntero)
    Sumatoria += NumeroEntero
#Calcular el Promedio
Promedio = Sumatoria / 7
print(f"Promedio: {Promedio}")
#Recorrer el vector y mostrar los mayores al Promedio
for i in range(0,7,1):
    if ListaNumeros[i] > int(Promedio):
        print(f"Número almacenado mayor que el Promedio: {ListaNumeros[i]}")
