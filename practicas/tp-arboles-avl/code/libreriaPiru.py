from algo1 import Array
from random import randint
from linkedlist import *
#funcion para imprimir matriz
def print_matriz(matriz):  
  for i in matriz:
   print(i, end="  ")
   print()
fila=randint(0, 5)
columna=randint(0, 5)
matriz=Array(fila,Array(columna,0))
#funcion para llenar matriz
def creando_matriz(matriz,fila,columna):
  for x in range (0,fila):
   for n in range (0,columna):
     matriz[x][n]=randint(0, 5)
#funcion para llenar matriz con elementos nulos
def creando_matriz_nula(matriz,fila,columna):
  for x in range (0,fila):
   for n in range (0,columna):
     matriz[x][n]=0
#funcion para llenar vector
def llenar_vector(vector,dimension):
  for i in range(0,dimension):
    vector[i]=randint(0,10)
#funcion que busca el mayor elemento de una matriz
def mayor_elemento(vector,dimension, mayor):
  for i in range(0, dimension):
    if vector[i]>mayor:
      mayor=vector[i]
#funcion para sacar modulo de un vector
def modulo_vector(vector_suma,dimension):
  sum_cuad=0
  for x in range(0,dimension):
    sum_cuad=sum_cuad+pow(vector_suma[x],2)
  mod=sqrt(sum_cuad)
  print("el modulo de su vector es:",mod)

def MTriangS(fila,colum,matriz):
  MTS=0
  for i in range(0,fila):
    for j in range (0,colum):
      if i>j:
        if matriz[i][j]==0:
         MTS=MTS+1
        else:
         MTS=0
         break
  return MTS
    
def det_MTriang(fila,colum,matriz):
  determinante=1
  for i in range(0,fila):
      for j in range (0,colum):
       if i==j:
         determinante=determinante*matriz[i][j]
  return determinante

#funcion para imprimir lista
def print_list(L):
	current = L.head
	currentPos = 0

	while current != None:
		if currentPos != 0: print(end=" -> ")
		print(current.value, end="")
		current = current.nextNode
		currentPos = currentPos+1
	print()
	return currentPos
 
#funcion para revertir una lista
def revert(L):
	new = LinkedList()
	len = length(L)
	current = L.head

	for i in range(len):
		len -= 1
		add(new, current.value)
		current = current.nextNode
	return new
#funcion para imprimir lista empleados
def print_list_emp(L):
  current = L.head
  currentPos = 0

  while current != None:
	  if currentPos != 0: print(" | ")
	  print(current.value.nombre, end=", ")
	  print(current.value.edad, end=", ")
	  print(current.value.nroLegajo)
	  current = current.nextNode
	  currentPos += 1
  print()
  return currentPos
#search en empleados
def searchEmp(L,nroLegajo):
	current = L.head
	currentPos = 0

	while current != None:
		if current.value.nroLegajo == nroLegajo:
			return currentPos

		current = current.nextNode
		currentPos += 1
	return

#Utiles de practicos 
def previousNode(L, position):
	count = 0
	current = L.head
	while count < position-1:
			current = current.nextNode
			count += 1
	return current

def move(L, position_orig, position_dest):
	if position_orig == position_dest:return
	elif position_orig == 0:
		# La head es la posición de origen
		originalNode = L.head

		L.head = L.head.nextNode
		previousDest = previousNode(L, position_dest)

		originalNode.nextNode = previousDest.nextNode
		previousDest.nextNode = originalNode
	elif position_dest == 0:
		# La head es la posición de destino
		previousOrig = previousNode(L, position_orig)
		originalNode = previousOrig.nextNode

		if previousOrig.nextNode != None:
			previousOrig.nextNode = previousOrig.nextNode.nextNode
		else: previousOrig.nextNode = None

		originalNode.nextNode = L.head
		L.head = originalNode
	else:
		previousOrig = previousNode(L, position_orig)
		originalNode = previousOrig.nextNode

		if previousOrig.nextNode != None:
			previousOrig.nextNode = previousOrig.nextNode.nextNode
		else: previousOrig.nextNode = None

		previousDest = previousNode(L, position_dest)
		originalNode.nextNode = previousDest.nextNode
		previousDest.nextNode = originalNode      

def orderList(L):
	current = L.head
	count = 0

	while current.nextNode != None:
		if (current.value > current.nextNode.value):
			move(L, findNode(L, current.nextNode), count)
			return orderList(L)
		else:
			current = current.nextNode
			count += 1

def findNode(L, node):
	current = L.head
	count = 0

	while current != None:
		current = current.nextNode
		count += 1
		if current == node: return count    
  
#Posiblemente utiles vistas practicando:
def areEqualLists(list1, list2):
	current1 = list1.head
	current2 = list2.head
	equalValues = True

	while current1.nextNode != None and current2.nextNode != None:
		if current1.value != current2.value:
			equalValues = False
		
		current1 = current1.nextNode
		current2 = current2.nextNode
	
	return equalValues
  
def isPermutation(L, S):
	if areEqualLists(L,S): return False #si son iguales devuelve false xq ya no es permutacion
	currentL = L.head

	while currentL != None:
		if search(S, currentL.value) == None:
			return False
		currentL = currentL.nextNode
	return True

#practica calcular expresion:
def calculate_expression(L):
	while L.head.nextNode != None and L.head.nextNode.nextNode != None:
		result = calculate_operation(float(L.head.value), float(L.head.nextNode.nextNode.value), L.head.nextNode.value)
		# Se desvinculan los nodos con los que ya operamos
		L.head.nextNode = L.head.nextNode.nextNode.nextNode
		L.head.value = result
	return int(L.head.value)


def calculate_operation(num1, num2, operation):
	if operation == "/": return num1 // num2
	elif operation == "*": return num1 * num2
	elif operation == "+": return num1 + num2
	elif operation == "-": return num1 - num2



##################################################


def inorderSucessor(node):
  current=node
  if current.leftNode==None and current.rigthNode==None: #No tiene hijos
    if current.parent==None: #Es un nodo aislado(ni padre ni hijos)
      return None
    else:
      if current.parent.key>current.key: #tiene padre y su key es mayor
        return current.parent.value 
      else:
        return None
  else:    #tiene hijos y posiblemente padre(siempre y cuando no sea la raiz)
    while current.parent!=None:
      current=current.parent
    NewTree=BinaryTree()
    NewTree.root=current
    L=traverseinorderKey(NewTree)
    nodoAUX=searchKeyList(L, node.value)
    if nodoAUX.nextnode==None:
      return None
    else:
      return nodoAUX.nextnode.value



def searchKeyList(L,element):
	current = L.head

	while current != None:
		if current.key == element:
			return current
		current = current.nextNode
	return
    