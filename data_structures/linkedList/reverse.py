from definition import ListNode
from Ageneral import printList

def reverseList(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


# reverse recursively
def reverseList_recursively(head):
    if head is None or head.next is None:
        return head
    p = reverseList_recursively(head.next)
    head.next.next = head
    head.next = None
    return p

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next=b
b.next=c
c.next=d
d.next=e

printList(a)
reverseList(a)
printList(e)
