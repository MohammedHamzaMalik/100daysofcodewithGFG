## Problem:
***Check Tree Traversal***
Given ***Preorder, Inorder and Postorder*** traversals of some tree of size N. The task is to check if they are all of the same tree or not.
For more information about problem -- click [here](https://practice.geeksforgeeks.org/problems/cb02d40f50b0113c47cd9036e5f340bb51b32289/1#)

---

## Approach:
Using *recursion* we will first check the left subtree and then check the right subtree.
And then return if both are present or 0

---

## Explanation:
1. First using the size of tree we will check if the size is 0 then return 0
2. If the size is 1 then check if the Preorder, Inorder and Postorder traversals of the one element is equal then return it.
3. Using a variable and giving it value of -1.
4. Then search for first element of preorder in inorder array using a for loop.
5. If the value of that variable doesn't changes return 0.
6. Then matching element in postorder array if doesn't matches then return 0.
7. Using the recursion method first check the left subtree and then right subtree.
8. Then if both of the subtree matches with 1 then return 1 else return 0.
