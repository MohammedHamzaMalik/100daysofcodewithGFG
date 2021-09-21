'''
Problem: Dam of Candies
Geek wants to make a special space for candies on his bookshelf. Currently, it has N books, each of whose height is represented by the array height[] and has unit width.
Help him select 2 books such that he can store maximum candies between them by removing all the other books from between the selected books. The task is to find out the area between two books that can hold the maximum candies without changing the original position of selected books. 
'''
#Back-end complete function Template for Python 3

 
class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        result=0
        start=0
        end=n-1
       
        for i in range(end):
            area=min(height[end],height[start])*(end-start-1)
            result=max(result,area)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr,n))



# } Driver Code Ends

'''
Explaation and Approach:
1 -> first I created 3 variables one to store the result, second to index the starting point and the last one for indexing the ending point.
2 -> then running a for loop over the height array.
3 -> then using min we will find out the minimum value between start and end and then multiply it to get the area.
4 -> then finding out the maximum value between the result and the area using the max method.
5 -> then by using an if else condition we hve incremented the start and end variable.
6 -> at last returning the value of result.
'''
