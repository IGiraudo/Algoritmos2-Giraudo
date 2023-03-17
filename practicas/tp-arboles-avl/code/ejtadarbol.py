#EJERCITACIÓN TAD ARBOL
#Giraudo Ignacio 13855  LCC

from algo1 import *
from linkedlist import *
from mystack import *
from libreriaPiru import revert
from myqueue import *
from binarytree import *


class BinaryTree:
  root = None

class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None

#EJERCICIO 1
def verify_balanceP(B):
    current = B.root
    balance = verify_balanceR(B, current)
    return balance

def verify_balanceR(B, current):
    if current.leftnode == None and current.rightnode == None:
        return True
    elif current.leftnode == None and current.rightnode != None:
        if current.rightnode.leftnode != None or current.rightnode.rightnode != None:
            return False
        else:
            return True
    elif current.leftnode != None and current.rightnode == None:
        if current.leftnode.leftnode != None or current.leftnode.rightnode != None:
            return False
        else:
            return True
    else:  #Caso recursivo
        if current.leftnode.leftnode != None or current.leftnode.rightnode != None:
            bool1 = True
        else:
            return True
        if current.rightnode.leftnode != None or current.rightnode.rightnode != None:
            bool2 = True
        else:
            return True
        if bool1 == True and bool2 == True:
            verify_balanceR(B, current.leftnode)
            verify_balanceR(B, current.rightnode)
        else:
            return False

#EJERCICIO 2
def searchkey(B, key):
    current = B.root
    auxkey = key
    current = searchkeyR(B, current, auxkey)
    return current

def searchkeyR(B, current, auxkey):
    if current.key != None:
        if current.key == auxkey:
            return current
        elif current.leftnode.key != None:
            if current.leftnode.key == auxkey:
                return current.leftnode
            else:
                searchkeyR(B, current.leftnode, auxkey)
        elif current.rightnode.key != None:
            if current.rightnode.key == auxkey:
                return current.rightnode
            else:
                searchkeyR(B, current.rightnode, auxkey)
        else:
            return None
    else:
        return None


def TreeinTreeP(BT1, BT2):
    current2 = BT2.root
    rootintree = searchkey(BT1, current2.key)
    treeintree = TreeinTreeR(BT1, BT2, rootintree, current2)
    return treeintree


def TreeinTreeR(BT1, BT2, rootintree, current2):
    if rootintree == None:
        return False
    else:
        if current2.leftnode.key != None and rootintree.leftnode.key != None:
            if current2.leftnode.key == rootintree.leftnode.key:
                if current2.rightnode.key != None and rootintree.rightnode.key != None:
                    if current2.rightnode.key == rootintree.rightnode.key:
                        if rootintree.leftnode.leftnode != None or rootintree.leftnode.rightnode != None:
                            booll = True
                            if rootintree.rightnode.leftnode != None or rootintree.lrightnode.rightnode != None:
                                boolr = True
                            else:
                                return True
                        else:
                            return True
                elif current2.rightnode.key == None and rootintree.rightnode.key == None:
                    if rootintree.leftnode.leftnode != None or rootintree.leftnode.rightnode != None:
                        booll = True
                    else:
                        return True
                else:
                    return False
            else:
                return False
        elif current2.leftnode.key == None and rootintree.leftnode.key == None:
            if current2.rightnode.key != None and rootintree.rightnode.key != None:
                if current2.rightnode.key == rootintree.rightnode.key:
                    if rootintree.rightnode.leftnode != None or rootintree.lrightnode.rightnode != None:
                        boolr = True
                    else:
                        return True
            elif current2.rightnode.key == None and rootintree.rightnode.key == None:
                return True
            else:
                return False

        else:
            return False

        if booll == True and boolr == True:
            TreeinTreeR(BT1, BT2, rootintree.leftnode, current2.leftnode)
            TreeinTreeR(BT1, BT2, rootintree.rightnode, current2.rightnode)
        elif booll == True and boolr != True:
            TreeinTreeR(BT1, BT2, rootintree.leftnode, current2.leftnode)
        elif booll != True and boolr == True:
            TreeinTreeR(BT1, BT2, rootintree.rightnode, current2.rightnode)
 
#EJERCICIO 3
#con traverseinorder verificamos que la lista quede ordenada de menor a mayor dado que leftnode < currentnode < rightnode.
def traverseinorderKey(B):
  L = LinkedList()
  traverseinorderKeyR(B.root, L)
  return revert(L)

#in order recursivo
def traverseinorderKeyR(node, L):
  if node != None:
    traverseinorderKeyR(node.leftnode, L)
    add(L, node.key)
    traverseinorderKeyR(node.rightnode, L)

def checkBST(B):
  list = traverseinorderKey(B)
  current = list.head
  #verificamos los valores
  while current.nextNode != None:
    if current.value > current.nextNode.value:
      return False
    current = current.nextNode
  return True
