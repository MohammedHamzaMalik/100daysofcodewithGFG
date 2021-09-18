#User function Template for python3

def sum_of_query(arr,l,r):
    sum_of_each_query=0
    for i in range(l-1,r):
        sum_of_each_query+=arr[i]
    return sum_of_each_query
    
class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        query_sum_list=[]
        # for i in range(q):
        i=0
        while(i<q):
            query_sum_list.append(
                sum_of_query(arr,queries[i*2],queries[i*2+1]))
            i+=1
        return query_sum_list
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it,end=" ")
        print()
# } Driver Code Ends
