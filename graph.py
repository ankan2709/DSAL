class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        # O(1)
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        # O(1)
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        # O(E)
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
        return False
    
    def remove_vertex(self, vertex):
        # O(v + e)
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)

            del self.adj_list[vertex]
            return True
        return False
        




    

myGraph = Graph()
myGraph.add_vertex(1)
myGraph.add_vertex(2)
myGraph.add_vertex(3)
myGraph.add_edge(1, 2)
myGraph.print_graph()
myGraph.remove_edge(1,3)
myGraph.print_graph()