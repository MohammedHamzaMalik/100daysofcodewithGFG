    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort();
        res=0;
        # for(int i=0;i<n-2;i++){
        for i in range(0,n-1):
            j=i+1;
            k=n-1;
            while(j<k):
                total=arr[i]+arr[j]+arr[k];
                if(total<sumo):
                    res+=(k-j);
                    j+=1;
               # }
                else:
                    k-=1;
               # }
           # }
        # }
        return res;

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends