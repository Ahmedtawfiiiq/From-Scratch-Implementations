from definition import ListNode
from Ageneral import insert, printList

a = ListNode(5)
b = ListNode(23)
c = ListNode(7)
d = ListNode(13)

a.next = b
b.next = c
c.next = d

h = insert(a, 9, 2)
printList(h)
h = insert(a, 9, 0)
printList(h)
