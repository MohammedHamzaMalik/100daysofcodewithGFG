# Vertical Traversal of Binary Tree 🎄
## Problem
Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.
For more info. visit this [link](https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1#)

---
## Approach
- The approach for this problem is mainly based on the hash map.
- One needs to check the horizontal distance from root for all the nodes.
- If two nodes have the same horizontal distance, then they are on the same vertical line.
- The horizontal distance(hd) is 0 for root node.
- Right subtree is considered as +1 the hd.
- Left subtree is considered as -1 the hd.
- We can do preorder traversal of the given Binary Tree. 
- While traversing the tree, we can recursively calculate hds'. 
- We initially pass the horizontal distance as 0 for root. 
- For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. 
- For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1. 
- For every HD value, we maintain a list of nodes in a hash map. 
- Whenever we see a node in traversal, we go to the hash map entry and add the node to the hash map using HD as a key in a map.

---
## Explanation
1. Utility function to store vertical order in hash map.
2. hd is horizontal distance of current node from root and is initially passed as 0
3. Make a Base Case
4. Store current node in hash map.
5. Then store nodes in left subtree.
6. Then store nodes in right subtree.
7. In the main function, create a map and store vertical order in map.
8. 
