from time import process_time
from Graph import Graph

def main(G):
    start = process_time()
    G.calc_path()
    end = process_time()
    print(f'Path of graph is {G.path}. Processing time is {end - start} seconds.')

def test():
    G = Graph(5)
    G.graph = [[0, 9, 75, 0, 0],
               [9, 0, 95, 19, 42],
               [75, 95, 0, 51, 66],
               [0, 19, 51, 0, 31],
               [0, 42, 66, 31, 0]]

    main(G)
    
     
test()