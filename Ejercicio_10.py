from csv import Dialect


ListaDias   = []
ListaLluvia = []
Dia         = ''
Lluvia      = 0.0
TotalLluvia = 0.0
#Cargar lista con los 7 días de la semana y su lluvia correspondiente
for i in range(0,7,1):
    Dia     = input("Ingresar día de la semana: ")
    ListaDias.append(Dia)
    Lluvia  = float(input("Ingresar lluvia del día: "))
    ListaLluvia.append(Lluvia)
    TotalLluvia += Lluvia
print(f"Total de lluvia caída durante la semana: {TotalLluvia}")
Lluvia = max(ListaLluvia)
print(f"Día de mayor lluvia: {ListaDias[ListaLluvia.index(Lluvia)]}")
