ListaNombres = []
ListaSexos   = []
Nombre = ''
Sexo   = ''
#Cargar las lista de Nombres y Sexos
Continuar       = 'S'
while Continuar:
    Nombre  = input("Ingresar Nombre: ")
    ListaNombres.append(Nombre)
    Sexo    = input("Ingresar Sexo [H/M]: ")
    ListaSexos.append(Sexo)
    Continuar   = input("Desea continuar ingresando datos? ('S'/''):")

#Contar las 'M'ujeres
Contador = 0
for i in range(0,len(ListaSexos),1):
    if ListaSexos[i]  == 'M':
        Contador += 1

print(f"Cantidad de Mujeres cargadas: {Contador}")

#Mostrar las Mujeres cargadas
for i in range(0,len(ListaNombres),1):
    if ListaSexos[i] == 'M':
        print(f"{ListaNombres[i]}")