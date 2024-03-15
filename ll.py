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
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.head is None:     # OR IF SELF.LENGTH == 0# edge case if ll is empty
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def pop(self):
    if self.length == 0:
      return None

    pre = self.head
    temp = self.head
    while (temp.next):
      pre = temp
      temp = temp.next
    self.tail = pre
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

  def popFirst(self):
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
    if temp:  # test to see of temp is actually pointing to something or the index is not within the range
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
    pre = self.head
    temp = self.head
    for i in range(index):
      pre = temp
      temp = temp.next
    new_node.next = temp
    pre.next = new_node
    self.length += 1
    return True





myList = LinkedList(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.print_list()
print()
print(myList.insert(2,100))
myList.print_list()