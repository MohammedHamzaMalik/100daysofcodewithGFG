#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        res=0
        dictionary={}
        sumi=0
        for i in range(n):
            ans=sumi+arr[i]
            if ans==0:
                res=i+1
                sumi+=arr[i]
            elif ans in dictionary:
                res=max(res,i-dictionary[ans])
                sumi+=arr[i]
            else:
                dictionary[ans]=i
                sumi+=arr[i]
        return res

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
