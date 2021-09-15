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
