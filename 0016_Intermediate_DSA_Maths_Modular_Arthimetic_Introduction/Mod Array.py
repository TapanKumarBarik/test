"""
Problem Description

You are given a large number in the form of a array A of size N where each element denotes a digit of the number.
You are also given a number B. You have to find out the value of A % B and return it.



Problem Constraints

1 <= N <= 105
0 <= Ai <= 9
1 <= B <= 109


Input Format

The first argument is an integer array A.
The second argument is an integer B.


Output Format

Return a single integer denoting the value of A % B.


Example Input

Input 1:
A = [1, 4, 3]
B = 2
Input 2:

A = [4, 3, 5, 3, 5, 3, 2, 1]
B = 47


Example Output

Output 1:
1
Output 2:

20


Example Explanation

Explanation 1:
143 is an odd number so 143 % 2 = 1.
Explanation 2:

43535321 % 47 = 20
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        mod = B
        n = len(A)
        curr = 1
        for i in range(n - 1, -1, -1):
            dig = A[i]
            term = (dig * curr) % mod
            ans = (ans + term) % mod
            curr = (curr * 10) % mod
        return ans

# Test the function
if __name__ == "__main__":
    solution = Solution()
    A = [1, 4, 3]
    B = 2
    result = solution.solve(A, B)
    print(result)  # Output: 1

    A = [4, 3, 5, 3, 5, 3, 2, 1]
    B = 47
    result = solution.solve(A, B)
    print(result)  # Output: 20