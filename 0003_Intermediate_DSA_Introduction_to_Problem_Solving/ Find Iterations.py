"""
Find the number of times below code runs where N is a perfect square

for i -> 1 to N

if(i * i == N)

return i
"""

# ANSWER-sqrt(N)
def find_iterations(N):
    iterations = 0
    for i in range(1, N + 1):
        iterations += 1
        if i * i == N:
            return iterations
    return iterations

# Test cases
perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for N in perfect_squares:
    print(f"N = {N}, Iterations = {find_iterations(N)}")