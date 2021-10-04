# Maximum difference of zeros and ones in binary string
## Problem
Given a binary string S consisting of 0s and 1s. The task is to find the maximum difference of the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a string.
For more info. click [here](https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1#)

---
## Approach
- Using the a similar approach like of Kadane's algorithm.
- By traversing through the string check the index value and store the maximum difference in a varibale and return it.

## Explanation
1. Make a variable with value 0 to count the difference.
2. If the index value of string is 1 decrease the count by 1.
3. If it is 0 then increase it by 1.
4. Then using the max function store the maximum value in a variable say as result.
5. Then if the count values becomes negative change it to 0.
6. And return the result value.
