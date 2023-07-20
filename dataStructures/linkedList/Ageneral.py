from definition import ListNode


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# insertion at a given position in a singly linked list
def insert(head, data, index):
    newNode = ListNode(data)
    if index == 0:
        newNode.next = head
        return newNode
    curr = head
    i = 0
    while i < index - 1:
        curr = curr.next
        i += 1
    newNode.next = curr.next
    curr.next = newNode
    return head
