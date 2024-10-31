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

print ("Estas son tus calificaciones: ", materias)

#Establecemos segunda cadena If en caso de una materia reprobada

if Matematicas < 6:

    print("Debes repetir el curso de mate")

if Fisica < 6:

    print("Debes repetir el curso de fisica")

if Quimica < 6:

    print("Debes repetir el curso de quimica")

if  Historia < 6:

    print("Debes repetir el curso de historia")

if  Lengua < 6:

    print("Debes repetir el curso de lengua")
