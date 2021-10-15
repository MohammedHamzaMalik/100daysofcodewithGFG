#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        number = n
        foundodd = ""
        makebyte = ""
        stringchange = ""
        remove0b = ""
        convertintbinary = bin(number)
        remove0b = convertintbinary.lstrip('0b')
        binarylength = len(remove0b)
        if binarylength % 2 == 1:
            remove0b = '0' + remove0b
            binarylength = len(remove0b)
        for count in range(binarylength, 0,-2):
            findodd = remove0b[count-2:count]
            if findodd == "01":
               foundodd = "10"
            elif findodd == "10":
                foundodd = "01"
            else:
               foundodd = findodd           
            stringchange = foundodd + stringchange
        makebyte = '0b' + stringchange
        number = int(makebyte, base=2)
        return number

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends