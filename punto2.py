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
