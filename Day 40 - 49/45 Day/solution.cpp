// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{

	public:
	int find_min(int a[], int n, int k) {
        // Your code geos here
        int cnt = 0, cnt2 = 0;
    for (int i=0;i<n;i++) cnt +=(a[i]+1)/2-1, cnt2+=(a[i]%2==0);
    if (cnt2 + cnt < k)return -1;
    return n + 2 * k - max(1, k - cnt);
    }

};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        cin >> k;
        Solution obj;
        cout << obj.find_min(a, n, k) << endl;
    }
    return 1;
}
  // } Driver Code Ends