'''
Problem: Factorials of large numbers
Given an integer N, find its factorial.
'''
#User function Template for python3

class Solution:
    def factorial(self, N):
        #code here
        fact=1
        while(N>=1):
               fact*=N
               N-=1
        
        return str(fact)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends
