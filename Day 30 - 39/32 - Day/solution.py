from collections import defaultdict
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        mp = defaultdict(lambda:0)
     
        # initialize distinct element
        # count for current window
        dist_count = 0
        dist_arr=[]
        # Traverse the first window and store count
        # of every element in hash map
        for i in range(k):
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1
     
        # Print count of first window
        # print(dist_count)
        dist_arr.append(dist_count)
         
        # Traverse through the remaining array
        for i in range(k, n):
     
            # Remove first element of previous window
            # If there was only one occurrence,
            # then reduce distinct count.
            if mp[arr[i - k]] == 1:
                dist_count -= 1
            mp[arr[i - k]] -= 1
         
        # Add new element of current window
        # If this element appears first time,
        # increment distinct element count
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1
     
            # Print count of current window
            # print(dist_count)
            dist_arr.append(dist_count)
            
        return dist_arr

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends

# reference: https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/