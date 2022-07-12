MAX = 999999.99

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # Number of vertices in graph
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)] # Empty distance matrix
        self.path = [] # Minimum spanning tree of graph
    
    def calc_path(self):
        # Calculate the minimum spanning tree using Prim's algorithm
        
        edges = 0 # counter to keep track of number of edges in path
        visited = [False] * self.vertices # List to keep track of which vertices have been visited
        visited[0] = True # Add the first vertex to the set of visited vertices
        
        while (edges < self.vertices - 1):
            min = MAX

            # Variables to keep track of the indicies of the current best edge in the distance matrix 
            x = -1
            y = -1

            for i in range(self.vertices):
                if visited[i]:
                    for j in range(self.vertices):
                        if ((not visited[j]) and self.graph[i][j]):
                            # If not already in the path and distance is not zero, check how the edge compares to current best
                            if min > self.graph[i][j]:
                                min = self.graph[i][j]
                                x = i
                                y = j

            visited[y] = True
            print(str(x) + "-" + str(y) + ":" + str(self.graph[x][y]))
            self.path.append([x, y])
            edges += 1



            
