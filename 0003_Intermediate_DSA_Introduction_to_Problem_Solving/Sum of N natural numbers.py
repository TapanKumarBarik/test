"""

The sum of n natural numbers is :

(n*(n+1))/2
"""

def sum_of_natural_numbers(N):
    return (N * (N + 1)) // 2

# Example usage
N = 10
print(f"The sum of the first {N} natural numbers is: {sum_of_natural_numbers(N)}")