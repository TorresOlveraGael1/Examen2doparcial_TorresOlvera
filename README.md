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
materias = {
    'Matematicas' : Matematicas,
    
    'Fisica' : Fisica,
    
    'Quimica' : Quimica,
    
    'Historia' : Historia,
    
    'Lengua' : Lengua
}

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

![image](https://github.com/user-attachments/assets/f15715fb-d0ae-4bf3-9fb5-5b68d62ea59f)
![image](https://github.com/user-attachments/assets/f06216e4-9c35-452a-ab7b-90a4aee97ac7)
