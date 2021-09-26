## Problem:
Count Occurences of Anagrams
Given a word ***pat*** and a text ***txt***. Return the count of the occurences of anagrams of the word in the text.
For more information click [here](https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1#)
---
## Approach:
- In this problem, we will be using an empty ***dictionary*** in which we will store the text for which we have to ***find the number of anagrams.***
- By iterating over the given text and using the specific conditions for finding the anagrams we will return the final answer.
---
## Explanation:
1. First take two variables and store the length of the ***pat*** and ***txt*** word in each one respectively.
2. Then create an empty dictionary which will further store each alphabet of the pat word.
3. Use a for loop to iterate over the pat word and store each alphabet in the dictionary.
4. Afterwards create a variable that will store the length of the dictionary.
5. Use a while loop to iterate over the txt word.
6. If the length and the length of pat is equal and the length of dictionary is also 0 then increment our answer by 1.
7. Then check that if the present alphabet of txt is there in the dictionary or not.
8. Similarly repeat the process until the while loop stops and then return the answer.
