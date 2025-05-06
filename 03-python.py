#ESTRUCTURAS DE DATOS
#estructuras soportadas por defecto 
#operaciones de inserción, borrado, actualización y ordenación

#consultar: https://docs.python.org/es/3/tutorial/datastructures.html
#https://aprendepython.es/core/datastructures/lists/

#Listas
#compuesta por cero o más elementos
#elementos separados por comas y dentro de corchetes 
#operaciones de inserción, borrado, actualización y ordenación
lista_vacia=[]
#insercción al final de la lista
lista_vacia.append("Ingresando")
lista_vacia.append("Medio")
lista_vacia.append("Final")

#insercción involucrando indices
lista_vacia.insert(1,"indice") #se añadiría antes de el que esta actualmente en esa posición

#repetición de los elementos con *
#concatenación de listas con +
ejemplo2=["uno","dos","tres"]
ejemplo2*2
print(ejemplo2)
print(ejemplo2*2)

#adición de listas con extend (itera sobre cada elemento del objeto)
ejemplo1=["text1","text2","text3"]
ejemplo2.extend(ejemplo1)

#modificación mediante indice
ejemplo3=["element1","element2","element3"]
print(ejemplo3)
ejemplo3[0]="cambio"
print(ejemplo3)

#Borrar elementos 
#borrar con "del" e indice
ejemplo4=["Sol","Tierra","Agua","Aire"]
print(ejemplo4)
del ejemplo4[1]
print(ejemplo4)

#borrar con "remove()" y el valor
#en caso de valores duplicados se eleminará el primero
ejemplo5=["Epura","Bonafont","Ciel","Peñafiel"]
print(ejemplo5)
ejemplo5.remove("Bonafont")
print(ejemplo5)

#con "pop" y el indice podremos visualizar que estamos eliminando
ejemplo6=["Huevos","Leche","Queso"]
print(ejemplo6)
extraemos= ejemplo6.pop(1)
print(extraemos)
print(ejemplo6)

#Borrado completo de lista con nombre.clear()
#ordenar
#ambos métodos admiten un arametro booleano para indicar si lo queremos ne sentido inverso

#funcion sorted() que devuelve una lista nueva ordenada
ejemplo7=["Aceite","Frijol","Arroz","Atun"]
sorted(ejemplo7)
print(ejemplo7)

sorted(ejemplo7,reverse=True)
#funcion sort() que modifica la lista original
ejemplo8=["Aceite","Frijol","Arroz","Atun"]
print(ejemplo8)
ejemplo8.sort()
print(ejemplo8)


#Tuplas
#Conformada por un número de valores separados por comas
#representadas con parentesis
#son inmutables y suelen contener una secuencia heterogénea de elementos

#creacion de una tupla con un elemento 
tupla1=("elemento",) #Agregar una coma al final
#conversión de lista a tupla (aplicable en tipos de datos iterables)
tuple(ejemplo8)

#Set/conjuntos
conjunto1=set()
#conversión de otros tipos (diccionarios a set, se extraen los valores únicos)
set({'manzana': 'rojo', 'plátano': 'amarillo', 'kiwi': 'verde'})
#no podemos acceder a un elemento en concreto o modificarlo
#podemos añadir o borrar elemntos
nombres=set(["Juan","Pedro","José", "Martín"])
nombres.add("Margaret")
#borrar elemento por su valor
nombres.remove("Juan")
#podemos iterar sobre el conjunto
#ordenar
sorted(nombre)


#Diccionarios
#mantienen elorden en que se insertan las claves
#son mutables
#claves únicas
#usa llaves
nombres_edad={ "juan":15, "José":16,"Pedro":20}
#añadir o modificar un elemento
nombres_edad["Margaret"]=25
#modificar
nombres_edad["José"]=18

#Borrar
#sentencia del 
del nombres_edad["juan"]
nombres_edad.pop("José")
