# Detect cycle in an undirected graph 
## Problem
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 
For more info. click [here](https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#)

---
## Approach
- Run a DFS from each node that hasn't been visited yet. A cycle in a graph can be detected using Depth First Traversal. 
- A tree is produced using DFS for a connected graph. 
- Only if the graph has a rear edge does it have a cycle. 
- A back edge in the DFS tree is an edge that connects a node to itself (self-loop) or one of its ancestors.
- Keep a visited array to discover the back edge to any of its ancestors, and if there is a back edge to any visited node, do a loop and return true.

## Explanation
1. Create a graph with the number of edges and vertices specified.
2. Create a recursive function with the current index or vertex, visited array, and parent node as parameters.
3. Assign the status of visited to the current node.
4. Find all the vertices that haven't been visited yet that are near the current node. Call the function for those vertices recursively, and if it returns true, return true.
5. Return true if the nearby node is not a parent and has already been visited.
6. Make a wrapper class that calls the recursive function for all vertices and returns true if any of the functions return true.
7. Otherwise, if the function returns false for all vertices, return false.

Reference: [GeeksforGeeks](https://www.geeksforgeeks.org/detect-cycle-undirected-graph/)
