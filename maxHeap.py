class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2*index + 1
    
    def _right_child(self, index):
        return 2*index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] =  self.heap[index2], self.heap[index1] 

    def print_heap(self):
        print(self.heap)

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self.swap(current, self._parent(current))
            current = self._parent(current)

    def sinkDown(self, index):
        max_index = index
        while True:
            right = self._right_child(index)
            left = self._left_child(index)
            if (left < len(self.heap) and self.heap[left] > self.heap[max_index]):
                max_index = left
            if (right < len(self.heap) and self.heap[right] > self.heap[max_index]):
                max_index = right
            if max_index != index:
                self.swap(max_index, index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sinkDown(0)
        return max_value



myHeap = MaxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)
myHeap.insert(58)

myHeap.insert(100)
myHeap.insert(75)
myHeap.print_heap()
myHeap.remove()
myHeap.print_heap()
myHeap.remove()
myHeap.print_heap()