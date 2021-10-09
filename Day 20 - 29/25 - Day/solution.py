#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        i,j=0,0;
        while((n+m>2) and (k>2*(n+m-2))):
            k-=2*(n+m-2);
            i+=1;
            j+=1;
            n-=2;
            m-=2;
        for l in range(0,m):
            if(k==1): return a[i][j];
            j+=1;
            k-=1;
        j-=1;
        i+=1;
        for l in range(0,n-1):
            if(k==1): return a[i][j];
            i+=1;
            k-=1;
        i-=1;
        j-=1;
        for l in range(0,m-1):
            if(k==1): return a[i][j];
            j-=1;
            k-=1;
        j+=1;
        i-=1;
        for l in range(0,n-2):
            if(k==1): return a[i][j];
            i-=1;
            k-=1;


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends