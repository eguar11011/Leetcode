# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:      
        # Instanciamos nuestra lista 
        ans = ListNode()# nodo vacio
        current = ans
        # Creamos nuestro carry
        carry: int = 0
        while l1 or l2 or carry:
            sumal1l2 = carry
            # sumamos los valores correspientes
            if l1: sumal1l2 += l1.val; l1 = l1.next
            if l2: sumal1l2 += l2.val; l2 = l2.next

            # carry y digito
            carry = sumal1l2//10
            digito= sumal1l2%10

            current.next = ListNode(digito)
            current = current.next
        return ans.next
    
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

l1_values = [2, 4, 3]
l2_values = [5, 6, 4]

l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Imprimir el resultado
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")