class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sortedInsert(self,s, element):
 
        # Base case: Either stack is empty or newly inserted
        # item is greater than top (more than all existing)
        if len(s) == 0 or element > s[-1]:
            s.append(element)
            return
        else:
     
            # Remove the top item and recur
            temp = s.pop()
            self.sortedInsert(s, element)
     
            # Put back the top item removed earlier
            s.append(temp)
    
    def sortStack(self,s):
     
        # If stack is not empty
        if len(s) != 0:
     
            # Remove the top item
            temp = s.pop()
     
            # Sort remaining stack
            self.sortStack(s)
     
            # Push the top item back in sorted stack
            self.sortedInsert(s, temp)
    def sorted(self, s):
        # Code here
        self.sortStack(s)
        s.reverse()

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(0), end=" ")
        print()

# } Driver Code Ends
