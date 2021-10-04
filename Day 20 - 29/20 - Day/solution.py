#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		one=0
		zero=0
		count,res=0,-1
		for i in S:
            if i=='1':
                one+=1
                count-=1
            elif i=='0':
                zero+=1
                count+=1
            res=max(res,count)
            if count<0:
                count=0
            # res=max(res,count)
        
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends
