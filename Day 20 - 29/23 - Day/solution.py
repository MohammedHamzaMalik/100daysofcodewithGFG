#User function Template for python3

class Solution:
    def maxFrequency(self, S):
        # code here
		# if length of string is 1
        if(len(S)==1):
           return 1
        
		# list to collect all possible substring for given problem
        st=[]
        
        # iterating till the mid element of string
        for i in range(len(S)//2):
           # print(S[i])
           if(S[i]==S[-1]):
			   # checking if substring is equal from both sides
               if(S[:i+1]==S[len(S)-i-1:]):
                   # print(S[:i+1])
                   st.append(S[:i+1])
        
		# count of aquired substring in string
        maxi=[]
        for i in st:
           maxi.append(S.count(i))
                
		# if maxi is empty return 1
        if not maxi:
           return 1
        else:
           return max(maxi)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        Str = input()
        obj = Solution()

        print(obj.maxFrequency(Str))

# } Driver Code Ends
