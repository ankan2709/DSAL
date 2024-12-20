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

  def get(self, index):  # returns a pointer and not a node
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
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      self.popFirst()
    if index == self.length - 1:
      self.pop()
    prev = self.get(index-1)
    temp = prev.next    # takes O(1) time instead of another self.get which is O(n)
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

  def find_middle_node(self):
    if self.head is None:
      return None
    fast = self.head
    slow = self.head
    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
    return slow.value
  
  def hasCycle(self):
    if self.head is None:
      return None
    visited = []
    temp = self.head
    while temp.next is not None:
      if temp in visited:
        return True
      else:
        visited.append(temp)
        temp = temp.next
    return False



  

  


myList = LinkedList(0)
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)

# myList.print_list()
print(myList.find_middle_node())
print(myList.hasCycle())


