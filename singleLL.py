class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

    def pop(self):
        """
        two edge case: one element and no element
        """
        if self.head == None:
            return None
        prev = self.head
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
            
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length() - 1:
            return self.pop()
        prev = self.get(index - 1)    # o(n)
        temp = prev.next              # o(1)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def middleNode(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value
    
    def hasLoop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


myLL = LinkedList(1)
myLL.append(2)
myLL.append(3)
myLL.append(4)
myLL.print_list()

def find_kth_from_end(my_linked_list, k):
    if my_linked_list.head is None:
        return None
    fast = my_linked_list.head
    slow = my_linked_list.head

    for _ in range(k):
        if fast:
            fast = fast.next
        else:
            return None
        
    while fast:
        slow = slow.next
        fast = fast.next
        return slow.value
    
