# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev

# reverse recursively
def reverseList_recursively(head):
    if head is None or head.next is None:
        return head
    p = reverseList_recursively(head.next)
    head.next.next = head
    head.next = None
    return p

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

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

reverseList_recursively(e)
printList(a)
