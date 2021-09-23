#User function Template for python3
# def DecimalToBinary(num):
#     return bin(num).replace("0b", "")


class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        two = 2
        ans = 0
        N = n
        while(n != 0):
            ans += int(N / two) * (two >> 1)
            if((N & (two - 1)) > (two >> 1) - 1):
                ans += (N&(two - 1)) - (two >> 1) + 1
            two <<= 1;
            n >>= 1;
        return ans
        # return the count
        # x=0
        # arr=[]
        # for i in range(n):
        #     b=DecimalToBinary(i)
        #     arr.append(b)
            
        # for i in arr:
        #     for j in i:
        #         if i==1:
        #             x+=1
                    
        # return x
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends
