from datetime import date, time, datetime, timedelta
#from dateutil.relativedelta import relativedelta

ListaNombres    = []
ListaNacimientos= []
Nombre          = ''
FechaNacimiento = (0,0,0)
Continuar       = 'S'
#Carga lista con Nombres y Fechas de Nacimiento
while Continuar:
    Nombre          = input("Ingresar Nombre de la persona: ")
    ListaNombres.append(Nombre)
    FechaNacimiento = datetime.strptime(input("Ingresar Nacimiento (dd/mm/aaaa):"), "%d/%m/%Y")
    ListaNacimientos.append(FechaNacimiento)
    Continuar   = input("Desea continuar ingresando datos? ('S'/''):")
#print(f"Fechas almacenadas: {ListaNacimientos}")

#Recorrer y mostrar los Nombres de los mayores de edad
for i in range(0, len(ListaNombres),1):
    Edad = datetime.now() - ListaNacimientos[i]
    if Edad.days >= (18 * 365.25):
        print(f"Nombre de mayor de edad: {ListaNombres[i]}")
