'''
Problem: Repeated String Match
Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. If B cannot be a substring of A no matter how many times it is repeated, return -1.
'''
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

'''
Explanation:
1 -> first made two variables that will store the length of both strings respectively
2 -> then iterate over the length of 'A' string using a for or while loop
3 -> then we check the one index of 'B' string with every index of string 'A', as 'B' will start with the same alphabet as one of the index of 'A'.
4 -> then assinging that index value to a variable 'k', and making a new variable for counting how much time a is repeated
5 -> then iterate over 'B' string and increment count as we make k zero again.
'''
