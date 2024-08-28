from collections import defaultdict

# Create a class for the graph
class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Helper function to print all paths from start to end
    def _print_all_paths_util(self, start, end, visited, path):
        visited[start] = True
        path.append(start)
        
        # If start is the same as end, print the path
        if start == end:
            print(' -> '.join(map(str, path)))
        else:
            # Recur for all the vertices adjacent to this vertex
            for node in self.graph[start]:
                if not visited[node]:  # Ensure no cycles
                    self._print_all_paths_util(node, end, visited, path)
        
        # Backtrack
        path.pop()
        visited[start] = False

    # Function to print all paths from start to end
    def print_all_paths(self, start, end):
        # Ensure all nodes are in the visited dictionary
        nodes = set(self.graph.keys())
        for adj in self.graph.values():
            nodes.update(adj)
        
        # Initialize visited dictionary for all nodes
        visited = {node: False for node in nodes}
        
        # Store the path
        path = []
        
        # Call the recursive helper function to print all paths
        self._print_all_paths_util(start, end, visited, path)

# Create the graph given in the problem
g = Graph()

# Adding edges according to the table provided
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 6)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(6, 7)
g.add_edge(7, 8)

# Print all unique paths from Node 1 to Node 8
print("All unique paths from Node 1 to Node 8:")
g.print_all_paths(1, 8)
