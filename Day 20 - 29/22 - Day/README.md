# Edit Distance 📝
## Problem
Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:
1. Insert a character at any position of the string.
2. Remove any character from the string.
3. Replace any character from the string with any other character.

For more info. about the problem visit this [link](https://practice.geeksforgeeks.org/problems/edit-distance3702/1#)

---
## Approach
- We can simply use a Naive recursive approach to solve this problem.
- The aim is to analyse each character one at a time, starting from the left or right side of both strings.
- Let's start in the right corner; for each pair of characters traversed, there are two options.
- Nothing to do if the last characters of two strings are the same. Ignore the final few characters and get the total number of strings. As a result, we repeat for lengths m-1 and n-1.
- Otherwise, we consider all operations on ‘str1', all three operations on the last character of the first string, recursively compute minimal cost for all three operations, and choose the lowest of three results.

- Insert: Repeat for m and n-1 times.
- Remove: For m-1 and n, repeat.
- Replace: Recur for m-1 and n-1

---
## Explanation
1. Make a recursive function to calculate the minimum operations
2. In this function first check if the length of any one of the string is 0, then return the other non zero length of the string.
3. Then check if the last index value is same for both the string or not.
4. If the condition satisfies then return the count for remaining elements.
5. If the last characters of the first string are not the same, consider all three operations on the last character of the first string, compute the minimum cost for all three operations recursively, and take the lowest of the three results.

Reference: [GeeksforGeeks](https://www.geeksforgeeks.org/edit-distance-dp-5/)