#User function Template for python3

class Solution:
    def smallestRange(self, numbers, n, k):
        # code here
        # print the smallest range in a new line
        ptr = [0 for i in range(501)]            
        i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0
             
        # initializing to 0 index
        for i in range(k + 1):
            ptr[i] = 0
     
        minrange = 10**9
             
        while(1):   
             
                # for maintaining the index of list
                # containing the minimum element
            minind = -1
            minval = 10**9
            maxval = -10**9
            flag = 0
     
            # iterating over all the list
            for i in range(k):
                 
                    # if every element of list[i] is
                    # traversed then break the loop
                if(ptr[i] == n):
                    flag = 1   
                    break
     
                # find minimum value among all the list
                # elements pointing by the ptr[] array
                if(ptr[i] < n and numbers[i][ptr[i]] < minval):
                    minind = i # update the index of the list
                    minval = numbers[i][ptr[i]]
                 
                # find maximum value among all the
                # list elements pointing by the ptr[] array
                if(ptr[i] < n and numbers[i][ptr[i]] > maxval):
                    maxval = numbers[i][ptr[i]]
                 
             
     
            # if any list exhaust we will
            # not get any better answer,
            # so break the while loop
            if(flag):
                break
     
            ptr[minind] += 1
     
            # updating the minrange
            if((maxval-minval) < minrange):
                minel = minval
                maxel = maxval
                minrange = maxel - minel
            
        return minel,maxel
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends
