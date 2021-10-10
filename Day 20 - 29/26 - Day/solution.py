#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3
import bisect
class Solution:
    def ValidPair(self, a, n): 
        # Your code goes here
        # sort the given array
        a.sort()
        # make a variable to store the count
        ans = 0

        # iterating over the array using a for loop
        for i in range(n - 1):
            if a[i] > 0:
                k = n - i - 1
                ans += k * (k + 1) // 2
                return ans
            # finding the index using the bisect 
            ind = bisect.bisect_left(a, 1 - a[i])
            if ind < n:
                ans += n - ind

        return ans

#{ 
#Driver Code Starts.

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.ValidPair(array, n)
        print(ans) 



#} Driver Code Ends