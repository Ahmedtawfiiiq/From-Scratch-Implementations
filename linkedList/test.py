# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def todecimal(ll):
    number = ""
    while ll:
        number += str(ll.val)
        ll = ll.next
    return number


class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = todecimal(l1)
        n2 = todecimal(l2)
        summation = int(n1) + int(n2)
        l3 = ListNode()
        ptr = l3
        for digit in str(summation)[::-1]:
            ptr.next = ListNode(int(digit))
            ptr = ptr.next
        return l3.next

from Ageneral import printList


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f

s = Solution()
l3 = s.addTwoNumbers(a, d)
printList(l3)
