ListaNombres = []
Nombre = '1'
while Nombre:
    Nombre = input("Ingresar Nombre(vacío: '', termina): ")
    if Nombre:
        ListaNombres.append(Nombre)
Nombre   = '1'
posicion = 0
while Nombre:
    Nombre = input("Ingresar Nombre a buscar (vacío: '', termina): ")
    if Nombre:
        for i in range(0,len(ListaNombres),1):
            if ListaNombres[i] == Nombre:
                posicion = i
                print(f"Nombre {Nombre} encontrado en la posición {posicion}")