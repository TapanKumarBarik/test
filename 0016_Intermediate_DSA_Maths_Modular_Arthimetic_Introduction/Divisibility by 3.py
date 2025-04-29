"""
Problem Description

Given a number in the form of an array A of size N. Each of the digits of the number is represented by A[i]. Check if the number is divisible by 3.


Problem Constraints

1 <= N <= 105

0 <= A[i] <= 9

A[1] ≠ 0



Input Format

Given an integer array representing the number



Output Format

Return 1 if the number is divisible by 3 and return 0 otherwise.



Example Input

Input 1:
A = [1, 2, 3]
Input 2:
A = [1, 0, 0, 1, 2]


Example Output

Output 1:
1
Output 2:
0


Example Explanation

For Input 1:
The number 123 is divisible by 3.
For Input 2:
The number 10012 is not divisible by 3.

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        len_A = len(A)
        val = 0

        for i in range(len_A):
            val = (val + A[i]) % 3

        if val == 0:
            return 1
        return 0


# Test the function
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    A1 = [1, 2, 3]
    result1 = solution.solve(A1)
    print(f"Test case 1 result: {result1}")  # Expected output: 1

    # Test case 2
    A2 = [1, 0, 0, 1, 2]
    result2 = solution.solve(A2)
    print(f"Test case 2 result: {result2}")  # Expected output: 0