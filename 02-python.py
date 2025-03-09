#FUNCIONES
  #porciones de código cuya finalidad es evitar la repetitividqad de código 
#sintaxis 
#def nombre_funcion (parametros de entrada opcionales):
 #bloque de código a ejecutar


#FUNCIONES INTEGRADAS MAS COMUNES 
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






  
