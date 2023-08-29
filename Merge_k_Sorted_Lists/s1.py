# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def remove_head(self):
        if self.next:
            self.val = self.next.val
            self.next = self.next.next
        else:
            self.val = None
            self.next = None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans: ListNode = ListNode() # Nodo vacio
        current: ListNode = ans # Seguimiento del Nodo
        k:int = len(lists) # k-listas
        limit: bool = True 
        index: int = 0
        valor_menor: int =  10 ** 4
        pointer = None

        while limit:  # Si todos los ll estan vacios limit sera False
            print(valor_menor)
            ll: ListNode = lists[index] # likend-list actual ; likend-list=ll

            if ll.val == None: pass
            elif (valor_menor >= ll.val): 
                valor_menor = ll.val # guardar el valor 
                pointer = ll  # Puntero a la ll con el valor menor

            index = (index +1) % k # indice que elije una ll

            if index == 0: # cuando index es cero, es porque ya paso por todas las ll
                current.val = valor_menor # Guardamos el valor en ans
                current.next = ListNode()  # Crear un nuevo nodo 
                current = current.next  # Mover el puntero 'current' al siguiente nodo

                pointer.remove_head() # eliminamos el nodo de la ll actual
                valor_menor = 10 ** 4
            print([j.val is not None for j in lists])
            print([j.val for j in lists])
            limit = any(j.val is not None for j in lists) # Comprobamos si todos los ll estan vacios

        return ans


def create_linked_list(values):
    if not values:  # Si la lista de valores está vacía
        return None  # Retornar None, ya que no hay elementos para crear la lista enlazada

    # Crear el primer nodo con el valor en la posición 0 de 'values'
    head = ListNode(values[0])  # Crea el nodo inicial (cabeza) de la lista enlazada
    current = head  # Mantener un puntero a 'head' para rastrear la posición actual

    # Recorrer los valores restantes en 'values' para crear el resto de la lista enlazada
    for val in values[1:]:  # Comenzar desde la segunda posición en adelante
        current.next = ListNode(val)  # Crear un nuevo nodo con el valor actual
        current = current.next  # Mover el puntero 'current' al nuevo nodo creado

    return head  # Retornar el nodo inicial (cabeza) de la lista enlazada


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    # Output: [1,1,2,3,4,4,5,6]
    
    
    # Creamos una lista con las listas enlazadas
    likend_lists = [create_linked_list(i) for i in lists]
    s = Solution()
    result = s.mergeKLists(likend_lists)
    
    while result:
        print(result.val, end=" -> ")
        result = result.next
    #print("None")