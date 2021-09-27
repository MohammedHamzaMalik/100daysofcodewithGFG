# Problem:
***Finding middle element in a linked list***
Given a singly linked list of **N** nodes.
The task is to find the **middle** of the linked list. For example, if the linked list is
**1-> 2->3->4->5**, then the middle node of the list is 3.
If there are two middle nodes(in case, when **N** is even), print the second **middle** element.
For example, if the linked list given is **1->2->3->4->5->6**, then the middle node of the list is **4**.
For more information about the problem, visit this [link](https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1#)
---
# Approach:
### Method 1
- To solve this problem of linked list we will use **pointers**.
- By traversing over the linked list, **count the number of nodes.**
- After that traverse over the list again till the half of the count value.
- And return the node at the half of the count value.
### Method 2:
- In this method instead of using a single pointer, use two pointers.
- One will move fast and other will move slow.
- When the fast pointer reaches the end, the slow pointer will reach the middle of the linked list.
- And return the node on which the slow pointer is pointing.
---
# Explanation:
1. First make two pointers, both of them pointing towards the head node.
2. Then Iterate till fast pointer's next is null, for example use a while.
3. In this loop increase the slow pointer towards its next and the fast pointer towards its next of next.
4. And return the value of node at which the slow pointer is pointing.

Reference: [GeeksforGeeks](https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/)
