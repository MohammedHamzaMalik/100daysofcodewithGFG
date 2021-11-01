#User function Template for python3

class Solution:
	def isCircularPrime(self, n):
		# Code here
        if n==1:
	        return 0
	    size = len(str(n))
	    t = size
	    while size>0:
	        for i in range(2,(n//2)+1):
	            if n%i==0:
	                return 0
	        temp = str(n)
	      
	        n = int(temp[t-1:]+temp[:t-1])
	        size-=1
	    return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.isCircularPrime(n)
		print(ans)
# } Driver Code Ends