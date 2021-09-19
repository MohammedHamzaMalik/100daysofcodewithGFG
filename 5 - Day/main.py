'''
Problem: Median of 2 Sorted Arrays of Different Sizes
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.
For more information visit: https://practice.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1
'''
#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            final_array = array1+array2
            # sorted(final_array)
            final_array.sort()
            size = len(final_array)
            if size%2!=0:
                return int(final_array[size//2])
            else:
                median = (final_array[size//2-1]+final_array[size//2])/2
                if median == int(median):
                   return int(median)
                else:
                   return median
                   
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends

'''
Explanation:
We are given two arrays which are sorted for length m,n respectively.
...
1 -> first I have made a new final_array and have added both the array in it.
2 -> then I have sorted the final_array using the .sort method.
3 -> made a new variable 'size' which will contain the size of the final_array.
4 -> then using a simple if else condition, I have checked if the size is odd then it will return the middle element.
5 -> else if the size is even then the median will be the average of elements at index ((m+n)/2 – 1) and (m+n)/2 in the array.
6 -> then in the else condition itself, I have added another if else condition.
7 -> this will check if the median is an integer type then it will return a median of int type.
8 -> if it is not an integer type then it will return a float type value.
'''
