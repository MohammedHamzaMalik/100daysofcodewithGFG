#User function Template for python3

class Solution: 
    def candies(self, m,n): 
        # Your code goes here 
		# ans=int(((m-1)*(n-1)/2))
		i = 0
    	X = (m * n) - m - n

    	queue = []
    	queue.append(X)
    	set = {X}

    	ans = 0
    	while (len(queue) > 0):
    		curr = queue[0] 
    		queue.remove(queue[0])

    		ans += 1
    		key = curr-m
    		if (key > 0 and key not in set):
    			queue.append(key)
    			set.add(key)

    		key = curr-n
    		if (key > 0 and key not in set):
    			queue.append(key)
    			set.add(key)
				
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
	
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
    	arr = list(map(int, input().strip().split()))
    	m = arr[0]
    	n = arr[1]
    	obj = Solution()
    	print(obj.candies(m,n)) 



# } Driver Code Ends
