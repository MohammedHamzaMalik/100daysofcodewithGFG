# Problem:
**Sort a stack.**
Given a stack, the task is to sort it such that the top of the stack has the **greatest element.**
For more information about the problem click [here](https://practice.geeksforgeeks.org/problems/sort-a-stack/1#)

---
# Approach:
The approach is to use recursion to keep all values in the Function Call Stack until it is empty. When the stack is empty, place all held items in sorted order one by one. ***The importance of sorting order is critical here.***

---
# Explanation:
- First make a function for **inserting an element in a sorted manner.**
1. In this function first check if the ***length of the stack is 0*** or ***the present element is greater than the top element.***
2. If this condition is ***true***, then ***add that element to the stack*** and return.
3. If the condition is ***false***, then ***pop*** the last element from the stack and use ***recursion*** and append the element that is removed.
- Make another function for **sorting and putting the elements back in the stack.**
5. In this function put the condition, ***if the length of stack is not zero.***
6. If this condition is ***true***, then ***pop the last item*** from the stack and save it in a temp variable.
7. Then use ***recursion method*** for the remaining stack.
8. After that push the top item ***temp*** back in the sorted stack.
9. At last in the main sorted function, implement the ***second function*** which we created earlier.
10. Till now we get the stack that is ***sorted***, but we want the stack in ***reverse sorted manner***, so use the *reverse method* on the ***stack*.** 
