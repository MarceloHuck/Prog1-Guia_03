ListaLetras = []
Letra = '1'
while Letra:
    Letra = input("Ingresar letra (vacío: '', termina): ")
    if Letra:
        ListaLetras.append(Letra)
contador = 0
for i in range(0,len(ListaLetras),1):
    if ListaLetras[i] == 'a' or ListaLetras[i] == 'e' or ListaLetras[i] == 'i' or ListaLetras[i] == 'o' or ListaLetras[i] == 'u':
        contador += 1
print(f"Cantidad de vocales: {contador}")

