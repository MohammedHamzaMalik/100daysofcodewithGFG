int maxSumPairWithDifferenceLessThanK(int a[], int n, int k) {
   int ans = 0;
   sort(a, a + n);
   for (int i = n - 1; i >= 1; i--)if (a[i] - a[i - 1] < k)ans += a[i] + a[i - 1], i--;
   return ans;
}
