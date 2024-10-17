#Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
#El usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.

print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172")
print(" ")

#Este es un diccionario
D = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

# Imprimimos el diccionario
print(D)
print(" ")

# Pedimos al usuario que ingrese su divisa
S = str(input('Ingrese su divisa:'))
S = S.title()

# Ponemos condiciones para desplegar el simbolo correcto
if S in D:
    print("Su simbolo es:", D[S])
else:
    print("Esta divisa no esta disponible")


