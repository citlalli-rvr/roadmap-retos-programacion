#operadores aritméticos
#operaciones matematicas en variables y valores

print(f"suma { 2 + 5}")
print(f"resta {5 - 2}")
print(f"multiplicacion {3 * 9 }")
print(f"division {9/3}")
#modulo- devulve el residuo de la division
print(f"modulo {4 % 4}")
print(f"potencia {3 ** 2}")

#operadores de asignación
#asignar valores a variables
simple= "asignación simple con ="

#combinacion de asignacion y operación (compuesta)
num1=5
print(num1)
num1 +=3 #suma al valor
print(num1)
num2=10
num2 -=5 #resta al valor
print(num2)
num3=5
num3 *=2 #multiplicación al valor
print(num3)
num4=7
num4 /=2 #división al valor
print(num4)
num5= 15
num5 %=4 #modulo al valor
print(num5)
num6=7
num6 //=2 #división entera
print(num6)

#operadores de comparación
print( num1 == num2) #compara si son valores iguales (arroja True o False)
print(num3 != num4) #compara si sin valores desiguales 
print(num1 < num2) #menor que
print(num3 > num4) #mayor que
print(num5 >= num6) #mayor o igual que
print(num1 <= num2) #menor o igual que

#operadores lógicos
print(num1> 0 and num2< 20) #True si ambas son verdaderas de lo contrario False
print(num3> 10 or num4<20) #True si al menos una condición es verdadera
condicion= False
print(not condicion) #invierte el valor

#operadores a nivel de bits
#el operador es aplicado bit x bit (considerandose en binario)
print(num1|num2) #or bit a bit
print(num3^num4) #or exclusivo bit a bit
print(num5 & num6) #and bit a bit
print(num2 << 3) #desplaza num2 a 3 bits a la izquierda
print(num2 >> 3) #Desplaza num3 a 3 bits a la derecha
print(~num2) #obtienes los bits de num2 invertidos


#operadores de pertenencia
#se emplea para identificar pertenencia en alguna secuencia (listas,strings,tuplas)
a=[1,2,3,4,5]

print 3 in a # in devuelve True si el valor se encuentra en la secuencia, False si es lo contrario
print 12 not in a #True si el valor no se encuentra en la secuencia, False al contrario

str= "Hola mundo"
print "Hola" in str

#operadores de identidad
# comprobar si dos variables emplean la misma ubicación en memoria
a= 3
b= 3
c= 4

print a is b #muestra true
print a is not b #muestra false
print a is not c #muestra True


#Estructuras de control
  #permiten modificar le flujo de la ejecución de un conjunto de instrucciones
    #control secuencia
    #control de selección
    #control de repetición

#ESTRUCTURAS DE SELECCIÓN

#sentencia if
#permite ejecutar un bloque de código si cumple una condición
a= 3
b=3
c= 4
d=4

if a is b:
  print("Las variablesa y b emplean la misma ubicación")
elif a is not c:
  print ("Las variables a y c no emplean la misma ubicación")
else:
  (" las variables a y b no emplean la misma ubicación de memoria")

#ESTRUCTURAS DE REPETICIÓN

#ciclo for
#se conoce el número de iteraciones a realizar 
#for VAR  in SECUENCIA--> variable del ciclo/control y secuencia de valores a iterar
letras=[1,2,3,4,5]
for l in letras:
  l +=3
  print (l)

#ciclos anidados
  #ciclo for dentro de otro

informacion=[[1,3],[7,9,8].[3,1,6]]
for fila in informacion:
  for num in fila:
    num /=2
    print(num)
#desempaquetar valores
num= [(1,2),(3,4),(5,6),(7,8)]

for x,y in num:
  print (f"impar {x} par= {y}")

for x, y in num:
  print (x>y or y>x)
  print (y<x and y>x)


#ciclo while
 #ejecuta un bloque de instrucciones mientras haya una condición que se cumpla
  #while condicion:
x=1
y=1
print("prueba con operadores logicos") 
while x> 0 and y < 6:
  print(f"{x}:{y}")
  x+=1
  y+=2

#sentencia try-except 
#manejo de excepciones especificas
#Sintaxis
#try
  #código que puede generar una excepción
  #si ocurre una excepción aquí, el control se transfiere al bloque except
#except ExcepcionX:
  #Código que maneja la excepción de tipo ExcepcionX

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

try:
    c = a / b 
except ZeroDivisionError:
    print("Estás intentando dividir por cero")
#TIPOS DE ERRORES
# SyntaxError--> error de sintaxis 
#IndetationError--> error de identación
#TypeError-->  tipo de dato incompatible 
#NameError--> implementación de variable no definida previamente 
#ValueError--> error en el valor de una argumento que recibe una función
#IndexError--> indice fuera de rango

# EXTRA 
#Crea un programa que imprima por consola todos los números comprendidos
 #entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for x in range (1,56):
  if x %2 ==0 and x %3 !=0 and x !=16:
    print (x)



