ListaNumeros = []
NumeroEntero = 1

#Cargar lista con Números Enteros
while NumeroEntero:
    NumeroEntero = int(input("Ingresar número entero (0 para terminar): "))
    if NumeroEntero > 0 and NumeroEntero < 31 and (NumeroEntero % 2) == 0:
        ListaNumeros.append(NumeroEntero)
        print(f"Número almacenado: {NumeroEntero}")


