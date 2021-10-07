# Elixir of Life 🧬 
## Problem
Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden.
The garden consists of various plants represented by string S, where each letter represents a different plant.  But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring) at the beginning of the forest (prefix), the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.

Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest.

For more info. click [here](https://practice.geeksforgeeks.org/problems/20290dc4188d384ae1f17d6a14bd2c95ea7012a8/1#)
---

## Approach
- By iterating till the middle element of the string and checking if both the sides are equal or not.
- And then adding the specific substring if the condition is matched.
- Then add the count of the total substrings and return it.
---

## Explanation
1. First check the condition if the length of the string is 1 or not.
2. If the condition is true then return 1
3. If not then make an empty array to store all the substrings.
4. Then iterate till the middle element of the string and checking if both the sides of the string are equal or not.
5. If the condition is matched then append that substring to the empty array created.
6. Then again create an empty array to store the count of the aquired substring in string.
7. Then return the maximum of the array.
