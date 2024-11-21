import collections
class SnapshotArray:

    def __init__(self, length):
        self.snap_id = 0
        self.mymap = collections.defaultdict(list)

    def set(self, index, val):
        if self.mymap[index] and self.mymap[index][-1][0] == self.snap_id:
            self.mymap[index][-1] = (self.snap_id, val)
        else:
            self.mymap[index].append((self.snap_id, val))

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index, snap_id):
        if index not in self.mymap:
            return 0
            



# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0,5)
param_2 = obj.snap()
param_3 = obj.get(0,0)

print(param_2)
print(param_3)