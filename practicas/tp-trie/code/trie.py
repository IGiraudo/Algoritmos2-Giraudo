from LinkedList import *
from algo1 import *
#Giraudo Ignacio 13855 LCC 
class Trie:
	root = None

class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

#Ejercicio 1
def insert(T, element):
    if T.root.children is None:
        T.root.children = LinkedList()
    insert_r(T.root.children, None, element, 0)

def insert_r(list, node, str, str_index):
    if str_index >= len(str): return
    char = str[str_index]
    list_node = search_list_with_trie_nodes(list, char)
    trie_node = None
    if list_node is not None:
        trie_node = list_node.value

    if trie_node is None:
        new_trie_node = TrieNode(node, LinkedList(), char, len(str) - 1 == str_index)
        add(list, new_trie_node)
        insert_r(new_trie_node.children, new_trie_node, str, str_index + 1)
    else:
        if str_index == len(str) - 1:
            trie_node.isEndOfWord = True
        insert_r(trie_node.children, trie_node, str, str_index + 1)

def search_list_with_trie_nodes(L, char):
    current = L.head
    while current != None:
        if current.value.key == char:
            return current
        current = current.nextNode
    return

def search(T, element):
    list_node = search_r(T.root.children, element, 0)
    trie_node = None
    if list_node is not None: trie_node = list_node.value
    if trie_node is None: return False
    return trie_node.isEndOfWord

# retorna el último nodo de la palabra a buscar
def search_r(list, str, str_index):
    if str_index >= len(str): return
    char = str[str_index]
    list_node = search_list_with_trie_nodes(list, char)

    if list_node is None:
        return
    else:
        if str_index == len(str) - 1:
            return list_node
        return search_r(list_node.value.children, str, str_index + 1)

#Ejercicio 3

def delete(T, element):
    list_node = search_r(T.root.children, element, 0)
    trie_node = None
    if list_node is not None: trie_node = list_node.value
    if trie_node is None or not trie_node.isEndOfWord: return False

    # El elemento es parte de otro elemento más largo
    if trie_node.children is not None:
        if trie_node.children.head is not None:
            trie_node.isEndOfWord = False
            return

    # El elemento está presente y es único (ninguna parte del elemento contiene a otro)
    while trie_node.parent is not None:
        delete_list(trie_node.parent.children, trie_node)
        # El elemento está presente y tiene al menos un elemento incluido.
        if trie_node.parent.isEndOfWord or trie_node.parent.children.head is not None: break
        trie_node = trie_node.parent
    return True

#Ejercicio 4

def print_word_with_length(T, element, n):
    node = search_r(T.root.children, element, 0)
    if node is not None:
        stack = LinkedList()
        push(stack, element)
        print_word_with_length_r(node.value.children.head, stack, n)

def print_word_with_length_r(node, stack, n):
    if node is None: return
    word = access(stack, 0) + node.value.key
    if node.value.isEndOfWord and len(word) == n:
        print(word)
       if node.value.children is not None:
        push(stack, word)
        print_word_with_length_r(node.value.children.head, stack, n)
        pop(stack)
    print_word_with_length_r(node.nextNode, stack, n)

#Ejercicio 5

def are_from_the_same_document(T1, T2):
    words1 = T1.get_words()
    words2 = T2.get_words()
    return is_sublist(words1, words2)


def is_sublist(list1, list2):
    node1 = list1.head
    while node1 is not None:
        if search(list2, node1.value) is None:
            return False
        node1 = node1.nextNode
    return True

#Ejercicio 6

def has_inverted_words(T):
    words = T.get_words()
    node = words.head
    while node is not None:
        inv_word = invert(node.value)
        if search_list(words, inv_word) is not None:
            return True
        node = node.nextNode
    return False

def invert(str):
    inv_str = ""
 for i in range(len(str), 0, -1):
        inv_str += str[i-1]
    return inv_str

#Ejercicio 7

def auto_complete(T, str):
    list_node = search_r(T.root.children, str, 0)
    trie_node = None
    if list_node is not None: trie_node = list_node.value
    ret_str = String("")

    while trie_node is not None:
        # Para evitar que se sume el último caracter de str
        if trie_node is not list_node.value:
            ret_str = concat(ret_str, String(trie_node.key))
        if trie_node.children is None or trie_node.isEndOfWord:
            return ret_str
        if trie_node.children is not None and length(trie_node.children) > 1:
            return ret_str
        trie_node = trie_node.children.head.value
    return String("")

