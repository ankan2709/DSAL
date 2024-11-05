class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp      

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < (self.length / 2):
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
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
        before = self.get(index - 1)
        after = before.next
        new_node = Node(value)

        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True
       
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        # before = self.get(index-1)
        # temp = before.next
        # after = temp.next

        # before.next = after
        # after.prev = before
        # temp.next = None
        # temp.prev = None
        # self.length -= 1

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def reverse(self):
        current_node = self.head
        while current_node is not None:
            


myDL = DoublyLL(1)
myDL.append(2)
myDL.append(100)
myDL.remove(1)
myDL.print_list()