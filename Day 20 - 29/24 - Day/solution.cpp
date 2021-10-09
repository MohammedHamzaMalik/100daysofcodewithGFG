// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
	public:
	void multiply(vector<vector<int64_t>> &a, vector<vector<int64_t>> &b) {
    vector<vector<int64_t>> c(2, vector<int64_t>(2, 0));
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int l=0;l<2;l++)(c[i][j]+=a[i][l]*b[l][j])%=((int)1e9 + 7);
        }
    }
    a = c;
}
	int TotalAnimal(long long int N){
	    // Code here
	    vector<vector<int64_t>> ans(2, vector<int64_t>(2, 1)), d(2, vector<int64_t>(2, 1));
    d[1][1] = ans[0][1] = ans[1][0] = 0;
    while (N > 0) {
        if (N & 1)multiply(ans, d);
        multiply(d, d);
        N >>= 1;
    }
    return ans[0][0];
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int N;
		cin >> N;
		Solution ob;
		int ans = ob.TotalAnimal(N);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends