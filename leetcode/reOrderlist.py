def reorderList(head):
    if not head or not head.next or not head.next.next:
        return
    
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    
    before = None
    temp = slow
    slow.next = None

    while temp:
        after = temp.next
        temp.next = before
        before = temp
        temp = after 

    first = head
    second = before

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2