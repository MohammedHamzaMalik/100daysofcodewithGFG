'''
Problem of the day: Sum of Query II
You are given an array arr[] of n integers and q queries in an array queries[] of length 2*q containing l, r pair for all q queries. You need to compute the following sum over q queries.
If you want more idea about the problem visit this link: https://practice.geeksforgeeks.org/problems/sum-of-query-ii5310/1#  
'''
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

'''
Explanation:
Step by step explanation is provided below:
1 -> First I made a function sum_of_query with an array,l and r as three its parameters that will return the sum of a query.
2 -> This function contains a variable that will store the sum of that query.
3 -> then I have iterated over a range of starting and ending point of the query & added the value of array elements to the variable.
4 -> then in the main function I have made a new list which will contain the sum of each query.
5 -> then using a for loop I iterated over the range of q and added the sum of each query to the new list using the previously made function.
     and this main function will return the list containing the sum of each query.
'''
