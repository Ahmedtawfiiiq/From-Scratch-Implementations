def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
