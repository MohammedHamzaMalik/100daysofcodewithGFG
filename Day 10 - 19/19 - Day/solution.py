class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
        visited = [0]*V
		
		def dfs(current, parent):
		    visited[current] = 1
		    
		    for i in adj[current]:
		        if not visited[i]:
		            if dfs(i, current): 
		                return True
		        elif i != parent:
		            return True
		            
		    return False
		
		for i in range(V):
		    if not visited[i]:
		        if dfs(i, -1): return True
		        
		return False
#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
