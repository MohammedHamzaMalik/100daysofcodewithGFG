## Problem
: **Largest subarray with 0 sum**
Given an **array** having both positive and negative integers. The task is to **compute the length of the largest subarray with *sum 0***.
For more information click [here](https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#)

---

## Approach
: The approach is simple, suppose we are at *ith* position and after *kth* steps we reach at *(i+k)* position & if the value at *ith* position is same as at *(i+k)* position i.e. the element between *i* and *i+k* has sum=0.
The reason is that if after taking some steps if there is no change in the value and adding 0 in such case would not change the value either so in that case the length is equal to *(i+k-i)* i.e. *(k)*.
This means that our present position and where we were having the same value & to check that the value at such position is repeated or not we will use ***Hashmaps***.
We will check that if at certain position the sum is 0 then the answer will be the position ***i*-1**.

---

## Explanation:
1. First make a variable with value 0 to store the result
2. Then make an empty dictionary
3. And make a variable to store the sum.
4. Iterate over using a for loop.
5. Then make another variable that will store the current sum and value of each element pf array.
6. And if that value is equal to 0
7. If it is then increase the result by *one and the index of that element*.
8. If not then check in the dictionary that we created earlier that what is maximum the value of *result* or the *index minus the element of dictionary*.
9. If both of the conditions are not true then give the dictionary element the value of that index and add the value of element to the overall sum.
10. Atlast return the value of result as our answer.
