#Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta, 
#un número de kilos mostrar el precio de ese número de kilos de fruta.
print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172")
print(" ")

# Matriz de frutas con precios por kilo
frutas_matriz = [
    ['Uvas', 10],
    ['Mango', 12],
    ['Durazno', 16],
    ['Sandia', 22],
    ['Manzana', 8],
    ['Piña', 14]
]

# Convertimos la matriz en un diccionario
D = {fruta[0]: fruta[1] for fruta in frutas_matriz}

# Mostrar el diccionario para verificar
print("Precios por kilo de las frutas disponibles:")
print(D)
print(" ")

# Preguntar al usuario por la fruta y la cantidad de kilos
S = str(input('Ingrese la fruta que desea comprar:')).title()

a = float(input("Cuántos kilos desea llevar:"))

# Verificar si la fruta está en el diccionario
if S in D:
    # Calcular el precio total multiplicando el precio de la fruta por los kilos
    b = a * D[S]
    print(f"El precio total es: {b} MXN")
else:
    print("Esta fruta no está disponible")
