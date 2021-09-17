#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        final = []
        for i in range(len(arr1)):
            final.append(arr1[i])
        for i in range(len(arr2)):
            final.append(arr2[i])
        final.sort()
        
        for i in range(len(final)):
            if i==k:
                return final[i-1]
                # break
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
