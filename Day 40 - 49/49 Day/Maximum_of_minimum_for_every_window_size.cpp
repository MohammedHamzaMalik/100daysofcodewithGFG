// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to find maximum of minimums of every window size.
    vector <int> maxOfMin(int arr[], int n)
    {
        // Your code here
        vector<int>preSmall;
       stack<int>pre;
       pre.push(0);
       preSmall.push_back(-1);
       for(int i=1;i<n;i++) {
           while(!pre.empty() && arr[pre.top()]>=arr[i])
{
              pre.pop();
           }
           preSmall.push_back(pre.empty()? -1: pre.top());
           pre.push(i);
       }
       
       stack<int>nex;
       vector<int>nexSmall(n);
       // nex.push(n-1);
       // nexSmall.push_back(n);
       for(int i=n-1;i>=0;i--)
{
           while(!nex.empty() && arr[nex.top()]>=arr[i])
{
               nex.pop();
           }
           nexSmall[i]=(nex.empty()?n:nex.top());
           nex.push(i);
       
       }
       
       vector<int>ans(n+1);
       for(int i =0;i<n;i++) { 
           int len((nexSmall[i]-preSmall[i])-1); 
           ans[len]=max(ans[len],arr[i]); 
       }
       for(int i=n-1;i>=1;i--)
{
           ans[i]=max(ans[i],ans[i+1]);
       }
       ans.erase(ans.begin());
       return ans;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution ob;
        vector <int> res = ob.maxOfMin(a, n);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends

//   r: https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/