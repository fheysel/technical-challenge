from time import time, sleep
from Graph import Graph

def main(G):
    start = time()
    G.calc_mst()
    G.calc_path()

    # Without a sleep, the function runs too fast to accurately measure processing time
    # and always displays 0.0 runtime. By adding a 1 second delay and then subtracting
    # its affect in the elapsed variable calculation we can get a reading on the runtime
    sleep(1) 

    elapsed = time() - start - 1
    print(f'Path of graph is {G.path}. Processing time is {elapsed} seconds.')

def test():
    G = Graph(10)
    G.graph = [[0.0,  8.1,  9.2,  7.7,  9.3,  2.3,  5.1,  10.2, 6.1,  7.0],
               [8.1,  0.0,  12.0, 0.9,  12.0, 9.5,  10.1, 12.8, 2.0,  1.0],
               [9.2,  12.0, 0.0,  11.2, 0.7,  11.1, 8.1,  1.1,  10.5, 11.5],
               [7.7,  0.9,  11.2, 0.0,  11.2, 9.2,  9.5,  12.0, 1.6,  1.1],
               [9.3,  12.0, 0.7,  11.2, 0.0,  11.2, 8.5,  1.0,  10.6, 11.6],
               [2.3,  9.5,  11.1, 9.2,  11.2, 0.0,  5.6,  12.1, 7.7,  8.5],
               [5.1,  10.1, 8.1,  9.5,  8.5,  5.6,  0.0,  9.1,  8.3,  9.3],
               [10.2, 12.8, 1.1,  12.0, 1.0,  12.1, 9.1,  0.0,  11.4, 12.4],
               [6.1,  2.0,  10.5, 1.6,  10.6, 7.7,  8.3,  11.4, 0.0,  1.1],
               [7.0,  1.0,  11.5, 1.1,  11.6, 8.5,  9.3,  12.4, 1.1,  0.0]]


    main(G)
    
     
test()