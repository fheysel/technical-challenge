MAX = 999999.99

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # Number of vertices in graph
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)] # Empty distance matrix
        self.mst = [] # Minimum spanning tree of graph
        self.path = [] # Final path for 

    def calc_path(self):
        # Calculate the path by doing a pre-order traversal of the MST
        for i in self.mst:
            if i[0] not in self.path:
                self.path.append(i[0])
            if i[1] not in self.path:
                self.path.append(i[1])
    
    def calc_mst(self):
        # Calculate the minimum spanning tree using Prim's algorithm
        
        edges = 0 # counter to keep track of number of edges in mst
        visited = [False] * self.vertices # List to keep track of which vertices have been visited
        visited[0] = True # Add the first vertex to the set of visited vertices
        self.path.append(0)
        
        while (edges < self.vertices - 1):
            min = MAX

            # Variables to keep track of the indicies of the current best edge in the distance matrix 
            x = -1
            y = -1

            for i in range(self.vertices):
                if visited[i]:
                    for j in range(self.vertices):
                        if ((not visited[j]) and self.graph[i][j]):
                            # If not already in the mst and distance is not zero, check how the edge compares to current best
                            if min > self.graph[i][j]:
                                min = self.graph[i][j]
                                x = i
                                y = j

            visited[y] = True # Mark vertex as visited
            self.mst.append([x, y]) # Add to MST
            edges += 1



            
