class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.lenght = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enque(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1

    def deque(self):
        if self.lenght == 0:
            return None
        
        temp = self.first
        if self.lenght == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.lenght -= 1
        return temp



# my_queue = Queue(1)
# my_queue.enque(2)
# my_queue.enque(2)
# my_queue.print_queue()
# print(my_queue.deque())
# print(my_queue.deque())
# print(my_queue.deque())
# print(my_queue.deque())
# my_queue.print_queue()



exp = '{[()]}'

closeToOpen = {"}":"{", "]":"[", ")":"("}

stackList = []

for item in exp:
    if item in closeToOpen:
        if stack and stack[-1] == closeToOpen[item]:
            stack.pop()
        else:
            return False

    else:
        stackList.append(item)

