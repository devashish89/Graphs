# Undirected/Directed Graph
# https://www.youtube.com/watch?v=g65I8-qwY2c&list=PLFV6T8f5WU2GdWGvhmLnlACuQaFtG2Nu3&index=2
# nodes/vertices = A,B,C,D,E
# edges AB,BC,CD,AD,DE
# Adjacency List if Undirected Graph
# {A:[B,D]
# B:[A,C]
# C:[B,D]
# D:[A,C,E]
# E:[D]}
#
# Adjacency List if Directed Graph
# {A:[B,D]
# B:[C]
# C:[D]
# D:[E]
# E:[]}
class Graph:
    def __init__(self, vertices, is_directed):
        self.nodes = vertices
        self.adjacency_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_edges(self, u, v):
        if u in self.nodes and v in self.nodes:
            self.adjacency_list[u].append(v)
            if not self.is_directed:
                self.adjacency_list[v].append(u)
            return True
        return False

    def add_node(self, Node):
        node = Node
        self.nodes.append(node)
        self.adjacency_list[node] = []

    def get_degree(self, Node):
        node = Node
        if node in self.nodes:
            return len(self.adjacency_list[node])
        return -1

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


from collections import deque


def bfs(graph, startVertex):
    # uses queue: FIFO
    queue = deque()
    visited = []
    node = startVertex
    queue.append(node)
    visited.append(node)
    while len(queue) > 0:
        cur = queue.popleft()
        print(cur, end=" ")

        for neighbour in graph.adjacency_list[cur]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


def dfs(graph, startVertex):
    # uses stack: LIFO
    stack = deque()
    visited = []
    node = startVertex
    stack.append(node)
    visited.append(node)
    while len(stack) > 0:
        cur = stack.pop()
        print(cur, end=" ")

        for neighbour in graph.adjacency_list[cur]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)


if __name__ == '__main__':
    Nodes = ['A', 'B', 'C', 'D', 'E']
    graph = Graph(Nodes, is_directed=True)
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D'), ('D', 'E')]
    for edge in edges:
        n1, n2 = edge
        graph.add_edges(n1, n2)

    # graph.add_node('F')
    graph.print_graph()
    print("Degree of node 'A':", graph.get_degree('A'))
    print("-" * 20)
    print("*** BFS : Breadth First Traversal ****")
    bfs(graph, 'A')
    print(end="\n")
    print("-" * 20)
    print("*** DFS : Depth First Traversal ****")
    dfs(graph, 'A')
