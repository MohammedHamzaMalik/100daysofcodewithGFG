#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            final_array = array1+array2
            # sorted(final_array)
            final_array.sort()
            size = len(final_array)
            if size%2!=0:
                return int(final_array[size//2])
            else:
                median = (final_array[size//2-1]+final_array[size//2])/2
                if median == int(median):
                   return int(median)
                else:
                   return median
                   
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends
