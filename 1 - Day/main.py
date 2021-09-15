'''Problem => Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.'''

'''Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)'''

#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        arr.sort()

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

'''
Explanation:
In Python there is a built-in method list.sort(), which will sort a list simple ascending order.
There is also a built-in function sorted(list) which will return a new sorted list.
The difference between both of them is that the list.sort() method is only defined for lists, whereas the sorted() function accepts any iterable.

For sorting in descending order add a reverse parameter with a boolean value (reverse=True).

Key Functions can also be used to sort according to the key. 
Both list.sort() and sorted() have a key parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.

For more information check out the the documentation: https://docs.python.org/3/howto/sorting.html
'''
