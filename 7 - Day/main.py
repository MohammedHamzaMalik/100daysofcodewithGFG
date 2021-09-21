
#Back-end complete function Template for Python 3

 
class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        ans=0
        l=0
        r=n-1
       
       # while(l<r):
        for i in range(r):
            area=min(height[r],height[l])*(r-l-1)
            ans=max(ans,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr,n))



# } Driver Code Ends
