"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# graph = Graph()
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Queue
        queue = Queue()
        visited = set()
        # current = starting_vertex
        # while current:
        #     visited.add(current)
        #     print(current)

        #     for v in self.vertices[current]:
        #         if v not in visited:
        #             queue.enqueue(v)

        #     if queue.size() == 0:
        #         break

        #     current = queue.dequeue()
        #     while current in visited and current is not None:
        #         current = queue.dequeue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Stack
        stack = Stack()
        visited = set()
        # current = starting_vertex
        # while current:
        #     visited.add(current)
        #     print(current)

        #     for v in self.vertices[current]:
        #         if v not in visited:
        #             stack.push(v)

        #     if stack.size() == 0:
        #         break

        #     current = stack.pop()
        #     while current in visited and current is not None:
        #         current = stack.pop()

        stack.push(starting_vertex)
        while stack.size() > 0:
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex is None:
            return
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
        else:
            return
        edges = self.get_neighbors(starting_vertex)
        for edge in edges:
            self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    queue.enqueue(current_path + [edge])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    stack.push(current_path + [edge])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set(), path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if starting_vertex is not None:
        visited.add(starting_vertex)
        # path.append(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            # Base Case
            return path
        edges = self.get_neighbors(starting_vertex)
        for edge in edges:
            if edge not in visited:
                possible_path = self.dfs_recursive(edge, destination_vertex, visited, path)
                if possible_path:
                    return possible_path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("BFT")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    # '''
    print("DFT")
    graph.dft(1)
    print("DFT RECURSIVE")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    # '''
    print ("DFS")
    print(graph.dfs(1, 6))
    print("DFS RECURSIVE")
    print(graph.dfs_recursive(1, 6))
