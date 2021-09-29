# Restricted Pacman 🕹
## Day 15 - Problem
In the game of Restricted Pacman, an infinite linear path is given. Pacman has to start at position 0 and eat as many candies as possible. In one move he can only jump a distance of either M or N.  If M and N are coprime numbers, find how many candies will be left on the board after the game is over.
Note: The result is always finite as after a point X every index in the infinite path can be visited.
For more information visit this [link](https://practice.geeksforgeeks.org/problems/2caf0501a39567d653197364a2b5c8a9f5943b7e/1#)

---
## Approach
Find the largest index that can’t be obtained using any combination of M & N using Frobenius Number ( don't know what this is? check out this [wiki](https://en.wikipedia.org/wiki/Coin_problem) ) which defines X = (M * N) – M – N. Add X to a queue. X is the largest index than cannot be visited so every index greater than X need not be checked. Now add X-M and X-N to the queue and so on.

---

## Explanation
This👇 is the main part of the code.
```python
# So we only need to check for numbers 
# less than or equal to (mn - m - n)
ans=int(((m-1)*(n-1)/2)) 
# Return the ans. YES THAT'S IT😮!
return ans
```
1. First make a that will store this **((m-1)x(n-1))/2** value of **Frobenius Number**.
2. Then make an empty queue and add the above value in it.
3. Then make a set of value of the Frobenius Number.
4. Then make a variable that will store our answer with initial value of zero 0.
5. Then use a while loop with a condition that length of queue is greater than zero.
6. In the loop first assign a variable the value of first element of the queue.
7. Then remove that element from the queue.
8. Now increment the ans with 1.
9. And make a key with a value of first element of queue minus the value of m.
10. Now check if the value of key is greater than zero and it is not present in the set.
11. Then add that key in the queue and in the set.
12. Similarly repeat the process with the replacing m with n in the value of key.
13. Now return our answer and that's it.
