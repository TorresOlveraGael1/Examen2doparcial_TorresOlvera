# Punto 4

#En este programa realizaremos un codigo que meta la informacion de un usuario

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Solicitar información al usuario

nombre = str(input("Introduce tu nombre: "))

edad = str(input("Introduce tu edad: "))

telefono = str(input("Introduce tu numero telefonico: "))

direccion = str(input("Introduce tu direccion: "))

#Crear un diccionario para almacenar la información del usuario

usuario = {

'name' : nombre,

'age' : edad,

'phone-number' :telefono,

'adress' : direccion
}

#Mostrar la información en el formato deseado

print (" ")

print(f"El nombre del usuario es: {usuario['name']}")

print (" ")

print (f"El usuario tiene: {usuario['age']}")

print (" ")

print (f"su número de teléfono es: {usuario['phone-number']}")

print (" ")

print (f"la direccion del usuario es: {usuario['adress']}")

print (" ")