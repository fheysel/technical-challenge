# technical-challenge
***Problem statement:*** Calculate the shortest path in a fully connected graph that visits each vertex exactly once

## Initial thoughts / Background research
Calculating the shortest path by visiting every vertex in a graph exactly once is highly related to the Travelling Salesman and Hamiltonian Cycle problems - two well known NP-Hard problems.
For the purposes of this challenge, I focus on finding a suitable heuristic to find an approximate solution, rather than a non-polynomial time exact solution.
The overall logical flow of the algorithm is as follows:
1. Calculate the graph's Minimum Spanning Tree (MST) using Prim's algorithm
2. Convert the MST into a path by performing a pre-order traversal through the tree.

This solution is proven to be a 2-approximate of the optimal solution and is proven [here](https://www.geeksforgeeks.org/travelling-salesman-problem-set-2-approximate-using-mst/)
  
## Assumptions
1. All distances in the graph are positive floats or integers
2. No distance will be greater than 999999.99
3. All graphs are fully connected and satisfy the [triangle inequality](https://www.britannica.com/science/triangle-inequality).

## Improvements
Given more time to work on the problem I would make the following improvements to the solution:
1. Use minheap to store MST. By using a MST rather than a list to store the MST the runtime could have been reduced from O(V^2) to O(ElogV).
2. Use an external tree library to represent the MST (if still using tree rather than minheap) this would help extract out the display and traversal of the tree. Lending to better readibility and maintainability. An external library was chosen not to be used as the final solution is a code source (not a docker container) and I did not want to run the risk of the tester being unable to run the code due to dependancy errors.
3. Adding data visualization and graphing to help view results and understand them visually.
4. Adding excepion handling. Currently the system has no excpetion handling and assumes perfect-scenario inputs.
5. Unit testing. Adding a unit testing suite to check for edge cases and improve maintainability.
6. Docker file and publication. Given more time I would have liked to create a docker file so that the code can utilize external libraries and be published in the AWS cloud.

## Alternatives considered.
Other algorithms considered during the development process are:
1. Brute force. Due to the small verticy limit of 20 verticies max, checking all pat permutations and selecting the least cost solution would have been able to execute in milisecond-level time. However, this solution was not selected in order to build in scalability to the solution and demonstrate good domain knowledge.
2. Using Kruskal's MST algorithm instead of Prim's. Not selected as Kruskal's performs best in sparse graphs, in a fully connected graph Prim's should perform better.
3. Several non-polynomial time algorithms were considered but not selected. These algorithms include:
  * Least-cost branch and bound 
  * Dynamic programming
  * Naive greedy algorithm
