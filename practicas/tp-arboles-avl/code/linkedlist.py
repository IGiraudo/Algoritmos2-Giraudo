#Giraudo Ignacio 13855  LCC

from algo1 import *
class LinkedList:
  head=None
  value=None
  nextNode=None
class Node:
  value=None
  nextNode=None
  
#Función Add
def add(L,element):
	current = L.head
	newNode = Node()
	newNode.value = element

	if current == None:
		L.head = newNode
	else:
		newNode.nextNode = current
		L.head = newNode
	return
  
#Funcion Search
def search(L,element):
	current = L.head
	currentPos = 0

	while current != None:
		if current.value == element:
			return currentPos

		current = current.nextNode
		currentPos += 1
	return
    
#Funcion Insert
def insert(L,element,position):
	current = L.head
	currentPos = 0

	if position == 0:
		add(L,element)
		return position

	elif position > 0:
		if current == None: return
		newNode = Node()
		newNode.value = element

		while current.nextNode != None:
			if currentPos+1 != position:
				current = current.nextNode
				currentPos += 1
			else:
				newNode.nextNode = current.nextNode
				current.nextNode = newNode
				return position
		current.nextNode = newNode
		return currentPos+1
	return
    
#Funcion Delete
def delete(L,element):
	current = L.head
	position = search(L, element)
	if position == None: return
	if position == 0: 
		L.head = L.head.nextNode
		return position

	for i in range(0, position-1):
		current = current.nextNode
	current.nextNode = current.nextNode.nextNode
	return position
  
#Funcion length
def length(L):
	current = L.head
	currentPos = 0
	while current != None:
		current = current.nextNode
		currentPos += 1
	return currentPos

#Función Access
def access(L,position):
	if position >= 0:
		current = L.head

		for i in range(0, position):
			if current == None: return
			current = current.nextNode
		return current.value
	return
  
#Función Update
def update(L,element,position):
	if position >= 0:
		current = L.head

		for i in range(0, position):
			current = current.nextNode
			if current == None: return
		current.value = element
		return position
	return