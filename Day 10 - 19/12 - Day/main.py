#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
        # code here
        l_txt=len(txt)
        p_txt=len(pat)
        dicti={}
        for i in pat:
            dicti[i]=dicti.get(i,0)+1
        i=0
        j=0
        count=len(dicti)
        ans=0
        length=0
        # for i in range(0,l_txt+1):
        while(i<l_txt):
            if length==p_txt:
                if count==0:
                    ans+=1
                    if txt[i] in dicti:
                        dicti[txt[i]]=dicti[txt[i]]+1
                        if dicti[txt[i]]==1:
                            count+=1
                    i+=1
                    length-=1
                else:
                    if txt[i] in dicti:
                        dicti[txt[i]]=dicti[txt[i]]+1
                        if dicti[txt[i]]==1:
                            count+=1
                    i+=1
                    length-=1
            else:
                if j!=l_txt:
                    if txt[j] in dicti:
                        dicti[txt[j]]=dicti[txt[j]]-1
                        if dicti[txt[j]]==0:
                            count-=1
                        j+=1
                        length+=1
                    else:
                        j+=1
                        length+=1
                else:
                    break
	    return ans
	            
	    
	    
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends
