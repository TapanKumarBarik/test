Find the time and space complexity for printing sum of each subarray?

```java

void printSums(int ar[]) {
    int n = ar.length;
    int pf[N];

    // Compute prefix sums
    pf[0] = ar[0];
    for (int i = 1; i < n; i++) {
        pf[i] = pf[i - 1] + ar[i];
    }

    // Print sums of all subarrays
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (i == 0) {
                print(pf[j]);
            } else {
                print(pf[j] - pf[i - 1]);
            }
        }
    }
}
```

TC = O(N^2) , SC = O(N)