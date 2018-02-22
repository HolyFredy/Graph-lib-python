class Graph:
    def __init__(self):
        self.vertices = []

    def __init__(self, x:Vertex):
        self.add_vertex(x)

    def __init__(self, x:list):
        self.add_vertices(x)

    def add_vertex(self, x):
        if isinstance(x, Vertex):
            self.vertices.append(x)
        else:
            return False

    def add_vertices(self, x):
        for y in x:
            self.add_vertex(y)

    def show(self):
        for x in self.vertices:
            x.show()

    def check_loops(self): # check if vertex can go to all vertices

        for x in self.vertices:
            check = 0
            for y in self.vertices:
                if not x.find_path(y):
                    print(x.name + " can't go to " + y.name)
                    check += 1
            else:
                if not check:
                    print(x.name + " can go to all vertices.")
        return True

class Vertex:
    def __init__(self, x):
        self.name = x
        self.edges = []

    def __str__(self):
        return self.name

    def find_path(self, end, path=[]):
        if self.name in path and self != end:
            return None
        path = path + [self.name]
        if self == end and len(path) > 1:
            return path
        for x in self.edges:
            newpath = x.find_path(end, path)
            if newpath: return newpath
        return None

    def find_all_path(self, end, path=[]):
        if self.name in path and self != end:
            return None
        path = path + [self.name]
        if self == end and len(path) > 1:
            return [path]
        paths = []
        for x in self.edges:
            if x not in path:
                newpaths = x.find_all_path(end, path)
                if newpaths:
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths

    def show(self):
        print(self.name + " : ", end="")
        for x in self.edges:
            print(x, end=" ")
        print()

    def add_edge(self, x):
        if isinstance(x, Vertex):
            self.edges.append(x)
        else:
            return False

    def add_edges(self, x):
        for y in x:
            self.add_edge(y)

if __name__ == '__main__':
    # some test
    my_graph = Graph()

    my_graph.add_vertices([Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")])

    my_graph.vertices[0].add_edges([my_graph.vertices[1]])
    my_graph.vertices[1].add_edges([my_graph.vertices[2]])
    my_graph.vertices[2].add_edges([my_graph.vertices[3], my_graph.vertices[4]])
    my_graph.vertices[3].add_edges([my_graph.vertices[0], my_graph.vertices[5]])
    my_graph.vertices[4].add_edges([my_graph.vertices[1]])
    my_graph.vertices[5].add_edges([my_graph.vertices[1]])

    my_graph.show()
    my_graph.check_loops()
