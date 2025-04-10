What is the time and space complexity for printing the sum of each subarray?

```python

int n = ar.length;

for(int i = 0 ; i < n ; i++){
    
    int sum = 0;
    
        for(int j = i ; j < n ; j++){
        
            sum = sum + ar[j];
            
            print(sum)
        
        }
    
    }

}
```

TC = O(N^2) , SC = O(1)
```