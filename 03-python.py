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
#insercción al fianl de la lista
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
ejemplo3[0]="cambio"

#Borrar elementos 



#Tuplas
#Set
#Diccionarios
