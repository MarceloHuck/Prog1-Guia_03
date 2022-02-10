ListaNombres = []
ListaSueldos = []
Nombre = ''
Sueldo = 0.0
#Cargar las lista de Nombres y Sueldos: n elementos
Continuar = 'S'
while Continuar:
    Nombre  = input("Ingresar Nombre: ")
    ListaNombres.append(Nombre)
    Sueldo  = float(input("Ingresar Sueldo: "))
    ListaSueldos.append(Sueldo)
    Continuar = input("Desea continuar cargando elementos? ('S'/' '): ")
#Mostrar las Personas que ganan más de $ 85000
for i in range(0,len(ListaNombres),1):
    if ListaSueldos[i] > 85000:
        print(f"Persona que gana más de $ 85000: {ListaNombres[i]}")