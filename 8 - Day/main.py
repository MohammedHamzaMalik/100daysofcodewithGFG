#User function Template for python3
def checking_substring(a,b):
    for i in a:
        if i==b:
            return True;
            
class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        
        len_a = len(A)
        len_b = len(B)
            
        i=0
        
        while(i<len_a):
        
            if A[i] == B[0]:
                k = i
                count = 1
                j=0
                while(j<len_b):
                    if k >= len_a:
                        k = 0
                        count = count + 1
                    if A[k] != B[j]:
                        break
                    k+=1
                    j+=1
                else:
                    return count
            i+=1
        return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        A=input().strip()
        B=input().strip()
        obj = Solution()
        print(obj.repeatedStringMatch(A,B))
# } Driver Code Ends
