#FUNCIONES
  #porciones de código cuya finalidad es evitar la repetitividqad de código 
#sintaxis 
#def nombre_funcion (parametros de entrada opcionales):
 #bloque de código a ejecutar


#FUNCIONES INTEGRADAS MAS COMUNES 

#hex(x) recibe numero decimal y devuelve en hexadeximal con el prefijo 0x
print(hex(255))
print(hex(-42))
#filtrado de esta funcion (quitar prefijo y pasar a mayusculas)
print(f"{255:#x}",f"{255:x}",f"{255:X}")

#dirección de memoria
z=2
print(id(z))

print("Imprime un mensaje en consola"))
lista=[2,4,5,6,8]
print(len(lista))
#conversion de objetos 
print(str(234))
print(int("123"))
print(float("2.5"))

print(type(3.14)) #tipo de un objeto

entrada=input("dato: ") #lee entrada desde consola 

print(abs(-2)) #devuelve el valor absoluto de un número
print(round(1.789,2)) # decimales especificos

#funciones de iteración
for i in range (5): #genera secuencia de números 
  print(i)

lista=["a","b","c"]
for indice, valor in enumerate (lista): #añade un contador a un iterable 
  print (indice, valor)

#ordenamiento y filtrado 
lista=[1,3,4,2]
print(sorted(lista)) #ordena los elementos 

def es_par(num):
  return num %2==0
numeros=[1,2,3,4,5]
pares=filter(es_par, numeros) #implementa de filtro otra función
print(list(pares))

#FUNCIONES CREADAS POR EL USUARIO
  #return para devolver un valoro varios (separados por coma) 
  # valor predeterminado--> a devolver "None", especificar en parametros de funcion
  #función sin parametros o retorno de valores
  #parametros a recibir= parametros colocados en la definición de la función


def fun_01():
  print("función sin parametros")

fun_01()
  #Función con un parametro
def fun_02(valor):
  print("Parametro recibido: " + valor)

fun_02("hii")

  #función con multiples parámetros con una sentencia de retorno
def potencia(val1,val2):
  return val1** val2

potencia(2,3)

#valores predeterminados
def suma(a, b=3): #si no se ingresa le valor se toma el predeterminado
  return a + b

print(suma(2,5))
print(suma(2))

#manipulación como objetos
  #asignar la función a una variable y emplear dicha variable como la función
s= suma 
print(s(1,2)) 

#variables locales
  #definidas dentro de la funcion 

def doble(valor):
  x=valor*2
  return x
  
print(x) #x sin definir debido a que es local
print(doble(3))

#funciones con cantidad variable de parametros
def promedio (*numeros): #tupla cuya longitud depende de los argumentos ingresados
  suma=0
  k=0
  for n in numeros:
    suma += n
    k += 1
  return suma/k
print(promedio(10,7,8,9))
print(promedio(8,9))

#funciones y orden de los argumentos

def cuenta(frase, letra):
  k=0
  for car in frase:
    if car == letra:
      k+=1
  return k
    #proporcionando parametros en funcion de su nombre
print(cuenta("buen día grupo", "u"))
print(cuenta(frase="les tengo noticias", letra="e"))
print(cuenta(letra="i", frase= "colibri"))

#FUNCIONES ANIDADAS
  #Crear la función externa.
  #Definir la función interna dentro de la función externa.
  #Llamar a la función interna dentro de la función externa o devolverla.
    #crear funciones dentro de otras
    #mejoran legibilidad y la modularizacion del código 
def principal(x): #x=3
  def secundaria(y): # funcion interna
    return x+y  #usa 'x' de la funcion externa 
  return secundaria #devuelve la funcion secundaria (no su resultado)
  
funcion= principal (3) #devuelve "secundaria", con 'x' almacenado 
#asignarla a una variable para poder emplearla despues
print(principal(2)) #Ejecuta 'secundaria(2)', donde x=3 y y=2--> 3+2 =5


#EXTRA
def convertir (texto1: str, texto2: str)-->int:
  
  





  
