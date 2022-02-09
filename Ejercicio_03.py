ListaNombres = []
ListaSexos   = []
Nombre = ''
Sexo   = ''
#Cargar las lista de Nombres y Sexos: 8 elementos
for i in range(0,8,1):
    Nombre  = input("Ingresar Nombre: ")
    ListaNombres.append(Nombre)
    Sexo    = input("Ingresar Sexo [H/M]: ")
    ListaSexos.append(Sexo)

ListaMujeres = []
#Cargar la lista de Mujeres
for i in range(0,8,1):
    if ListaSexos[i] == "M" or ListaSexos[i] == "m":
        ListaMujeres.append(ListaNombres[i])
#        print(f"{ListaNombres[i]}")

#Mostrar las Mujeres cargadas
for i in range(0,len(ListaMujeres),1):
    print(f"Mujer {i+1}: {ListaMujeres[i]}")