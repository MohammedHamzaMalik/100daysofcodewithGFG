// { Driver Code Starts
// kth largest element in a 2d array sorted row-wise and column-wise
#include<bits/stdc++.h>
using namespace std;
#define MAX 1000
int mat[MAX][MAX];
int kthSmallest(int mat[MAX][MAX], int n, int k);
// driver program to test above function
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
    
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                cin>>mat[i][j];
        int r;
        cin>>r;
        cout<<kthSmallest(mat,n,r)<<endl;
    }
     // cout << "7th smallest element is " << kthSmallest(mat, 4, 7);
      return 0;
}
// } Driver Code Ends

struct HeapNode {
    int val;
    int r;
    int c;
};
void minHeapify(HeapNode harr[], int i, int heap_size)
{
    int l = i * 2 + 1;
    int r = i * 2 + 2;
     if(l < heap_size&& r<heap_size && harr[l].val < harr[i].val && harr[r].val < harr[i].val){
            HeapNode temp=harr[r];
            harr[r]=harr[i];
            harr[i]=harr[l];
            harr[l]=temp;
            minHeapify(harr ,l,heap_size);
            minHeapify(harr ,r,heap_size);
        }
          if (l < heap_size && harr[l].val < harr[i].val){
            HeapNode temp=harr[i];           
            harr[i]=harr[l];
            harr[l]=temp;
            minHeapify(harr ,l,heap_size);
        }
}


int kthSmallest(int mat[MAX][MAX], int n, int k)
{
  //Your code here
  if (k < 0 && k >= n * n)
        return INT_MAX;
    HeapNode harr[n];
    for (int i = 0; i < n; i++)
        harr[i] = { mat[0][i], 0, i };
 
    HeapNode hr;
    for (int i = 0; i < k; i++) {
        hr = harr[0];
        int nextval = (hr.r < (n - 1)) ? mat[hr.r + 1][hr.c]: INT_MAX;
        harr[0] = { nextval, (hr.r) + 1, hr.c };
        minHeapify(harr, 0, n);
    }
    return hr.val;
}
