"""
Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje 
<nombre> 
tiene <edad> años, 
vive en <dirección> 
y su número de teléfono es <teléfono>
"""
print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172")
print(" ")

# Le pedimos su informacion al usuario
n = str(input('Cual es su nombre? '))
print(" ")
e = int(input('Cual es su edad? '))
print(" ")
d = str(input('Cual es su direccion? '))
print(" ")
t = str(input('Cual es su telefono? '))

# Los guardamos en un diccionario
info = {
  "Nombre": n,
  "Edad": e,
  "Direccion": d,
  "Telefono": t
}
print(" ")

# Imprimimos el diccionario
print(info)
print(" ")

# Mostramos en pantalla toda su informacion
print(n)
print(f'Tiene {e} años,')
print(f'Vive en {d},')
print(f'Y su numero de telefoo es {t}')