from array import *
from linkedlist import *

class dictionaryNode:
  value=None
  key=None
  nectNode=None

class dictionary:
  head=None

def hash(k, m):
    if m==None or k==None:
        return None
    else:
        pos= k % m
        return pos

def insert(D, key, value):
  if D==0 or D==None:
    print('Error. No se encontró una tabla Hash.')
    return None
  else:
    i=hash(key, len(D))
    if D[i]==None:
      List=[]
      node=(key, value)
      List.append(node)
      D[i]=List
    else:
      node=(key, value)
      D[i].append(node)

def search(D, key):
  if D==None or key==None:
    print('Error, valores inválidos.')
  else:
    index=hash(key, len(D))
    if D[index]!=None:
      current=D[index]
      while current!=None:
        if current.key==key:
          return current.value
        else:
          current=current.nextNode
def delete(D, key):
  if search(D, key)!=None:
    index=hash(key, len(D))
    current=D[index]
    while current!=None:
      if current.key==key:
        D[index].pop(current)
        return D


