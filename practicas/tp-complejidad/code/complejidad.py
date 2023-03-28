from algo1 import *
from mylinkedlist import *
from random import randint
#Giraudo Ignacio 13855

# Ejercicio 4:

'''Tomamos el valor del medio, vemos los lugares que tiene antes que él, la mitad de esta cantidad tienen que tener valores menores que el valor del medio.
La cantidad de números que tengamos antes de nuestro middle_value va a ser igual al número de su posición.
Guardamos las posiciones de los elementos que tienen un valor mayor a middle_value y se encuentran posicionados antes que él.
Luego si no tenemos los valores menores necesarios, realizamos un intercambio de un valor menor que esté posicionado a la derecha con uno guardado en la lista antes mencionada'''


def middle_value_sort(array):
	middle_index = int(len(array)/2)
	print("middle value:", array[middle_index])
	minor_values = 0
	major_values_positions = LinkedList()
	minor_values_positions = LinkedList()

	for i in range(0, middle_index):
		if(array[i] < array[middle_index]):
			minor_values += 1
			add(minor_values_positions, i)
		elif(array[i] > array[middle_index]):
			add(major_values_positions, i)

	# están los valores menores necesarios a la izquierda
	if(minor_values == int(middle_index/2)): 
		return array

	# faltan valores menores a la izquierda
	if(minor_values < int(middle_index/2)): 
		for i in range(middle_index+1, len(array)):
			if(array[i] < array[middle_index]):
				if(major_values_positions.head == None):
					return array
				
				swapPositions(array, i, major_values_positions.head.value)
				deletePosition(major_values_positions, 0)
				minor_values += 1
			if(i == len(array)-1):
				return array

		if(minor_values == int(middle_index/2)):
			return array

	# hay valores menores de más a la izquierda
	if(minor_values > int(middle_index/2)): 
		for i in range(middle_index+1, len(array)):
			if(array[i] >= array[middle_index]):
				swapPositions(array, i, minor_values_positions.head.value)
				deletePosition(minor_values_positions, 0)
				minor_values -= 1
			if(minor_values == int(middle_index/2)):
				return array
			if(i == len(array)-1):
				return array
			

def swapPositions(array, pos1, pos2):
	temp = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = temp
	#array[pos1], array[pos2] = array[pos2], array[pos1]
	return array

newArray = Array(9, 0)
for i in range(0, len(newArray)):
	newArray[i] = randint(0, 10)

print(newArray)
print(middle_value_sort(newArray))


# Ejercicio 5: 

'''Podemos formar una nueva lista sin los números repetidos en la lista y sin los números que son mayores o iguales a n, ya que no van a poder formar sumas = n
Con mergesort y binary search se puede bajar la complejidad a O(nlogn)'''
# O(n²)
def contiene_suma(array,n):
	for i in range(0, len(array)):
		for j in range(i+1, len(array)):
			if(i != j):
				if(array[i]+array[j] == n):
					return True
	return False

print(contiene_suma(newArray, 10))

#Ejercicio 5 

def ContieneSuma(A, n):
  current = A.head
  aux = A.head
  if aux.value+current.nextNode.value==n:
    return true
  else:
    while current != None and aux != None: #o(n) peor caso-#O(C)
      if current.nextnode != None:
        if aux.value + current.nextnode.value == n:
          return True
        current = current.nextNode
      else:
        aux = aux.nextNode
        current = aux
    return
