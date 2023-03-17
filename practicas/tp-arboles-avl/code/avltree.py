#Giraudo Ignacio 13855  LCC
from array import *
from binarytree import *
from ejtadarbol import *
from linkedlist import *
from algo1 import *
from libreriaPiru import *


class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftNode = None
  rightNode = None
  key = None
  value = None
  bf = None

  def search(B, element): #O(n)
    node = searchNodeR(B.root, element)
    if node == None: return
    else: return node.key


# Función recursiva de search
def searchNodeR(node, element):
    if node == None: return

    if node.value == element:
        return node

    right = searchNodeR(node.rightnode, element)
    if right != None:
        return right

    left = searchNodeR(node.leftnode, element)
    if left != None:
        return left


''' Descripción: Busca un elemento en el TAD árbol binario.
Salida: Devuelve el nodo asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra. '''


def searchNode(B, element):
    return searchNodeR(B.root, element)


''' Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.
Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None. '''


def insert(B, element, key): #O(n)
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element

    if (B.root == None):
        B.root = newNode
        return key
    return insertR(newNode, B.root)


# Función recursiva de insert
def insertR(newNode, currentNode):
    if newNode.key > currentNode.key:
        if currentNode.rightnode == None:
            newNode.parent = currentNode
            currentNode.rightnode = newNode
            return newNode.key
        else:
            right = insertR(newNode, currentNode.rightnode)
            if right != None:
                return right
    else:
        if currentNode.leftnode == None:
            newNode.parent = currentNode
            currentNode.leftnode = newNode
            return newNode.key
        else:
            left = insertR(newNode, currentNode.leftnode)
            if left != None:
                return left


''' Descripción: Elimina un elemento del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
Salida: Devuelve clave (key) del elemento '''


def delete(B, element): #O(n)
    node = searchNode(B, element)
    if node == None: return
    else: return deleteCurrentCase(B, node)


# Valida y ejecuta los distintos casos de delete
def deleteCurrentCase(B, node):
    if node.rightnode == None:
        if node.leftnode == None:

            # Caso 1: El nodo a eliminar es una hoja
            if node.parent.leftnode != None and node.parent.leftnode == node:
                node.parent.leftnode = None
                return node.key
            elif node.parent.rightnode != None and node.parent.rightnode == node:
                node.parent.rightnode = None
                return node.key

        # Caso 2: El nodo a eliminar tiene un hijo del lado izquierdo
        if node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.leftnode
            return node.key
        elif node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.leftnode
            return node.key

    else:
        # Caso 2: El nodo a eliminar tiene un hijo del lado derecho
        if node.leftnode == None:
            if node.parent.leftnode == node:
                node.parent.leftnode = node.rightnode
                return node.key
            elif node.parent.rightnode == node:
                node.parent.rightnode = node.rightnode
                return node.key
        else:
            # Caso 3: El nodo a eliminar tiene dos hijos
            ''' # eliminar el menor de sus mayores   '''
            changeNode = smallerOf(node.rightnode)

            node.value = changeNode.value
            oldKey = node.key
            node.key = changeNode.key

            if changeNode.parent.leftnode == changeNode:
                changeNode.parent.leftnode = None
            elif changeNode.parent.rightnode == changeNode:
                changeNode.parent.rightnode = None

            return oldKey

            # o eliminar el mayor de sus menores
            changeNode = bigger(node.leftnode)

            node.value = changeNode.value
            oldKey = node.key
            node.key = changeNode.key

            if changeNode.parent.leftnode == changeNode:
                changeNode.parent.leftnode = None
            elif changeNode.parent.rightnode == changeNode:
                changeNode.parent.rightnode = None

            return oldKey


# Devuelve el elemento con menor key desde un nodo dado
def smaller(node):
    if node.leftnode != None:
        current = smaller(node.leftnode)
        if current != None:
            return current
    else:
        return node


