#Giraudo Ignacio 13855  LCC

from algo1 import *

#Función Search
def search(array,element):  
  position=0                
  for i in range (0,len(array)):  
    if element == array[i]: 
      position=position+i  
      in_array=False   
      break       
    else: 
      in_array=True   
  if in_array==False: 
   return(position)   
  else:
   return(None)     
    
#Función insert
def insert(array,element,position): 
  if position>=0 and position< len(array):  
    for i in range(len(array)-1,position,-1): 
       array[i]=array[i-1] 
    array[position]=element 
    return(position)
  else:
    return(None) 
    
#Función delete
def delete(array,element): 
  position=0
  for i in range(0,len(array)):
    if array[i]==element:
      position=i
      for j in range(i,len(array)-1):
          array[j]=array[j+1]
      in_array=True
      array[len(array)-1]=None
      break
    else:
      in_array=False
      
  if in_array==True:
    return(position)
  else:
    return(None)
    
#Funcion lenght
def length(array):
  cont=0
  for i in range(0,len(array)):
    if array[i] != None:
      cont= cont+1
  return (cont)