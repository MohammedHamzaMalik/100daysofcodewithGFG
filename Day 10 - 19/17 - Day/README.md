# Check for BST 🌳 
## Problem
**Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:**
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
For more info. click [here](https://practice.geeksforgeeks.org/problems/check-for-bst/1#)

---
## Approach
- A simple approach is to make a utility helper function that will traverse down the tree.
- This will keep the track of the narrowing of a min and max value.
- The initial values for min and max should be **-4294967296** and **4294967296** respectively, they narrow from there. 

---
## Explanation
1. First make a utility function with parameters: **node, min & max.**
2. In this function first check if node is **None** or not and return **True.**
3. And return False if the data of node is less than min or greater then max.
4. Else check and return the subtrees recursively tightening the min and max constraint.
5. Then in the main function use the utility function with the 3 parameters.
6. And return the value.
