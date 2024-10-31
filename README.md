# Examen2doparcial_TorresOlvera

Torres Olvera Gael

Examen del segundo parcial de frameworks

# Punto 1

#Escribir un programa que almacene las asignaturas de un curso

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Establecemos que el testeador introduzca sus calificiaciones

Matematicas = float(input("Que nota has sacado en Matematicas? "))

Fisica = float(input("Que nota has sacado en Fisica? "))

Quimica = float(input("Que nota has sacado en Quimica? "))

Historia = float(input("Que nota has sacado en Historia? "))

Lengua = float(input("Que nota has sacado en Lengua? "))

#Establecemos las matyerias en una lista

materias = [Matematicas, Fisica, Quimica, Historia, Lengua]

#Iprimimos las materias

print ("Estas  son tus calificaciones: ", materias)

#Establecemos cadena If en caso de una materia reprobada
if Matematicas < 6:
    
    print("Debes repetir el curso de mate")
    
elif Fisica < 6:
    
    print("Debes repetir el curso de fisica")
    
elif Quimica < 6:
    
    print("Debes repetir el curso de quimica")
    
elif  Historia < 6:
    
    print("Debes repetir el curso de historia")
    
elif  Lengua < 6:
    
    print("Debes repetir el curso de lengua")

![image](https://github.com/user-attachments/assets/e853e722-c84c-4896-81ac-8625e3e187ca)
![image](https://github.com/user-attachments/assets/db448b35-7d29-4711-8046-9ff2546ac036)

# Punto 2

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Establecemos que el testeador introduzca sus creditos

CreditosMate = float(input("De cuanto es tu credito en matematicas? "))

CreditosFi = float(input("De cuanto es tu credito en fisica? "))

CreditosQui = float(input("De cuanto es tu credito en quimica? "))

CreditosHis = float(input("De cuanto es tu credito en historia? "))

CreditosLen = float(input("De cuanto es tu credito en lengua? "))

#Establecemos las materias en un diccionario

materias = {
    
    'Matematicas' : CreditosMate,
    
    'Fisica' : CreditosFi,
    
    'Quimica' : CreditosQui,
    
    'Historia' : CreditosHis,
    
    'Lengua' : CreditosLen
}

#Imprimimos la cantidad de creditos de cada clase

print("El total de creditos en tu clase de Matematicas es: ", materias['Matematicas'])

print("El total de creditos en tu clase de Matematicas es: ", materias['Fisica'])

print("El total de creditos en tu clase de Matematicas es: ", materias['Quimica'])

print("El total de creditos en tu clase de Matematicas es: ", materias['Historia'])

print("El total de creditos en tu clase de Matematicas es: ", materias['Lengua'])

#Hacemos la suma del total de creditos nde todas las materias

suma = CreditosMate +  CreditosFi + CreditosQui + CreditosHis + CreditosLen

#Imprimos el total de creditos

print("El total de creditos en todas las materias es: ", suma) 

![image](https://github.com/user-attachments/assets/c3c40ded-3e91-4106-ace4-ed091c356d5f)
![image](https://github.com/user-attachments/assets/d914d134-f6f7-4cb7-b3e1-fc61b5a5dfeb)

# Punto 3

#Escribir un programa que almacene las asignaturas de un curso

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Establecemos que el testeador introduzca sus calificiaciones

Matematicas = float(input("Que nota has sacado en Matematicas? "))

Fisica = float(input("Que nota has sacado en Fisica? "))

Quimica = float(input("Que nota has sacado en Quimica? "))

Historia = float(input("Que nota has sacado en Historia? "))

Lengua = float(input("Que nota has sacado en Lengua? "))

#Establecemos las materias en un diccionario

#Establecemos las matyerias en una lista
materias = [Matematicas, Fisica, Quimica, Historia, Lengua]

#Imprimimos las materias

print ("Esta es tu calificacion en Mate: ", materias[0])

print ("Esta es tu calificacion en Mate: ", materias[1])

print ("Esta es tu calificacion en Mate: ", materias[2])

print ("Esta es tu calificacion en Mate: ", materias[3])

print ("Esta es tu calificacion en Mate: ", materias[4])

![image](https://github.com/user-attachments/assets/5780896b-126d-4834-8d3b-485529710d39)
![image](https://github.com/user-attachments/assets/fea58262-d0fd-4e1c-8c45-e95e164d210f)

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

![image](https://github.com/user-attachments/assets/e48a3926-69c2-44b9-a6ef-8f1db378ae0e)
![image](https://github.com/user-attachments/assets/479885e0-4e09-4af9-995b-f863efe5d8d4)