# Devuelve el elemento con mayor key desde un nodo dado
def bigger(node):
    if node.rightnode != None:
        current = bigger(node.rightnode)
        if current != None:
            return current
    else:
        return node


def smallerOf(node):
    if node.leftnode != None:
        changeNode = smallerOf(node.leftnode)
        if changeNode != None:
            return changeNode
    elif node.rightnode != None:
        changeNode = smallerOf(node.rightnode)
        if changeNode != None:
            return changeNode
    else:
        return node


def biggerOf(node):
    if node.rightnode != None:
        changeNode = biggerOf(node.rightnode)
        if changeNode != None:
            return changeNode
    elif node.leftnode != None:
        changeNode = biggerOf(node.leftnode)
        if changeNode != None:
            return changeNode
    else:
        return node


'''Descripción: Elimina una clave del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra. '''


def deleteKey(B, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else: return deleteCurrentCase(B, node)


# Función recursiva de searchKey
def searchKeyR(node, key):
    if node == None: return

    if node.key == key:
        return node

    right = searchKeyR(node.rightnode, key)
    if right != None:
        return right

    left = searchKeyR(node.leftnode, key)
    if left != None:
        return left


''' Descripción: Permite acceder a un elemento del árbol binario con una clave determinada.
Salida: Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave. '''


def access(B, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else: return node.value


''' Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada.
Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de element.
Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update. '''


def update(B, element, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else:
        node.value = element
        return node.key

##########################################################################################################################

#Ej 1: rotación a la izquierda
def rotateLeft(Tree, avlnode):
  current = avlnode
  if current.rightNode == None:  #Árbol de un solo nodo
    return avlnode
  elif current.rightNode.rightNode == None and current.rightNode.leftNode == None:  #RigthNode no tiene hijos
    current.rightNode.leftNode = current
    if current.parent!=None:
      current.rightNode.parent = current.parent
    else:
      Tree.root=current.rightNode
  elif current.rightNode.rightNode != None and current.rightNode.leftNode == None:  #Un solo hijo a la derecha
    current.rightNode.leftNode = current
    current.parent = current.rightNode
    if avlnode.parent!=None:
      current.rightNode.parent = current.parent
    else:
      Tree.root=current.rightNode    
  elif current.rightNode.rightNode == None and current.rightNode.leftNode != None:  #un solo hijo a la izquierda
    current.rightNode.rightNode = current
    current.rightNode.rightNode.rightNode = current.rightNode.leftNode
    current.rightNode.LeftNode = None
    if avlnode.parent!=None:
      current.rightNode.parent = current.parent
    else:
      Tree.root=current.rightNode
  elif current.rightNode.rightNode != None and current.rightNode.leftNode != None:  #dos hijos
    current.leftNode = current.rightNode.leftNode
    current.rightNode.leftNode = current
    current.rightNode.leftNode.rightNode = current.rightNode.leftNode.leftNode
    current.rightNode.leftNode.leftNode = None
    if avlnode.parent!=None:
      current.rightNode.parent = current.parent
    else:
      Tree.root=current.rightNode
  return Tree.root
  
def rotateRight(Tree, avlnode):
  current = avlnode
  if current.leftNode==None:
    return Tree
  elif current.leftNode!=None:
    if current.leftNode.leftNode==None and current.leftNode.rightNode==None: #sin hijos
      current.leftNode.rightNode=current
      if current.parent!=None:
        current.leftNode.parent=current.parent
      else:
        Tree.root=current.leftNode
        
    elif current.leftNode.leftNode!=None and current.leftNode.rightNode==None: #un hijo a la izq
      current.leftNode.rightNode=current
      if current.parent!=None:
        current.leftNode.parent=current.parent
      else:
        Tree.root=current.leftNode
        
    elif current.leftNode.leftNode==None and current.leftNode.rightNode!=None: #un hijo a la derecha
      current.rightNode=current.leftNode.rightNode
      current.leftNode.rightNode=current
      current.leftNode.rightNode.leftNode=current.leftNode.rightNode.rightNode
      current.leftNode.rightNode.rightNode=None
      if current.parent!=None:
        current.leftNode.parent=current.parent
      else:
        Tree.root=current.leftNode
    elif current.leftNode.leftNode!=None and current.leftNode.rightNode!=None:  #DOS HIJOS
      current.rightNode=current.leftNode.rightNode
      current.leftNode.rightNode=current
      current.leftNode.rightNode.leftNode=current.rightNode
      current.leftNode.rightNode.rightNode=None
      if current.parent!=None:
        current.leftNode.parent=current.parent
      else:
        Tree.root=current.leftNode

def CalculateBFTree(AVLTree,avlnode): 
  SubTleft=0
  SubTright=0
  bf=0
  if avlnode.leftnode!=None:
    avlnode=avlnode.leftnode
    node=leftnode
    SubTleft=1
    while avlnode.leftnode!=None or avlnode.rightnode!=None:
      if  avlnode.leftnode.leftnode!=None or avl.leftnode.rightnode!=None:
        node=leftnode
      elif avlnode.rightnode.leftnode!=None or avl.rightnode.rightnode!=None:
        node=rightnode
      else:
        node=leftnode
      SubTleft+=1
      avlnode=avlnode.node
  
  if avlnode.rightnode!=None:
    avlnode=avlnode.rightnode
    node=rightnode
    SubTright=1
    while avlnode.leftnode!=None or avlnode.rightnode!=None:
      if  avlnode.rightnode.leftnode!=None or avl.rightnode.rightnode!=None:
        node=rightnode
      elif avlnode.leftnode.leftnode!=None or avl.leftnode.rightnode!=None:
        node=leftnode
      else:
        node=rightnode
      SubTright+=1
      avlnode=avlnode.node
  bf=SubTleft-SubTright
  return bf

  #Ejercicio 2
  def calculateBalance(AVLTree):
    AVLTreeBalanced=AVLTree()
    avlnode=AVLTree.root
    AVLTreeBalanced=calculateBalanceR(AVLTree,avlnode)
    return AVLTreeBalanced
  def calculateBalanceR(AVLTree,avlnode)
    avlnode.bf=CalculateBFTree(AVLTree,avlnode)
    calculateBalanceR(AVLTree,avlnode.leftnode)
    calculateBalanceR(AVLTree,avlnode.rightnode)
    return AVLTree

#Ejercicio 3

def searchAVLBF(AVLTree):
    node = searchNodeR(B.root)
    if node == None: return
    else: return node.key

# Función recursiva de search 
def searchAVLBF_R(node):
    if node == None: return

    if node.bf < -1 or node.bf > 1 :
      return node

    right=searchNodeR(node.rightnode)
    if right != None:
      return right

    left = searchNodeR(node.leftnode)
    if left != None:
      return left

def reBalance(AVLTree):
  AVLTree=calculateBalance(AVLTree)
  avlnode=searchAVLBF(AVLTree)
  while avlnode!=None:
    if avlnode.bf < 0:
      if avlnode.rightnode.bf > 0:
        rotateRight(avlnode.rightnode)
        rotateLeft(avlnode)
      else:
        rotateLeft(avlnode)
    elif avlnode.bf > 0:
        if avlnode.leftnode.bf < 0:
          rotateLeft(avlnode.leftnode)
          rotateRight(avlnode)
        else:
          rotateRight(avlnode)
    AVLTree=calculateBalance(AVLTree)
    avlnode=searchAVLBF(AVLTree)
  return AVLTree

#Ejercicio 4

def InsertAVL(AVLTree, avlnode):
  insert(AVLTree, avlnode, avlnode.key)
  reBalance(AVLTree)
  return AVLTree

#Ejercicio 5

def DeleteAVL(AVLTree, avlnode):
  deleteKey(AVLTree, avlnode.key)
  reBalance(AVLTree)
  return AVLTree
