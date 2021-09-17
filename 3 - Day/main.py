'''
Problem: K-th element of two sorted Arrays
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
The task is to find the element that would be at the k’th position of the final sorted array.
'''
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

'''
Explanation:
In this I have simply used the for loops and if condition.
1 -> first I have made a new array in which I will be storing the elements of both of the arrays
2 -> then I have iterated over the first array and added of its element in the final array
3 -> similarly I have done the same process on the second array
4 -> then using sort built-in method I have sorted the final array (you can use any of the sorting method)
5 -> then I have iterated over the final array and checked if the position of any of the element of the final array is eqaul to k. If yes then I have returned the element just before the position which is equal to k.  
'''
