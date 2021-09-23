'''
Problem: Count total set bits
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
For more information visit this link: https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#
'''
#User function Template for python3
# def DecimalToBinary(num):
#     return bin(num).replace("0b", "")

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        i,ans = 0,0
        
        while ((1 << i) <= n) :
            k = 0
            change = 1 << i
            j=0
            while(j<n+1):
                ans += k
                if change == 1 :
                    k = not k
                    change = 1 << i
                else :
                    change -= 1
                j+=1
            i += 1
        return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends

'''
Explanation:
Using a simple approach that the bits get inverted after 2^i position in vertical sequence if observed from the rightmost side at a distance of i.
1 -> first create two variables one for iterating while loop and second to store our answer.
2 -> using a while loop iterate till n is greater than equal to 2^i
3 -> then again loop from 0 to n for every bit position.
4 -> then add the value to our ans variable.
5 -> then check if the iterator is equal to 1 then flip the bit and again set it to 2^i
6 -> at last return the ans variable.
'''
